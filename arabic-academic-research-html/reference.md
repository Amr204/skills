# Reference — CSS & Components

## Core glass card

```css
.glass-card {
  background: var(--color-glass-bg);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid var(--color-glass-border);
  border-radius: var(--radius-card);
  box-shadow: var(--shadow-soft);
  padding: 2rem;
  margin-bottom: var(--spacing-section);
}
```

## Section header pattern

```html
<div class="section-header">
  <div class="section-icon" aria-hidden="true"><!-- 24x24 SVG --></div>
  <h2 class="section-title">عنوان القسم</h2>
</div>
```

## Student author signature

```css
.case-student-author {
  display: block;
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(212, 160, 23, 0.18);
  text-align: left;
  font-size: 0.875rem;
  font-weight: 500;
  color: #a68b3c;
}
```

## Infographic wrapper

```css
.infographic-wrap {
  background: var(--color-glass-bg);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid var(--color-glass-border);
  border-radius: var(--radius-card);
  padding: 1.5rem;
  margin: 1.75rem 0;
}
.infographic-title {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--color-accent-dark);
  border-bottom: 1px solid rgba(212,160,23,0.2);
  padding-bottom: 0.75rem;
  margin-bottom: 1.25rem;
}
```

## Timeline (RTL)

```css
.timeline {
  position: relative;
  padding-right: 2rem;
}
.timeline::before {
  content: '';
  position: absolute;
  right: 0.55rem;
  top: 0.5rem;
  bottom: 0.5rem;
  width: 2px;
  background: linear-gradient(to bottom, var(--color-accent), rgba(212,160,23,0.2));
}
.timeline-dot {
  position: absolute;
  right: -2rem;
  top: 0.25rem;
  width: 1.15rem;
  height: 1.15rem;
  border-radius: 9999px;
  background: var(--color-accent);
  border: 3px solid #fff;
}
```

## SVG flow diagram tips

- `viewBox` for scalability; `font-family` inherited from page
- RTL: arrows point right-to-left (`marker-end` on lines)
- Colors: `#D4A017`, `#b8890f`, `#1d1d1f`, `#424245`
- `role="img"` + `aria-label` in Arabic

## Print overrides (essential)

```css
@media print {
  .navbar, .btn-pdf, .back-to-top, .print-tip-overlay, .print-header {
    display: none !important;
  }
  .glass-card, .case-card, .infographic-wrap {
    background: #fff !important;
    backdrop-filter: none !important;
    border: 1px solid #ddd !important;
    box-shadow: none !important;
    break-inside: avoid;
  }
  .hero-card { break-after: page; }
  #toc { break-after: page; }
  .section-card { break-before: page; }
  .section-card:first-of-type { break-before: auto; }
  .case-studies-grid { display: block !important; }
}
```

## PDF button JS

```javascript
document.getElementById('btnPdf').addEventListener('click', function() {
  document.getElementById('printTip').classList.add('visible');
});
document.getElementById('btnPrintConfirm').addEventListener('click', function() {
  document.getElementById('printTip').classList.remove('visible');
  if (typeof openAllAccordions === 'function') openAllAccordions();
  window.print();
});
window.addEventListener('beforeprint', function() {
  if (typeof openAllAccordions === 'function') openAllAccordions();
});
```

## Hero meta (group project)

```html
<div class="hero-meta">
  <div class="hero-meta-item"><strong>المادة:</strong> …</div>
  <div class="hero-meta-item"><strong>إشراف:</strong> الدكتور …</div>
  <div class="hero-meta-item">
    <strong>إعداد:</strong><br>
    اسم ١<br>اسم ٢<br>…
  </div>
  <div class="hero-meta-item"><strong>التاريخ:</strong> …</div>
</div>
```

## APA reference list

```html
<ol class="references-list">
  <li>Author, A. A. (Year). <em>Title</em>. Publisher.</li>
</ol>
```

Use `direction: ltr; unicode-bidi: embed` on reference `<li>` items for mixed Latin/Arabic.
