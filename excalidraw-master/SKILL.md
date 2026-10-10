---
name: excalidraw-master
description: Design, generate, analyze, repair, and improve Excalidraw diagrams for any idea, project, architecture, network, process, roadmap, workflow, mind map, system design, org chart, concept map, user flow, or technical/business visualization. Use this skill whenever the user asks for an Excalidraw file, a hand-drawn diagram, an editable visual map, converting structured ideas into a diagram, reading or fixing a .excalidraw file, or turning complex information into a clear editable canvas.
compatibility: Python 3.9+; no third-party packages required for core scripts.
---

# Excalidraw Master

Create Excalidraw diagrams that are semantically correct, visually clear, editable, compact, and structurally valid.

## Core principle

Do not treat Excalidraw as "JSON drawing". Treat every request as an information-design problem first, then a geometry/layout problem, then a file-format problem.

## Operating workflow

1. **Understand the intent**
   - Identify audience, purpose, expected decision/action, and level of detail.
   - Extract entities, groups, relationships, sequence, hierarchy, boundaries, and annotations.
   - If an input `.excalidraw` file exists, analyze it before changing anything.

2. **Choose the diagram family**
   Read `references/diagram-types.md` and select the best family or hybrid.

3. **Build a semantic model before coordinates**
   - Nodes = concepts, systems, actors, steps, states, or artifacts.
   - Edges = direction, dependency, data flow, sequence, ownership, association, or transition.
   - Containers = boundaries, phases, domains, layers, swimlanes, or clusters.
   - Notes = assumptions, legends, warnings, definitions, or evidence.

4. **Design the visual hierarchy**
   Read `references/design-system.md`.
   - One clear title.
   - 2–4 visual levels maximum in a single viewport where possible.
   - Strongest emphasis goes to the primary path or central concept.
   - Use color by meaning, never decoration alone.
   - Prefer whitespace over borders.

5. **Choose layout deliberately**
   - Flow/process: left→right by default; top→bottom for long sequential material.
   - Architecture/network: layers or zones with directional flows.
   - Roadmaps: vertical phases or horizontal timeline depending density.
   - Mind maps: radial only when relationships are genuinely radial.
   - Dense inventories: cards/columns, not spaghetti arrows.

6. **Generate or edit using the bundled builder**
   Use `scripts/excalidraw_builder.py` for deterministic construction.
   Use `scripts/analyze_excalidraw.py` before edits and for QA.
   Use `scripts/validate_excalidraw.py` before delivery.

7. **Run the quality gate**
   Read `references/quality-checklist.md` and fix all important failures.

8. **Deliver the editable `.excalidraw` file**
   Preserve source files when editing unless the user explicitly asks to overwrite.

## Input handling

### When the user provides prose or requirements
Convert the content into a semantic outline first. Do not put full paragraphs into shapes. Compress labels while preserving meaning.

### When the user provides an existing `.excalidraw`
Run:

```bash
python scripts/analyze_excalidraw.py input.excalidraw
python scripts/validate_excalidraw.py input.excalidraw
```

Then inspect:
- element counts and types;
- canvas dimensions and density;
- text hierarchy and font sizes;
- color usage;
- bound text / container relationships;
- arrow bindings and dangling references;
- groups/frames;
- repeated visual patterns;
- excessive whitespace or collisions;
- unusually long text blocks.

Preserve the existing visual language when it is coherent. Improve it only where the task requires.

## Output modes

### A. New diagram from scratch
Create a `Diagram` with the builder and generate rectangles/cards, text, arrows, lines, ellipses, diamonds, and section headers.

### B. Structured spec → Excalidraw
For repeatable work, create a small JSON spec and feed it to `scripts/generate_from_spec.py`.

### C. Analyze / review only
Return a concise structural review without modifying the file.

### D. Repair / improve existing diagram
Keep IDs stable when possible. Avoid deleting user content unless explicitly requested. Re-layout, restyle, bind, or simplify surgically.

## Semantic design rules

- Every arrow must have a meaning. If its meaning is ambiguous, label it or remove it.
- Do not use arrows merely to fill space.
- A container represents a real boundary or grouping, not decoration.
- Use consistent shapes for consistent semantics.
- Distinguish primary flow from secondary/reference relationships.
- Mark assumptions and unknowns visually distinct from confirmed facts when the source material has uncertainty.
- For architecture, distinguish trust/ownership/deployment/domain boundaries from simple grouping.
- For processes, distinguish states from actions and decisions.
- For data models, distinguish entities from events, stores, external systems, and relationships.

## Layout rules

- Default canvas origin near `(40, 40)`; avoid needless negative coordinates.
- Default node gap: 40–80 px.
- Default section gap: 100–160 px.
- Default card width: 220–360 px.
- Keep related objects aligned to shared x/y guides.
- Avoid edge crossings; reroute or reorder nodes first.
- If the diagram becomes taller than roughly 2–3 screens, add clear phase/section headings.
- If a canvas becomes extremely wide, split into zones or stacked bands.
- Prefer several coherent regions over one huge undifferentiated canvas.

## Text rules

- Title: 26–32 px.
- Section heading: 20–24 px.
- Card heading: 17–20 px.
- Body/annotation: 14–17 px.
- Use short labels; keep detailed explanations outside shapes or in dedicated notes.
- Use multiline text intentionally, not as accidental wrapping.
- Preserve Arabic text as UTF-8. For Arabic-heavy diagrams, favor wider cards and fewer words per line.

## Color rules

Use the semantic palette in `references/design-system.md`. Reuse a color for the same meaning. Never assign a unique color to every box unless color encodes a real category.

## Arrow rules

- Primary directional flow: 2 px solid arrow.
- Secondary/reference relationship: 1–2 px muted or dashed arrow.
- Use bindings for important anchored relationships when practical.
- Ensure arrow `points`, width, height, and bindings agree.
- Maintain reciprocal `boundElements` entries when binding arrows to elements.

## File integrity rules

A normal Excalidraw file must have top-level keys:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "...",
  "elements": [],
  "appState": {},
  "files": {}
}
```

Do not strip unknown element fields from existing files unless necessary. Excalidraw evolves; preserving compatible fields is safer than aggressively normalizing.

## Editing discipline

When modifying an existing file:
1. Clone the original structure.
2. Touch only elements necessary for the requested change.
3. Preserve IDs for unchanged elements.
4. Preserve `files` assets.
5. Recompute or carefully maintain arrow/container references.
6. Validate after the edit.

## Quality bar

A strong output should let a reader answer within seconds:
- What is this diagram about?
- Where should I start?
- What is the primary structure or flow?
- What do colors/shapes mean?
- What is inside/outside each boundary?
- What are the key relationships?

If not, simplify before delivery.

## Bundled references

- `references/diagram-types.md` — selection guide and layout recipes.
- `references/design-system.md` — typography, spacing, color, shapes, arrows.
- `references/excalidraw-format.md` — practical JSON structure and bindings.
- `references/quality-checklist.md` — final QA gate.
- `references/reference-file-analysis.md` — lessons extracted from the provided sample.

## Bundled scripts

- `scripts/excalidraw_builder.py` — reusable Python builder API.
- `scripts/generate_from_spec.py` — generate from a simple semantic JSON spec.
- `scripts/analyze_excalidraw.py` — structural analysis of any `.excalidraw` file.
- `scripts/validate_excalidraw.py` — structural and referential validation.

## Final verification

Always run:

```bash
python scripts/validate_excalidraw.py output.excalidraw
python scripts/analyze_excalidraw.py output.excalidraw --json
```

Do not claim completion when validation reports errors.
