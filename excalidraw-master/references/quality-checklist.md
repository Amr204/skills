# Quality Checklist

## Semantics
- [ ] Title states the subject clearly.
- [ ] Start point or visual entry is obvious.
- [ ] Shape types have consistent meanings.
- [ ] Colors encode categories/status/meaning consistently.
- [ ] Every important arrow has an understandable meaning.
- [ ] Unknown/assumed information is not visually presented as confirmed.

## Layout
- [ ] Major groups are aligned.
- [ ] Whitespace separates sections.
- [ ] Edge crossings are minimized.
- [ ] No important text overlaps shapes or arrows.
- [ ] Long diagrams have section landmarks.
- [ ] Canvas bounds are reasonable for content.

## Text
- [ ] Labels are concise.
- [ ] Font hierarchy is consistent.
- [ ] Body text is readable at normal zoom.
- [ ] Arabic/RTL content is not cramped.

## File integrity
- [ ] JSON parses.
- [ ] Top-level Excalidraw keys exist.
- [ ] IDs are unique.
- [ ] Bound element references resolve.
- [ ] Arrow binding references resolve.
- [ ] Text container references resolve.
- [ ] No deleted element is accidentally used as an active dependency.
- [ ] `files` assets are preserved on edit.

## Final
- [ ] Run `validate_excalidraw.py` with zero errors.
- [ ] Run `analyze_excalidraw.py --json` and inspect element counts/bounds.
