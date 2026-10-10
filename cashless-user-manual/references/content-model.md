# Manual Content Model

The deterministic generator consumes UTF-8 JSON and produces a self-contained HTML file. Start from `examples/manual.example.json`.

## Top-level shape

```json
{
  "meta": { "...": "..." },
  "chapters": [
    {
      "id": "ch1",
      "number": "CHAPTER 01",
      "title": "مقدمة سريعة",
      "intro": "...",
      "toc_page": "3",
      "blocks": [],
      "sections": []
    }
  ]
}
```

## `meta`

Recommended fields:

| Field | Meaning |
|---|---|
| `lang` / `dir` | Usually `ar` / `rtl` |
| `html_title` | Browser/PDF metadata title |
| `brand_prefix` / `brand_highlight` | Brand text before and inside the orange span |
| `logo` | PNG/JPEG/WebP path; relative paths resolve from the JSON file, then skill root |
| `eyebrow` | Usually `USER MANUAL` |
| `title` | Main English cover title |
| `subtitle` | Arabic manual scope |
| `derived` | One-sentence source/scope note |
| `prepared_for` | Audience or client |
| `edition` | Edition and year |
| `toc_title` / `toc_subtitle` | TOC labels |

Plain string values are HTML-escaped. For controlled inline formatting, provide a sibling key ending in `_html`, for example `subtitle_html` or `text_html`.

## Chapters and sections

- `id` values must be unique.
- A chapter may have introductory `blocks` before its sections.
- Section `level` must be 2, 3, or 4.
- Use stable numbering in the title: `3.4.2 تبويب الملف`.
- `toc_page` is updated after PDF render using `scripts/sync_toc_pages.py`.
- Keep each h2 section focused on one task or screen.

## Block types

### Paragraph

```json
{ "type": "p", "text": "نص عادي" }
```

Controlled formatting:

```json
{
  "type": "p",
  "text_html": "اضغط <strong>حفظ</strong> ثم تحقق من ظهور رسالة النجاح."
}
```

### Bullet list

```json
{
  "type": "bullets",
  "items": ["العنصر الأول", "العنصر الثاني"],
  "navy": false
}
```

Use bullets for properties, prerequisites, or alternatives. Use steps for ordered actions.

### Numbered steps

```json
{
  "type": "steps",
  "items": [
    { "title": "فتح الصفحة", "body": "اختر إدارة الممثلين من القائمة." },
    { "title": "التحقق", "body": "تأكد من ظهور الجدول." }
  ]
}
```

Each step should state the action, target, and expected evidence. Avoid combining multiple screens in one step.

### Table

```json
{
  "type": "table",
  "caption": "الجدول 1: الحقول الأساسية",
  "headers": ["الحقل", "الوصف", "إلزامي"],
  "rows": [
    ["المعرف العام", "معرف فريد.", { "html": "<span class=\"req-yes\">نعم</span>" }]
  ]
}
```

A cell may be a plain string or `{ "html": "..." }`. Keep column count consistent.

### Callout

```json
{
  "type": "callout",
  "variant": "warning",
  "icon": "!",
  "label": "تحذير",
  "paragraphs": ["هذا الإجراء يؤثر على وصول المستخدم."]
}
```

Allowed variants: `note`, `warning`, `tip`, `important`.

### Screenshot

```json
{
  "type": "screenshot",
  "src": "screenshots/actors-page.png",
  "alt": "صفحة الممثلين",
  "number": "شكل 1",
  "caption": "صفحة الممثلين — تعرض أدوات البحث وجدول السجلات."
}
```

The generator embeds the image as a data URI. Use PNG for UI captures. Captions must identify the screen and explain what the reader should notice.

### Info card

```json
{
  "type": "info_card",
  "title": "معلومات السجل",
  "items": [
    { "label": "الحالة", "value": "نشط" },
    { "label": "النوع", "value": "فرد" }
  ]
}
```

### Workflow

```json
{
  "type": "workflow",
  "steps": [
    "فتح الصفحة",
    { "text": "مراجعة البيانات", "active": true },
    "الحفظ"
  ]
}
```

Use one active orange step at most.

### Raw HTML

```json
{ "type": "raw_html", "html": "<span class=\"status-pill status--active\">نشط</span>" }
```

Use only for existing locked classes that the structured blocks cannot express. Do not add inline style attributes or new CSS.

## Supported inline classes

- `code-ref`
- `badge badge--correct|wrong|navy|orange|soft`
- `status-pill status--active|pending|locked|under-approval|suspended`
- `req-yes`, `req-no`

## Content quality rules

- Use actual system terminology from screenshots, requirements, UI source, or user-provided documentation.
- Never invent button labels, permissions, validation messages, field requirements, or irreversible effects.
- If an operational fact cannot be verified, write `[TBD — يحتاج تأكيد]` and list it in the handoff.
- Explain prerequisites before steps, result after steps, and recovery/rollback where relevant.
- Keep figure and table numbering continuous across chapters.
- Keep Arabic punctuation and spelling consistent; preserve English product/field identifiers.
