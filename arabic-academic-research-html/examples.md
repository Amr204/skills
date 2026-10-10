# Examples — User Prompts

## Full paper (like this project)

```
أنشئ ملف HTML واحد لبحث أكاديمي عربي بصيغة Liquid Glass.

العنوان: [عنوان البحث]
المادة: [اسم المادة]
الإشراف: [اسم الدكتور]
الطلاب: [قائمة الأسماء]
التاريخ: [التاريخ]

الأقسام: مقدمة، إطار نظري، أبعاد التأثير، العوامل المؤثرة،
أمثلة من الواقع، خاتمة، مراجع APA.

دراسات الحالة (نص كل طالبة كما هو):
1. [الاسم]: [الحملة + النص الكامل]
2. ...

متطلبات: IBM Plex Sans Arabic، RTL، إنفوجرافيك SVG،
طباعة PDF، ترقيم صفحات في الأسفل فقط.
```

## Update student cases only

```
حدّث قسم دراسات الحالة فقط في [file.html]:
- استبدل الحملات بـ [قائمة]
- ضع اسم كل طالبة تحت بحثها بلون خافت
- لا تعدّل باقي الملف
```

## Design-only refresh

```
أضف إنفوجرافيك احترافي (flow, timeline, stat cards, circular SVG)
داخل [file.html] دون حذف المحتوى الأكاديمي.
```

## Expected file output

- Path: user-chosen, e.g. `d:\Projects\تكليف\بحث-[topic].html`
- Single file, typically 2000–2500 lines for full papers with infographics
- Open in browser → «تحميل PDF» → disable browser headers → Save as PDF
