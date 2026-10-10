---
name: arabic-academic-research-html
description: >-
  Builds a single self-contained Arabic academic research HTML page with Liquid
  Glass design, SVG infographics, student case studies, and print-ready PDF
  export. Use when the user asks for بحث أكاديمي HTML, تكليف جامعي, academic
  report as one HTML file, Liquid Glass Arabic document, or recreating this
  research-paper web format.
---

# Arabic Academic Research HTML (Liquid Glass)

Produce **one `.html` file** only: embedded CSS + JS, no external libraries except Google Fonts (`IBM Plex Sans Arabic`).

Reference implementation: `بحث-الحملة-الإعلانية.html` in the user's projects. For CSS/component details, read [reference.md](reference.md). For input templates, read [examples.md](examples.md).

## Output rules

- Real Arabic academic prose (5000–7000 words for full papers). No Lorem Ipsum.
- No fabricated statistics or unverified campaign metrics.
- `html lang="ar" dir="rtl"` on root.
- Do not create extra files unless the user asks.

## Document structure (in order)

1. **Sticky glass navbar** — short title + `تحميل PDF` button (`window.print()`).
2. **Hero card** — badge, title, المادة, إشراف (professor), إعداد (student(s)), التاريخ.
3. **TOC card** — anchor links with `scroll-behavior: smooth`.
4. **Section cards** (`glass-card section-card`) — each major chapter with SVG icon in `.section-header`.
5. **Case studies** — one full-width card per student submission + timeline + summary table.
6. **Conclusion + References** (APA, 5–6 sources).
7. **Back-to-top** circular glass button.

## Design tokens (`:root`)

| Token | Value |
|-------|-------|
| Background | `#FFFFFF` (no gradients, no dark mode) |
| Text | `#1d1d1f` |
| Accent | `#D4A017` |
| Glass bg | `rgba(255,255,255,0.65)` + `backdrop-filter: blur(20px) saturate(180%)` |
| Radius | `1.5rem` cards, `9999px` pills |
| Font | `"IBM Plex Sans Arabic", "Segoe UI", "Tahoma", sans-serif` |

Corners: only `rounded-2xl` (~1.5rem) and `rounded-full`. No sharp corners.

## Required infographics (embed where content supports them)

Use HTML + CSS + inline SVG only. Distribute naturally; do not decorate without purpose.

| Type | Class / pattern | Use for |
|------|-----------------|--------|
| Stat cards | `.stat-cards` | Research structure overview |
| Process steps | `.process-steps` | Campaign build phases |
| Flow diagram | `.flow-svg-wrap` + SVG | Impact paths, AIDA-like flows |
| Timeline | `.timeline` | Case study chronology |
| Comparison cards | `.comparison-cards` | Target vs general public |
| Circular chart | `.circular-infographic` | 3 theories / 3 impact dimensions |
| Feature grid | `.feature-infographic` | Success factors |
| Visual summary | `.visual-summary` | Conclusion takeaways |
| Data tables | `.data-table` | Criteria, comparisons |

Wrap each infographic in `.infographic-wrap` with `.infographic-title`.

## Student case studies (group assignments)

When multiple students each submit a campaign analysis:

```html
<article class="case-card">
  <div class="case-card-header">...</div>
  <div class="case-card-body case-student-content">
    <!-- student's original text: نبذة، الرأي، etc. -->
    <span class="case-student-author">اسم الطالبة</span>
  </div>
</article>
```

- `.case-student-author`: muted gold `#a68b3c`, left-aligned, border-top separator.
- Use `.case-studies-grid` as **single column** (`flex-direction: column`) for long essays.
- Preserve each student's wording; do not invent data.

## Print / PDF (`@media print`)

**Must implement:**

- Hide: `.navbar`, `.btn-pdf`, `.back-to-top`, `.print-tip-overlay`, `.print-header`
- Glass cards → solid white, `border: 1px solid #ddd`, no backdrop-filter
- `@page { size: A4; margin: 2cm 2cm 2.6cm 2cm; }`
- `page-break-before: always` on `.section-card` (except first)
- `break-inside: avoid` on cards, tables, infographics
- **Page numbers only** in fixed footer:

```html
<footer class="print-chrome print-footer" aria-hidden="true">
  <span class="print-footer-page">صفحة </span>
</footer>
```

```css
@media print {
  .print-footer {
    position: fixed; bottom: 0; left: 0; right: 0;
    display: flex !important; justify-content: center;
  }
  .print-footer-page::after {
    content: counter(page) " / " counter(pages);
  }
}
```

**Do NOT** use a fixed print header (it repeats on every page and overlaps content).

**Print tip modal** before `window.print()`:
1. User opens «المزيد من الإعدادات»
2. Disables «الرؤوس والتذييلات» (browser URL/title)
3. Saves as PDF

Call `openAllAccordions()` on `beforeprint` if accordions exist.

## Build workflow

```
Progress:
- [ ] 1. Parse user input: title, course, professor, students, sections, case studies
- [ ] 2. Scaffold HTML head + :root + navbar + print chrome
- [ ] 3. Write hero + TOC
- [ ] 4. Write academic sections (intro → theory → analysis → factors)
- [ ] 5. Add 2–4 infographics per major section (SVG)
- [ ] 6. Insert student case cards + timeline + summary table
- [ ] 7. Conclusion visual summary + APA references
- [ ] 8. Print CSS + PDF button JS + print tip
- [ ] 9. Verify RTL, contrast ≥4.5:1, responsive mobile/tablet/desktop
```

If the file exceeds token limits, build in phases: skeleton → sections → infographics → case studies.

## Accessibility

- Semantic HTML5 (`header`, `nav`, `main`, `section`, `article`)
- `aria-label` on infographics and tables
- Visible `:focus-visible` outlines (accent color)
- Keyboard: TOC links, accordion triggers, print modal buttons

## What NOT to do

- No React/Vue/Bootstrap/Tailwind CDN
- No external images (SVG vectors only)
- No manual page numbers in body HTML (use CSS counter in print footer)
- No browser header duplication (hidden via user print settings + no fixed print header)
- No deleting user-provided case study text when updating design

## Additional resources

- Component CSS snippets: [reference.md](reference.md)
- User prompt templates: [examples.md](examples.md)
