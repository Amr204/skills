---
name: find-skills-local
description: Finds and ranks the strongest locally installed agent skills for the current project by scanning C:\Users\amral\.agents\skills and reading only each skill's name and description. Use when the user wants the best existing local skills for the project or task without searching online.
---

# Find Skills Local

Find the strongest and most relevant **locally installed skills** for the user's current project.

## Skills directory

Default:

```text
My Drive\MASAR\skills
```

If the user provides another local skills path, use that instead.

## Workflow

1. Understand the **current project** from the available project context:
   - user's current request
   - project files and folder structure
   - README or project metadata when available
   - technologies, frameworks, languages, and workflows in use

2. Recursively scan the local skills directory for `SKILL.md` files.

3. For each skill, read **only**:
   - `name`
   - `description`

4. Do not read the rest of a skill's instructions during discovery.

5. Compare each skill's name and description against the current project's needs.

6. Rank the strongest matches by:
   - direct relevance to the project
   - usefulness for the project's technologies and workflow
   - likely impact on the current work
   - specificity over generic overlap

7. Return only the best relevant skills. Put the strongest recommendation first.

## Response

Keep the result concise.

Example:

```text
أفضل المهارات المحلية المناسبة للمشروع:

1. <skill-name> — <why it fits>
2. <skill-name> — <why it fits>
3. <skill-name> — <why it fits>

الأفضل للبدء: <skill-name>
```

Include the local skill path when useful.

## Rules

- Local-only by default.
- Use `SKILL.md` frontmatter `name` and `description` as the discovery source.
- Do not inspect full skill instructions during discovery.
- Do not use `npx skills find`.
- Do not browse skills.sh, GitHub, npm, or other online skill sources.
- Do not install, update, delete, rename, move, or modify skills.
- Scan recursively because skills may be nested.
- Do not recommend every partial match; prefer a short ranked list of the strongest matches.
- If no suitable local skill exists, say so clearly.
- If the local skills directory cannot be accessed, report that instead of switching to online search.
