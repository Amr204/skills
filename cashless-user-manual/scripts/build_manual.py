#!/usr/bin/env python3
"""Build a self-contained RTL user manual HTML using the locked Cashless template."""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
import re
import sys
from pathlib import Path
from typing import Any

SKILL_ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = SKILL_ROOT / "assets" / "master.css"
SHELL_PATH = SKILL_ROOT / "assets" / "manual-shell.html"
DEFAULT_LOGO = SKILL_ROOT / "assets" / "brand-logo.png"


def fail(message: str) -> "NoReturn":
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Input JSON not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
    if not isinstance(data, dict):
        fail("Top-level JSON value must be an object")
    return data


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def rich(obj: dict[str, Any], key: str, default: str = "") -> str:
    html_key = f"{key}_html"
    if html_key in obj:
        return str(obj[html_key])
    return esc(obj.get(key, default))


def cell(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("html", esc(value.get("text", ""))))
    return esc(value)


def slugify(value: str, fallback: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\u0600-\u06ff-]+", "-", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or fallback


def resolve_asset(path_value: str, input_dir: Path) -> Path:
    candidate = Path(path_value).expanduser()
    if candidate.is_absolute() and candidate.exists():
        return candidate
    for base in (input_dir, SKILL_ROOT, SKILL_ROOT / "assets"):
        resolved = (base / candidate).resolve()
        if resolved.exists():
            return resolved
    fail(f"Asset not found: {path_value}")


def data_uri(path_value: str, input_dir: Path) -> str:
    if path_value.startswith("data:"):
        return path_value
    path = resolve_asset(path_value, input_dir)
    mime, _ = mimetypes.guess_type(path.name)
    mime = mime or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def render_cover(meta: dict[str, Any], input_dir: Path) -> str:
    logo_value = str(meta.get("logo", DEFAULT_LOGO))
    logo = data_uri(logo_value, input_dir)
    brand_prefix = rich(meta, "brand_prefix", "Verto")
    brand_highlight = rich(meta, "brand_highlight", "core")
    prepared_label = rich(meta, "prepared_label", "PREPARED FOR")
    edition_label = rich(meta, "edition_label", "EDITION")
    return f"""
<section class="cover">
  <div class="cover__brand-row">
    <img class="cover__logo" src="{logo}" alt="{esc(meta.get('logo_alt', 'Brand logo'))}">
    <div class="cover__logo-text">{brand_prefix}<span>{brand_highlight}</span></div>
  </div>
  <div class="cover__center">
    <div class="cover__eyebrow">{rich(meta, 'eyebrow', 'USER MANUAL')}</div>
    <h1 class="cover__title">{rich(meta, 'title', 'System User Manual')}</h1>
    <p class="cover__subtitle">{rich(meta, 'subtitle', '')}</p>
    <p class="cover__derived">{rich(meta, 'derived', '')}</p>
  </div>
  <div class="cover__footer">
    <div>
      <div class="cover__prepared-label">{prepared_label}</div>
      <div class="cover__prepared-value">{rich(meta, 'prepared_for', '')}</div>
    </div>
    <div class="cover__edition">
      <div class="cover__edition-label">{edition_label}</div>
      <div class="cover__edition-value">{rich(meta, 'edition', '')}</div>
    </div>
  </div>
</section>"""


def normalize_chapters(data: dict[str, Any]) -> list[dict[str, Any]]:
    chapters = data.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        fail("'chapters' must be a non-empty array")
    result: list[dict[str, Any]] = []
    used_ids: set[str] = set()
    for ci, chapter in enumerate(chapters, 1):
        if not isinstance(chapter, dict):
            fail(f"Chapter {ci} must be an object")
        ch = dict(chapter)
        ch_id = str(ch.get("id") or f"ch{ci}")
        if ch_id in used_ids:
            fail(f"Duplicate id: {ch_id}")
        used_ids.add(ch_id)
        ch["id"] = ch_id
        sections = ch.get("sections", [])
        if not isinstance(sections, list):
            fail(f"Chapter {ci} 'sections' must be an array")
        normalized_sections = []
        for si, section in enumerate(sections, 1):
            if not isinstance(section, dict):
                fail(f"Chapter {ci}, section {si} must be an object")
            sec = dict(section)
            level = int(sec.get("level", 2))
            if level not in (2, 3, 4):
                fail(f"Section level must be 2, 3, or 4; got {level}")
            sec_id = str(sec.get("id") or f"{ch_id}-{si}")
            if sec_id in used_ids:
                fail(f"Duplicate id: {sec_id}")
            used_ids.add(sec_id)
            sec["id"] = sec_id
            sec["level"] = level
            normalized_sections.append(sec)
        ch["sections"] = normalized_sections
        result.append(ch)
    return result


def render_toc(meta: dict[str, Any], chapters: list[dict[str, Any]]) -> str:
    entries: list[str] = []
    for chapter in chapters:
        entries.append(f'<li class="toc__chapter">{rich(chapter, "title")}</li>')
        chapter_page = esc(chapter.get("toc_page", "—"))
        entries.append(
            f'<li><a class="toc__entry" href="#{esc(chapter["id"])}">'
            f'<span class="toc__entry-text">{rich(chapter, "title")}</span>'
            f'<span class="toc__dots"></span><span class="toc__page">{chapter_page}</span>'
            f'</a></li>'
        )
        for section in chapter["sections"]:
            cls = "toc__entry toc__entry--sub" if section["level"] == 2 else "toc__entry toc__entry--sub2"
            page = esc(section.get("toc_page", "—"))
            entries.append(
                f'<li><a class="{cls}" href="#{esc(section["id"])}">'
                f'<span class="toc__entry-text">{rich(section, "title")}</span>'
                f'<span class="toc__dots"></span><span class="toc__page">{page}</span>'
                f'</a></li>'
            )
    return f"""
<nav class="toc">
  <h2 class="toc__title">{rich(meta, 'toc_title', 'الفهرس')}</h2>
  <p class="toc__subtitle">{rich(meta, 'toc_subtitle', 'محتويات دليل الاستخدام')}</p>
  <ul class="toc__list">{''.join(entries)}</ul>
</nav>"""


def render_blocks(blocks: Any, input_dir: Path) -> str:
    if blocks is None:
        return ""
    if not isinstance(blocks, list):
        fail("'blocks' must be an array")
    out: list[str] = []
    for index, block in enumerate(blocks, 1):
        if not isinstance(block, dict):
            fail(f"Block {index} must be an object")
        kind = str(block.get("type", "p"))
        if kind == "p":
            out.append(f"<p>{rich(block, 'text')}</p>")
        elif kind == "bullets":
            items = block.get("items", [])
            cls = "bullet-list bullet-list--navy" if block.get("navy") else "bullet-list"
            out.append(f'<ul class="{cls}">' + "".join(f"<li>{cell(x)}</li>" for x in items) + "</ul>")
        elif kind == "steps":
            items = block.get("items", [])
            li = []
            for n, item in enumerate(items, 1):
                if isinstance(item, dict):
                    title = rich(item, "title")
                    body = rich(item, "body")
                    body_html = (f"<strong>{title}</strong>" if title else "") + body
                else:
                    body_html = esc(item)
                li.append(f'<li><span class="step__num">{n}</span><div class="step__body">{body_html}</div></li>')
            out.append('<ol class="steps">' + "".join(li) + "</ol>")
        elif kind == "table":
            headers = block.get("headers", [])
            rows = block.get("rows", [])
            caption = f"<caption>{rich(block, 'caption')}</caption>" if block.get("caption") or block.get("caption_html") else ""
            thead = "<thead><tr>" + "".join(f"<th>{cell(h)}</th>" for h in headers) + "</tr></thead>"
            tbody = "<tbody>" + "".join("<tr>" + "".join(f"<td>{cell(v)}</td>" for v in row) + "</tr>" for row in rows) + "</tbody>"
            out.append(f'<table class="data-table">{caption}{thead}{tbody}</table>')
        elif kind == "callout":
            variant = str(block.get("variant", "note"))
            if variant not in {"note", "warning", "tip", "important"}:
                fail(f"Unsupported callout variant: {variant}")
            icon = esc(block.get("icon", "!"))
            label = rich(block, "label", variant.upper())
            paragraphs = block.get("paragraphs")
            if paragraphs is None:
                paragraphs = [block.get("text_html", esc(block.get("text", "")))]
            rendered_ps = "".join(f"<p>{cell(p)}</p>" for p in paragraphs)
            out.append(
                f'<aside class="callout callout--{variant}"><div class="callout__label">'
                f'<span class="callout__icon">{icon}</span>{label}</div>{rendered_ps}</aside>'
            )
        elif kind == "screenshot":
            src = str(block.get("src", ""))
            if not src:
                fail("Screenshot block requires 'src'")
            uri = data_uri(src, input_dir)
            number = rich(block, "number", f"شكل {index}")
            caption = rich(block, "caption")
            out.append(
                f'<figure class="screenshot"><img src="{uri}" alt="{esc(block.get("alt", ""))}">'
                f'<figcaption><span class="fig__num">{number}</span>{caption}</figcaption></figure>'
            )
        elif kind == "info_card":
            items = block.get("items", [])
            rendered_items = "".join(
                f'<div><div class="info-card__label">{rich(item, "label")}</div>'
                f'<div class="info-card__value">{rich(item, "value")}</div></div>'
                for item in items if isinstance(item, dict)
            )
            out.append(
                f'<section class="info-card"><h4 class="info-card__title">{rich(block, "title")}</h4>'
                f'<div class="info-card__grid">{rendered_items}</div></section>'
            )
        elif kind == "workflow":
            steps = block.get("steps", [])
            rendered = []
            for n, step in enumerate(steps):
                if isinstance(step, dict):
                    text = rich(step, "text")
                    active = bool(step.get("active"))
                else:
                    text, active = esc(step), False
                cls = "workflow__step workflow__step--active" if active else "workflow__step"
                rendered.append(f'<div class="{cls}">{text}</div>')
                if n < len(steps) - 1:
                    rendered.append('<div class="workflow__arrow">←</div>')
            out.append('<div class="workflow">' + "".join(rendered) + "</div>")
        elif kind == "raw_html":
            out.append(str(block.get("html", "")))
        else:
            fail(f"Unsupported block type: {kind}")
    return "\n".join(out)


def render_chapters(chapters: list[dict[str, Any]], input_dir: Path) -> str:
    articles: list[str] = []
    for ci, chapter in enumerate(chapters, 1):
        sections_html: list[str] = []
        for section in chapter["sections"]:
            level = section["level"]
            title = rich(section, "title")
            sections_html.append(f'<h{level} id="{esc(section["id"])}">{title}</h{level}>')
            sections_html.append(render_blocks(section.get("blocks", []), input_dir))
        articles.append(
            f'<article class="chapter" id="{esc(chapter["id"])}">'
            f'<div class="chapter__number">{rich(chapter, "number", f"CHAPTER {ci:02d}")}</div>'
            f'<h1 class="chapter__title">{rich(chapter, "title")}</h1>'
            f'<p class="chapter__intro">{rich(chapter, "intro")}</p>'
            f'{render_blocks(chapter.get("blocks", []), input_dir)}'
            f'{"".join(sections_html)}</article>'
        )
    return "<main>" + "\n".join(articles) + "</main>"


def build(data: dict[str, Any], input_path: Path) -> str:
    meta = data.get("meta", {})
    if not isinstance(meta, dict):
        fail("'meta' must be an object")
    chapters = normalize_chapters(data)
    body = "\n".join([
        render_cover(meta, input_path.parent),
        render_toc(meta, chapters),
        render_chapters(chapters, input_path.parent),
    ])
    shell = SHELL_PATH.read_text(encoding="utf-8")
    css = CSS_PATH.read_text(encoding="utf-8")
    replacements = {
        "{{LANG}}": esc(meta.get("lang", "ar")),
        "{{DIR}}": esc(meta.get("dir", "rtl")),
        "{{HTML_TITLE}}": esc(meta.get("html_title", meta.get("title", "System User Manual"))),
        "{{CSS}}": css,
        "{{BODY}}": body,
    }
    for key, value in replacements.items():
        shell = shell.replace(key, value)
    return shell


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path, help="Manual content JSON")
    parser.add_argument("output_html", type=Path, help="Self-contained output HTML")
    args = parser.parse_args()
    data = load_json(args.input_json)
    output = build(data, args.input_json.resolve())
    args.output_html.parent.mkdir(parents=True, exist_ok=True)
    args.output_html.write_text(output, encoding="utf-8")
    print(f"Wrote {args.output_html} ({args.output_html.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
