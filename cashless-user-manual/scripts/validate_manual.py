#!/usr/bin/env python3
"""Validate structural and style invariants of a generated Cashless manual."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = SKILL_ROOT / "assets" / "master.css"
EXPECTED_CSS_SHA256 = "b2e3981605875fa29a79a446e3b779958237ced168ea8675b4a1992894d7e36b"


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.classes: list[str] = []
        self.images: list[dict[str, str]] = []
        self.html_attrs: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.html_attrs = data
        if "id" in data:
            self.ids.append(data["id"])
        if "class" in data:
            self.classes.extend(data["class"].split())
        if tag == "img":
            self.images.append(data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_html", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable report")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    html_text = args.input_html.read_text(encoding="utf-8")
    inspector = Inspector()
    inspector.feed(html_text)

    css_hash = hashlib.sha256(CSS_PATH.read_bytes()).hexdigest()
    if css_hash != EXPECTED_CSS_SHA256:
        errors.append("assets/master.css differs from the locked reference style")
    if inspector.html_attrs.get("dir") != "rtl":
        errors.append("<html> must use dir=rtl")
    if inspector.html_attrs.get("lang") != "ar":
        warnings.append("<html> lang is not ar")
    duplicates = sorted({x for x in inspector.ids if inspector.ids.count(x) > 1})
    if duplicates:
        errors.append("Duplicate ids: " + ", ".join(duplicates))
    required_classes = {"cover", "toc", "chapter", "chapter__title", "chapter__intro"}
    missing = sorted(required_classes - set(inspector.classes))
    if missing:
        errors.append("Missing required classes: " + ", ".join(missing))
    for n, image in enumerate(inspector.images, 1):
        src = image.get("src", "")
        if not src.startswith("data:image/"):
            warnings.append(f"Image {n} is not embedded as a data URI")
        if not image.get("alt"):
            warnings.append(f"Image {n} has empty alt text")
    if "{{" in html_text or "}}" in html_text:
        errors.append("Unresolved template placeholder found")
    if "IBM Plex Sans Arabic" not in html_text or "Inter" not in html_text:
        errors.append("Required font families are missing")
    if "#0D274D" not in html_text or "#F8722B" not in html_text:
        errors.append("Locked brand colors are missing")
    if not re.search(r'<figure class="screenshot">', html_text):
        warnings.append("No screenshot figures found")

    report = {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": {
            "ids": len(inspector.ids),
            "images": len(inspector.images),
            "chapters": inspector.classes.count("chapter"),
            "tables": inspector.classes.count("data-table"),
            "callouts": inspector.classes.count("callout"),
        },
        "css_sha256": css_hash,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("VALID" if report["valid"] else "INVALID")
        for message in errors:
            print(f"ERROR: {message}")
        for message in warnings:
            print(f"WARNING: {message}")
        print("COUNTS:", report["counts"])
    raise SystemExit(0 if report["valid"] else 1)


if __name__ == "__main__":
    main()
