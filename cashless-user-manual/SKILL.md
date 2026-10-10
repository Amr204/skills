---
name: cashless-user-manual
description: Use this skill whenever the user asks to create, recreate, update, or export an Arabic RTL system user guide, operating manual, admin manual, دليل استخدام, دليل مستخدم, شرح نظام, or documentation in the exact Cashless/Vertocore visual style. Produce a self-contained HTML manual and, when requested, an A4 PDF using the locked navy/orange template, IBM Plex Sans Arabic/Inter typography, cover, TOC, chapters, numbered steps, tables, callouts, screenshots, captions, and visual QA. Do not use for generic reports, presentations, README files, or unrelated documents.
license: Proprietary. Use only with authorization from the template owner.
compatibility: Requires Python 3.10+. PDF rendering prefers Playwright plus Chromium; WeasyPrint is the fallback. PyMuPDF is used for page rendering and TOC synchronization. Exact typography requires IBM Plex Sans Arabic and Inter through network access or local installation; font files are not bundled.
metadata:
  author: mark
  version: "1.0.0"
  template: "Cashless Arabic User Manual Master CSS v2"
---

# Cashless User Manual

أنشئ أدلة استخدام عربية RTL مطابقة بصريًا للقالب المرجعي، مع إبقاء التصميم ثابتًا وجعل المحتوى والصور فقط قابلين للتغيير.

## عقد الإخراج

عند تفعيل المهارة:

1. أنشئ دليلًا ذاتي الاحتواء بصيغة HTML باستخدام `assets/master.css` دون تعديله.
2. أنشئ PDF بحجم A4 عندما يطلب المستخدم PDF أو دليلًا نهائيًا قابلًا للطباعة.
3. استخدم العربية وRTL افتراضيًا، مع إبقاء أسماء المنتجات والحقول التقنية كما تظهر في النظام.
4. سلّم ملف JSON قابلًا للصيانة عندما يتوقع المستخدم تحديث الدليل مستقبلًا.
5. لا تدّعِ التطابق الحرفي قبل التحقق البصري من الصفحات النهائية.

## الملفات التي يجب قراءتها

اقرأ حسب الحاجة وبنمط الإفصاح التدريجي:

- اقرأ `references/style-spec.md` دائمًا قبل التأليف؛ يحتوي على القيم البصرية المقفلة.
- اقرأ `references/content-model.md` قبل إنشاء JSON أو استخدام المكونات.
- اقرأ `references/production-workflow.md` عند إنشاء PDF، معالجة صور، مزامنة الفهرس، أو تنفيذ QA.
- افتح `references/reference-manual.html` فقط عند الحاجة إلى مقارنة مرئية أو فهم سلوك مكوّن غير واضح؛ الملف كبير ولا يلزم تحميله كاملًا في كل تشغيل.
- استخدم `examples/manual.example.json` كنقطة بداية، وليس كمصدر لمحتوى فعلي.

## قواعد غير قابلة للتفاوض

- لا تعِد كتابة CSS من الذاكرة ولا تنشئ قالبًا قريبًا منه.
- لا تغير `assets/master.css` إلا إذا طلب المستخدم إعادة تصميم صريحة.
- لا تغير ألوان `#0D274D` و`#F8722B` أو الخطوط أو مقاسات العناوين أو بنية الغلاف.
- لا تضف inline styles أو مكتبة UI أو framework جديدًا.
- لا تستخدم صور واجهة مولّدة أو تخمّن شكل شاشة غير متاحة.
- لا تخترع أسماء أزرار أو حقول أو صلاحيات أو رسائل نجاح/خطأ أو آثار تشغيلية.
- لا تعرض أسرارًا أو بيانات شخصية أو رموز وصول في الصور أو النصوص.
- لا تصغّر الخط لكسب مساحة؛ قسّم المحتوى منطقيًا بدلًا من ذلك.

## المدخلات المطلوبة

استخرج من طلب المستخدم والملفات المرفقة:

- اسم النظام ونطاق الدليل؛
- الجمهور والأدوار والصلاحيات؛
- الإصدار أو البيئة عند ارتباط الخطوات بها؛
- قائمة الشاشات والعمليات بترتيب منطقي؛
- لقطات الشاشة؛
- مسارات التنقل، الحقول، الأزرار، الحالات، والنتائج المتوقعة؛
- المخاطر، الموافقات، والاسترجاع/الرجوع؛
- بيانات الغلاف والشعار والإصدار.

اسأل فقط عن المعلومات التي تمنع إنتاج تعليمات صحيحة وآمنة. استخدم placeholders واضحة للبيانات الشكلية غير الحرجة. استخدم `[TBD — يحتاج تأكيد]` للحقائق التشغيلية غير المتحققة، ثم اذكرها في التسليم.

## سير التنفيذ

### 1. افحص المصادر

- اقرأ المتطلبات والوثائق المرفقة.
- افحص كل لقطة شاشة بدقة.
- رتّب الشاشات حسب رحلة المستخدم لا حسب ترتيب الملفات.
- أنشئ جدولًا داخليًا يربط: المهمة ← الشاشة ← الدور ← المدخلات ← الإجراء ← النتيجة ← الاستثناء.
- صحح أي افتراض غير مدعوم قبل التأليف.

### 2. صمّم بنية الدليل

استخدم هذا التسلسل ما لم يتطلب النظام غيره:

1. الغلاف.
2. الفهرس.
3. مقدمة ونطاق وصلاحيات.
4. الوصول إلى النظام والتنقل.
5. فصل لكل وحدة رئيسية.
6. قسم لكل شاشة أو مهمة.
7. الإجراءات الحساسة وحالات الخطأ.
8. عملية اعتماد/إغلاق/تسوية شاملة عند وجودها.

اجعل h2 لمهمة أو شاشة رئيسية، h3 لتبويب/حالة فرعية، وh4 لمجموعة حقول أو استثناء محدود.

### 3. أنشئ مصدر JSON

ابدأ بنسخة عمل:

```bash
cp examples/manual.example.json work/manual.json
```

استبدل كل المحتوى التجريبي. استخدم فقط المكونات المحددة في `references/content-model.md`:

- `p`
- `bullets`
- `steps`
- `table`
- `callout`
- `screenshot`
- `info_card`
- `workflow`
- `raw_html` لفئات القالب الموجودة فقط

رقّم الفصول والأقسام والأشكال والجداول باستمرار. اجعل مسارات الصور نسبية لملف JSON عندما يكون ذلك ممكنًا.

### 4. ابنِ HTML

```bash
python scripts/build_manual.py \
  work/manual.json \
  output/system-user-manual-ar.html
```

يبني السكربت ملفًا ذاتي الاحتواء ويضمّن الشعار والصور كـ data URIs، مع CSS الأصلي.

### 5. تحقق من البنية وقفل التصميم

```bash
python scripts/validate_manual.py \
  output/system-user-manual-ar.html \
  --json
```

يجب حل جميع `errors`. لا تتجاهل warning إلا بسبب موثّق. إذا فشل hash الخاص بـ CSS، استعد الملف الأصلي بدل محاولة إصلاحه يدويًا.

### 6. أنشئ PDF عند الحاجة

```bash
python scripts/render_manual.py \
  output/system-user-manual-ar.html \
  output/system-user-manual-ar.pdf
```

- استخدم Playwright/Chromium عندما يتوفر.
- استخدم WeasyPrint كخيار احتياطي فقط، ثم دقق الفروقات البصرية.
- لا تستخدم `--offline` للتسليم النهائي إذا كان التطابق الخطي مطلوبًا وتتوفر الشبكة.
- إذا استُخدم offline، صرّح بأن الخط العربي قد يكون fallback.

### 7. زامن أرقام الفهرس

بعد أول PDF:

```bash
python scripts/sync_toc_pages.py \
  work/manual.json \
  output/system-user-manual-ar.pdf \
  work/manual.synced.json

python scripts/build_manual.py \
  work/manual.synced.json \
  output/system-user-manual-ar.html

python scripts/render_manual.py \
  output/system-user-manual-ar.html \
  output/system-user-manual-ar.pdf
```

كرر حتى تثبت أرقام الصفحات. افحص يدويًا أي عنوان لم يجده السكربت.

### 8. نفّذ QA بصريًا

```bash
python scripts/render_pages.py \
  output/system-user-manual-ar.pdf \
  output/rendered-pages \
  --dpi 150
```

افحص كل صفحة. تحقق من:

- سلامة تشكيل العربية واتجاهها؛
- عدم القص أو التداخل أو المربعات السوداء؛
- بقاء العناوين مع محتواها؛
- عدم فصل الصور عن captions؛
- قراءة النص داخل screenshots عند 100%؛
- عدم تقسيم callouts والخطوات والجداول بشكل غير مقروء؛
- صحة أرقام الفهرس والأشكال والجداول؛
- مطابقة الغلاف والألوان والخطوط والهوامش للمرجع؛
- عدم وجود صفحات فارغة غير مقصودة.

لا تعتبر الدليل منجزًا قبل هذه المراجعة.

## قواعد كتابة المحتوى

- اشرح الهدف والمتطلبات قبل الخطوات.
- اجعل كل خطوة فعلًا واحدًا محددًا، ثم اذكر دليل النجاح.
- استخدم النص الظاهر في الواجهة بين علامتي تنصيص أو بخط عريض.
- استخدم جدولًا لتعريف الحقول والأعمدة والحالات، لا فقرات طويلة.
- استخدم warning لإجراء خطِر، important لبوابة تشغيلية، note لمعلومة سياقية، tip لتحسين التنفيذ.
- ضع rollback أو recovery بعد أي إجراء يغيّر الحالة أو يمنع الوصول.
- استخدم captions تشرح ما يجب ملاحظته، لا captions من نوع “صورة الشاشة”.
- لا تكتب معلومات عامة لا تساعد المستخدم على تنفيذ مهمة.

## التعامل مع الصور

- استخدم PNG للواجهات.
- حافظ على scale موحد بين اللقطات.
- قص العناصر غير المهمة فقط.
- قم بإزالة الأسرار والبيانات الشخصية من البكسلات نفسها قبل التضمين.
- لا تستخدم CSS blur كإخفاء أمني.
- لا تعدّل محتوى الواجهة لإجباره على مطابقة الشرح.
- عند نقص لقطة مهمة، اطلبها أو ضع placeholder واضحًا؛ لا تنشئ لقطة وهمية.

## الاستثناءات والأعطال

- إذا تعذر التحقق من سلوك النظام، أوقف الادعاء ودوّن ما ينقص.
- إذا اختلف الخط، تحقق من توفر IBM Plex Sans Arabic وInter ثم أعد التصدير.
- إذا انجرف التصميم، استعد `assets/master.css` وتحقق من hash.
- إذا تغير pagination، ارجع آخر تعديل، أعد البناء، ثم زامن الفهرس.
- إذا تعطلت صورة، أصلح مسار المصدر في JSON وأعد البناء؛ لا تعدّل base64 داخل HTML.
- احتفظ بنسخة سابقة سليمة أو استخدم source control قبل أي تحديث كبير.

## التسليم

سلّم الملفات النهائية فقط:

- `<system>-user-manual-ar.html`
- `<system>-user-manual-ar.pdf` عندما يكون مطلوبًا
- `<system>-user-manual-ar.source.json` للصيانة المستقبلية

اذكر الافتراضات وTBDs واختلاف الخط إن وجد. لا تسلّم مجلدات render المؤقتة إلا إذا طلب المستخدم أدلة QA.

## أمثلة التفعيل

يجب تفعيل المهارة لطلبات مثل:

- “اعمل لي دليل استخدام للنظام بنفس الدليل السابق.”
- “حوّل screenshots إلى user manual عربي RTL.”
- “حدّث فصل إدارة المستخدمين مع الحفاظ على التصميم حرفيًا.”
- “صدّر دليل Cashless إلى HTML وPDF.”

لا تفعّلها لتلخيص دليل، كتابة README، إنشاء تقرير عام، عرض تقديمي، أو إصلاح CSS غير متعلق بهذا القالب.
