# Locked Visual Specification

## Authority and fidelity target

The authoritative visual source is `references/reference-manual.html`. The reusable stylesheet is `assets/master.css`.

- Locked stylesheet SHA-256: `b2e3981605875fa29a79a446e3b779958237ced168ea8675b4a1992894d7e36b`
- Treat `assets/master.css` as immutable unless the user explicitly requests a redesign.
- Build new manuals by changing content and images, not by rewriting the design from memory.
- A result is “exact style” only when the locked CSS, component class names, font families, A4 print rules, and cover structure remain unchanged.

## Design tokens

| Token | Exact value | Use |
|---|---:|---|
| Navy | `#0D274D` | Cover, table headers, dark callouts, workflow steps |
| Orange | `#F8722B` | Brand accent, chapter label, step circles, active workflow step |
| Ink | `#000000` | Headings, strong text, table body text |
| Body | `#808191` | Paragraphs, captions, secondary copy |
| Body soft | `#595959` | Muted labels and inactive values |
| Success | `#28A745` | Positive/required status |
| Danger | `#DC3545` | Warnings, invalid/locked status |
| Border | `#E5E7EB` | Tables, images, cards |
| Soft background | `#F8F9FA` | Browser canvas and subtle surfaces |

Do not introduce a new brand color, gradient, decorative pattern, or shadow system.

## Typography

- Arabic/body: `IBM Plex Sans Arabic`, weights 300/400/500/600/700.
- English/cover: `Inter`, weights 300/400/500/600/700/800.
- Monospace: `SFMono-Regular`, `Consolas`, `Courier New`.
- Default HTML size: 16px.
- Printed body size: 11pt.
- Body line height: 1.55; paragraphs and lists generally 1.7.
- Heading line height: 1.30.

Exact typography requires `IBM Plex Sans Arabic` and `Inter` to be available through the preserved Google Fonts links or installed in the rendering environment. Do not bundle or redistribute font files. When rendering offline, report that fallback typography may differ.

## Direction and language

- Root HTML: `lang="ar" dir="rtl"` for Arabic manuals.
- Body: `direction: rtl; text-align: right`.
- English cover content uses the English font but remains positioned by the RTL layout inherited from the reference.
- Inline code must be `direction: ltr; display: inline-block`.
- Preserve product names, API identifiers, commands, and field keys exactly; do not Arabize identifiers.

## A4 and print geometry

- Page size: A4.
- Print margins: top 18mm, right 14mm, bottom 16mm, left 14mm.
- Screen content width: max 210mm, centered, 24px gap, subtle shadow.
- Cover and TOC always end with a page break.
- Every chapter starts on a new page.
- Avoid page breaks inside screenshots, callouts, tables, step items, info cards, and workflows.
- Avoid page breaks immediately after h2/h3/h4 and chapter headers.

## Cover

Required structure and classes:

```html
<section class="cover">
  <div class="cover__brand-row">...</div>
  <div class="cover__center">...</div>
  <div class="cover__footer">...</div>
</section>
```

Visual rules:

- Navy background.
- Orange vertical bar on the right, exactly 8mm wide.
- Cover padding on screen: 40mm 30mm 30mm.
- Print cover padding: 60mm 24mm 24mm.
- English title: 56px/700, line-height 1.1.
- Eyebrow: orange uppercase, 11px/600, 2px letter spacing.
- Footer separated by a low-opacity white rule.

## Table of contents

- White A4 page.
- Title: 32px/700 black.
- Subtitle: 14px body color with 2px orange underline.
- Chapter rows: 15px/700 with dashed border.
- Section rows: 12px; deeper entries 11.5px and 48px right indentation.
- Use dotted leaders and explicit page numbers.
- Page numbers must be synchronized from the rendered PDF before final delivery.

## Chapter headers

- `.chapter__number`: orange pill, white uppercase 12px/700.
- `.chapter__title`: 32px/700 black.
- `.chapter__intro`: 16px body color, 4px orange right rule, 1.7 line height.
- h2: 22px/700 black, subtle navy underline.
- h3: 18px/700 black.
- h4: 15px/600 navy.

## Component rules

### Numbered steps

Use `.steps`, `.step__num`, and `.step__body`. Step numbers are 32px orange circles. Each step must contain one action and a verifiable result.

### Tables

Use `.data-table` only. Header is navy with white text. Alternate rows use the existing 5% navy fill. Keep a table together when practical; split a large table by logical group instead of shrinking text.

### Callouts

Only these variants are allowed:

- `callout--note`: navy background, orange label.
- `callout--warning`: pale danger background and 4px danger right rule.
- `callout--tip`: pale orange background and 4px orange right rule.
- `callout--important`: navy background and 4px orange right rule.

Do not use a callout as ordinary decoration. Use it only for risk, prerequisite, exception, irreversible action, or operational guidance.

### Screenshots

- Use `<figure class="screenshot">`.
- Image width 100%, 1px border, 4px radius.
- Caption uses `.fig__num` followed by a factual sentence.
- Number figures sequentially across the whole manual: `شكل 1`, `شكل 2`, etc.
- Crop only irrelevant browser/desktop chrome. Never alter functional UI content.
- Redact secrets and personal data before embedding.

### Info cards and workflows

- Info cards use `.info-card`, a navy 4px right edge, and a two-column grid.
- Workflows use navy steps and one orange active/current step.
- Workflow arrows are `←` in RTL order.

## Forbidden drift

Do not:

- replace the fonts with a different design choice;
- change color hex values;
- change the orange right-side cover bar;
- use rounded “modern card” styling not present in the reference;
- add icons from a different visual system;
- use generated/fabricated UI screenshots;
- reduce text below the specified sizes to force content onto a page;
- move the manual to DOCX/PPTX unless the user explicitly asks for those formats.
