#!/usr/bin/env python3
"""Render a self-contained manual HTML file to A4 PDF.

Preferred engine: Playwright driving system Chromium. It loads the HTML with
page.set_content(), avoiding file:// policy failures. Fallback: WeasyPrint.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def render_playwright(input_html: Path, output_pdf: Path, browser_path: str, timeout_ms: int, offline: bool) -> None:
    from playwright.sync_api import sync_playwright

    text = input_html.read_text(encoding="utf-8")
    args = ["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=browser_path, args=args)
        context = browser.new_context(offline=offline)
        page = context.new_page()
        page.set_content(text, wait_until="domcontentloaded", timeout=timeout_ms)
        if not offline:
            try:
                page.evaluate("() => Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 8000))])")
            except Exception:
                pass
        page.emulate_media(media="print")
        page.pdf(
            path=str(output_pdf),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=False,
        )
        browser.close()


def render_weasyprint(input_html: Path, output_pdf: Path) -> None:
    from weasyprint import HTML

    HTML(filename=str(input_html)).write_pdf(str(output_pdf))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_html", type=Path)
    parser.add_argument("output_pdf", type=Path)
    parser.add_argument("--timeout", type=int, default=120, help="Navigation timeout in seconds")
    parser.add_argument("--offline", action="store_true", help="Disable network; font fallback may differ from the reference")
    parser.add_argument("--engine", choices=("auto", "playwright", "weasyprint"), default="auto")
    args = parser.parse_args()

    input_html = args.input_html.resolve()
    output_pdf = args.output_pdf.resolve()
    if not input_html.exists():
        print(f"ERROR: HTML not found: {input_html}", file=sys.stderr)
        raise SystemExit(2)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    browser = next((shutil.which(x) for x in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable") if shutil.which(x)), None)
    errors: list[str] = []

    if args.engine in ("auto", "playwright"):
        if not browser:
            errors.append("Chromium/Chrome not found")
        else:
            try:
                render_playwright(input_html, output_pdf, browser, args.timeout * 1000, args.offline)
            except Exception as exc:
                errors.append(f"Playwright render failed: {exc}")
            else:
                print(f"Wrote {output_pdf} ({output_pdf.stat().st_size:,} bytes) using Playwright/Chromium")
                return
        if args.engine == "playwright":
            print("ERROR: " + "; ".join(errors), file=sys.stderr)
            raise SystemExit(3)

    if args.engine in ("auto", "weasyprint"):
        try:
            render_weasyprint(input_html, output_pdf)
        except Exception as exc:
            errors.append(f"WeasyPrint render failed: {exc}")
        else:
            print(f"Wrote {output_pdf} ({output_pdf.stat().st_size:,} bytes) using WeasyPrint")
            return

    print("ERROR: " + "; ".join(errors), file=sys.stderr)
    raise SystemExit(4)


if __name__ == "__main__":
    main()
