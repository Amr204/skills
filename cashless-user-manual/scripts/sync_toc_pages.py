#!/usr/bin/env python3
"""Update toc_page fields in manual JSON from heading locations in a rendered PDF."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("ـ", "")
    value = re.sub(r"[\u064b-\u065f\u0670]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip().lower()


def visible_title(obj: dict[str, Any]) -> str:
    # HTML-rich titles are intentionally unsupported for page matching.
    return str(obj.get("title", ""))


def locate(title: str, page_texts: list[str], start_page: int = 3) -> int | None:
    target = normalize(title)
    if not target:
        return None
    target_tokens = [token for token in target.split() if token]
    for page_number, text in enumerate(page_texts, 1):
        if page_number < start_page:
            continue
        if target in text:
            return page_number
        # Arabic text extraction may reverse visual word order. Match all
        # significant tokens regardless of order while preserving numbers.
        page_tokens = set(text.split())
        if target_tokens and all(token in page_tokens for token in target_tokens):
            return page_number
    # Fallback for long titles: match a distinctive token subset.
    significant = [t for t in target_tokens if len(t) >= 4][:4]
    if significant:
        for page_number, text in enumerate(page_texts, 1):
            if page_number >= start_page and all(t in set(text.split()) for t in significant):
                return page_number
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    doc = fitz.open(args.input_pdf)
    page_texts = [normalize(page.get_text("text")) for page in doc]
    missing: list[str] = []

    for chapter in data.get("chapters", []):
        title = visible_title(chapter)
        page = locate(title, page_texts, start_page=3)
        if page is None:
            missing.append(title)
        else:
            chapter["toc_page"] = str(page)
        for section in chapter.get("sections", []):
            title = visible_title(section)
            page = locate(title, page_texts, start_page=3)
            if page is None:
                missing.append(title)
            else:
                section["toc_page"] = str(page)

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output_json}")
    if missing:
        print("WARNING: headings not found:")
        for title in missing:
            print(f"- {title}")


if __name__ == "__main__":
    main()
