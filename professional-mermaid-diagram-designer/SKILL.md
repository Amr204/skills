---
name: professional-mermaid-diagram-designer
description: >
  Use this skill when the user asks to create, improve, redesign, beautify,
  organize, or convert an idea, system, process, architecture, workflow,
  troubleshooting plan, Linux/systemd flow, cybersecurity flow, AI/RAG/agent
  architecture, database workflow, DevOps process, or technical explanation into
  a professional Mermaid diagram. The skill must produce clean, modern, colorful,
  readable Mermaid diagrams with rounded corners, curved lines, clear hierarchy,
  Arabic-friendly labeling, technical precision, and a polished visual style.
---

# Professional Mermaid Diagram Designer Skill

## 1. Purpose

This skill generates professional Mermaid diagrams that are:

- visually clean
- technically accurate
- organized from top to bottom
- suitable for technical documentation
- suitable for cybersecurity, AI, DevOps, database, Linux, and architecture planning
- beautiful without becoming visually noisy
- readable in Arabic and English
- styled with modern colors
- free from sharp, ugly, crowded, or overlapping shapes

The main goal is to transform rough technical ideas into a polished diagram that looks like a professional engineering document.

---

## 2. When to Use This Skill

Use this skill whenever the user asks for any of the following:

- "اكتب لي مخطط Mermaid"
- "رتب لي هذا بمخطط"
- "افعل لي flowchart"
- "اشتيه ملون"
- "اشتيه احترافي"
- "اشتيه مثل الصورة"
- "خليه زوايا منحنية"
- "خليه واضح ومش متداخل"
- "اعمل architecture diagram"
- "اعمل system design diagram"
- "اعمل cybersecurity workflow"
- "اعمل AI/RAG/Agent diagram"
- "اشرحه بمخطط"
- "حوّل الكلام هذا إلى Mermaid"
- "رتب لي الخطة بصريًا"

Also use this skill if the user provides:

- a screenshot of a diagram
- messy Mermaid code
- a rough technical process
- a list of components
- shell scripts/systemd services/timers
- AI system components
- database workflow
- security testing methodology
- incident response plan
- DevOps pipeline

---

## 3. Core Output Principles

Every diagram must follow these principles:

1. **Direct usefulness first**
   - The diagram must explain the system clearly.
   - Beauty is important, but clarity is more important.

2. **Rounded shapes by default**
   - Avoid sharp rectangle syntax:
     - Bad: `A["text"]`
   - Prefer rounded syntax:
     - Good: `A("text")`
   - For main titles or soft pill-like nodes:
     - Good: `A(["text"])`

3. **Curved links by default**
   - Always use:
     ```mermaid
     "flowchart": {
       "curve": "basis"
     }
     ```
   - This gives the diagram smoother lines.

4. **Top-down hierarchy**
   - Prefer:
     ```mermaid
     flowchart TD
     ```
   - Use `LR` only when the process is naturally left-to-right.

5. **No visual crowding**
   - Avoid huge unreadable nodes unless the user explicitly wants all details inside one box.
   - Break large logic into clear stages.
   - Use subgraphs when there are logical groups.

6. **Arabic-friendly formatting**
   - Arabic labels are allowed.
   - Keep Arabic short and clean.
   - Use English technical names where useful.
   - Use `<br/>` for line breaks.
   - Use `<b>...</b>` for important component names.
   - Use `<code>...</code>` for commands, paths, services, APIs, and filenames.

7. **Professional engineering tone**
   - Labels should be precise.
   - Avoid vague labels such as:
     - "stuff"
     - "things"
     - "do something"
   - Use exact technical terms:
     - `systemd timer`
     - `oneshot service`
     - `flock`
     - `timeout`
     - `RAG pipeline`
     - `Vector DB`
     - `SQL validation`
     - `Access Control`

---

## 4. Default Mermaid Theme

Unless the user asks for another style, use this theme:

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis"
  },
  "themeVariables": {
    "background": "#111827",
    "primaryColor": "#1f2937",
    "primaryTextColor": "#e5e7eb",
    "primaryBorderColor": "#22c55e",
    "lineColor": "#94a3b8",
    "fontFamily": "Segoe UI, Arial"
  }
}}%%