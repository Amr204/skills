# Output Evaluation Rubric

Score each item 0 or 1 unless stated otherwise. A production pass requires all critical items and at least 18/20 total.

## Critical

1. Uses `assets/master.css` unchanged; hash matches the lock.
2. Produces `lang=ar`, `dir=rtl` for an Arabic manual.
3. Uses the exact navy `#0D274D` and orange `#F8722B` design.
4. Includes cover, TOC, and at least one chapter with the locked class structure.
5. Does not invent system behavior, labels, permissions, or screenshots.
6. Removes/redacts credentials, tokens, and personal data.
7. Generated HTML passes `scripts/validate_manual.py` without errors.
8. PDF is A4 with backgrounds and no browser header/footer when PDF is requested.
9. Every PDF page is visually inspected after rendering to PNG.
10. No clipping, overlap, broken Arabic glyphs, or unreadably split components.

## Quality

11. The skill triggers for user-manual requests and does not trigger for unrelated reports/docs.
12. Steps are atomic, ordered, and state expected results.
13. Risks and prerequisites appear before consequential actions.
14. Screenshots have sequential figure numbers, alt text, and useful captions.
15. Tables have captions, consistent columns, and readable text.
16. TOC page numbers match final PDF pages.
17. Chapter and section numbering is consistent.
18. Fonts are IBM Plex Sans Arabic/Inter or font fallback is explicitly disclosed.
19. Final filenames are clear and deliverables exclude temporary files.
20. Editable source JSON is delivered when ongoing maintenance is expected.
