# Production Workflow and QA

## 1. Intake and evidence

Collect or identify:

- system name and manual scope;
- intended audience and role/permission assumptions;
- environment/version/build date;
- ordered task list or source requirements;
- screenshots for each screen/state;
- exact field labels, button labels, status names, and expected results;
- known risks, approval gates, rollback/recovery steps;
- cover metadata: client/audience, edition, date, logo.

Do not block when a harmless cover field is missing; use a clear placeholder and record it. Do block or mark TBD when a missing fact would make operating instructions unsafe or incorrect.

## 2. Source analysis

For every requested workflow:

1. Identify entry point and required role.
2. Identify prerequisites and initial state.
3. Extract the exact navigation path.
4. Split the operation into atomic actions.
5. State the expected result after each critical action.
6. Capture exception paths and validation errors.
7. Document rollback/recovery for destructive or state-changing actions.
8. Map each screenshot to the step it proves.

For system documentation, factual correctness outranks completeness. Omit unverifiable detail rather than fabricate it.

## 3. Authoring

Copy the example JSON to a working directory:

```bash
cp examples/manual.example.json work/manual.json
```

Replace all example content. Keep the locked component vocabulary and CSS classes. Build:

```bash
python scripts/build_manual.py work/manual.json output/system-user-manual.html
```

Validate structure and style lock:

```bash
python scripts/validate_manual.py output/system-user-manual.html --json
```

Resolve every error. Review warnings; a warning is acceptable only with an explicit reason.

## 4. PDF rendering

Preferred:

```bash
python scripts/render_manual.py \
  output/system-user-manual.html \
  output/system-user-manual.pdf
```

Use `--offline` only when network access is unavailable. An offline render may substitute the Arabic font and therefore is not typography-identical to the reference.

The PDF must be A4 and include backgrounds. Do not add browser headers/footers.

## 5. Synchronize TOC page numbers

First render, then update page numbers:

```bash
python scripts/sync_toc_pages.py \
  work/manual.json \
  output/system-user-manual.pdf \
  work/manual.synced.json

python scripts/build_manual.py \
  work/manual.synced.json \
  output/system-user-manual.html

python scripts/render_manual.py \
  output/system-user-manual.html \
  output/system-user-manual.pdf
```

Run synchronization again if pagination changed. Stop after page numbers remain stable. Manually verify headings that the script reports as missing.

## 6. Visual QA

Render all PDF pages:

```bash
python scripts/render_pages.py \
  output/system-user-manual.pdf \
  output/rendered-pages \
  --dpi 150
```

Inspect every page, not only the first and last.

### Mandatory visual checks

- No clipped Arabic glyphs, black squares, missing characters, or font fallback surprises.
- No text/image overlap.
- No screenshot, callout, card, or step split in an unreadable way.
- No orphan heading at the bottom of a page.
- No blank page except an intentional section separator.
- Table headings remain with their tables.
- Captions remain with their screenshots.
- Screenshot text is legible at 100% PDF zoom.
- Cover, TOC, and chapters have the same proportions as the reference.
- Orange and navy colors match the locked values.
- Figure/table numbering is continuous.
- TOC links and page numbers are correct.

### Content checks

- Navigation labels match the UI exactly.
- Steps are executable in order.
- Roles and permissions are explicit where they matter.
- Destructive actions include warning and recovery guidance.
- No credentials, tokens, personal information, or production secrets are visible.
- No fabricated screenshot or undocumented behavior appears.

## 7. Screenshot hygiene

- Prefer native-resolution PNG captures.
- Keep browser zoom and OS scaling consistent across the set.
- Crop only irrelevant chrome; preserve context needed to locate controls.
- Redact with irreversible raster redaction before embedding.
- Do not blur merely with CSS; the source pixels must be removed or covered in the image itself.
- Do not sharpen or upscale so aggressively that UI text changes shape.
- Never generate a fake UI screenshot to fill a gap.

## 8. Failure handling and rollback

- Keep the source JSON, generated HTML, PDF, and rendered-page QA output in separate directories.
- Never overwrite the only known-good manual. Use versioned filenames or source control.
- If a style regression appears, restore `assets/master.css` and re-run validation.
- If pagination regresses, revert the last content/layout change, then re-render and compare.
- If fonts differ, rerender in an environment with IBM Plex Sans Arabic and Inter available.
- If a screenshot is wrong, replace the source PNG and rebuild; do not patch the embedded base64 manually.

## 9. Delivery contract

Deliver:

1. the final self-contained `.html`;
2. the final `.pdf` when requested;
3. the editable content `.json` when future maintenance is expected;
4. a concise list of unresolved TBDs or assumptions, if any.

Recommended filenames:

- `<system>-user-manual-ar.html`
- `<system>-user-manual-ar.pdf`
- `<system>-user-manual-ar.source.json`

Remove temporary render folders from the user-facing deliverables unless the user requests QA evidence.
