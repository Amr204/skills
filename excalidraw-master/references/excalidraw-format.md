# Practical Excalidraw JSON Notes

## Top level
`type`, `version`, `source`, `elements`, `appState`, `files`.

## Common element fields
`id`, `type`, `x`, `y`, `width`, `height`, `angle`, `strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`, `strokeStyle`, `roughness`, `opacity`, `groupIds`, `frameId`, `roundness`, `seed`, `version`, `versionNonce`, `isDeleted`, `boundElements`, `updated`, `link`, `locked`.

## Text
Text elements also use `text`, `fontSize`, `fontFamily`, `textAlign`, `verticalAlign`, `containerId`, `originalText`, `autoResize`, and `lineHeight`.

When text is bound to a container, set `containerId` on the text and add `{ "type": "text", "id": "..." }` to the container's `boundElements`.

## Arrows
Arrows use `points`, `lastCommittedPoint`, `startBinding`, `endBinding`, `startArrowhead`, `endArrowhead`, and optionally `elbowed`.

If an arrow binds to a node, the node should list the arrow in `boundElements`.

## Preservation rule
When editing an existing file, retain unknown fields. Avoid round-tripping through a restrictive schema that discards fields Excalidraw may need.
