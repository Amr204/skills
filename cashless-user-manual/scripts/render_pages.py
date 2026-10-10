#!/usr/bin/env python3
"""Render every PDF page to PNG for visual QA."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz  # PyMuPDF


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=150)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(args.input_pdf)
    zoom = args.dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for index, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        out = args.output_dir / f"page-{index:03d}.png"
        pix.save(out)
        print(out)
    print(f"Rendered {doc.page_count} page(s)")


if __name__ == "__main__":
    main()
