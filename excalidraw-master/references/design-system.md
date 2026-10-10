# Excalidraw Design System

## Typography
- Canvas title: 28 px, dark neutral.
- Subtitle: 16 px, muted.
- Section: 22 px.
- Card title: 18 px.
- Body: 16 px.
- Small label: 13–14 px.
- Default font family value: 5 when matching the provided reference style; fall back to 1 if compatibility requires.

## Semantic palette
- Neutral text/stroke: `#1e1e1e`
- Muted text: `#757575`
- Blue / primary / network: stroke `#2563eb`, fill `#a5d8ff`
- Amber / dependency / caution: stroke `#f59e0b`, fill `#ffd8a8`
- Purple / security / specialized: stroke `#8b5cf6`, fill `#d0bfff`
- Cyan / integration / data: stroke `#06b6d4`, fill `#99e9f2`
- Green / success / ready: stroke `#22c55e`, fill `#b2f2bb`
- Pink / people / UX: stroke `#ec4899`, fill `#eebefa`
- Red / risk / failure: stroke `#ef4444`, fill `#ffc9c9`

Use light fills with strong strokes. When creating background regions, reduce opacity instead of saturating colors.

## Shapes
- Rounded rectangle: normal concept/action/component.
- Diamond: decision.
- Ellipse: start/end, actor, or central concept when appropriate.
- Large translucent rectangle: zone/phase/container.
- Text-only: titles, captions, annotations.

## Spacing
- Internal padding: 14–20 px.
- Between peer cards: 40–60 px.
- Between groups/sections: 100–160 px.
- Outer canvas margin: at least 40 px.

## Stroke
- Primary shape: 2 px solid.
- Secondary background/container: 1 px, often 20–35% opacity.
- Primary flow arrow: 2 px.
- Secondary/reference: dashed or muted.

## Hierarchy
Never make every element equally loud. Use a predictable order:
1. Canvas title
2. Section headings / main path
3. Card headings
4. Body details
5. Notes / metadata
