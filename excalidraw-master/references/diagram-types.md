# Diagram Types & Layout Recipes

## Decision guide

| Need | Best pattern | Default direction |
|---|---|---|
| Steps / workflow | Flowchart | Left → right |
| Long learning path | Phased roadmap | Top → bottom |
| System components | Layered architecture | Left → right / top → bottom |
| Network topology | Zones + topology | Core outward |
| Business process across roles | Swimlanes | Left → right |
| Ideas around one concept | Mind map | Radial |
| Domain concepts | Concept/domain map | Clustered |
| Data movement | Data-flow diagram | Source → processing → sink |
| States and transitions | State machine | Left → right |
| Org/reporting | Hierarchy tree | Top → bottom |
| Responsibilities | RACI-style lanes | Matrix / lanes |
| Project plan | Roadmap | Horizontal timeline or vertical phases |
| Options/tradeoffs | Comparison board | Columns |
| User journey | Journey flow | Left → right |

## Flowchart
Use rounded rectangles for actions, diamonds for decisions, arrows for sequence. Keep the happy path visually dominant and exceptions below it.

## Architecture
Use large containers for system/domain/trust boundaries, cards for components, cylinders only when a datastore needs explicit distinction, and labeled arrows for APIs/events/data movement. Avoid implying deployment boundaries unless known.

## Network
Use zones (Internet, Edge, DMZ, Internal, Cloud, Branch) and devices inside them. Differentiate physical/logical connectivity only if relevant. Label protocols on important links.

## Roadmap / learning path
Use strong phase headings, compact content cards, a clear start, and directional continuity. For long content, stack phases vertically and keep consistent widths.

## Swimlane
One lane per actor/team/system. Activities sit inside the owning lane; arrows cross lanes only when handoff occurs. Use consistent horizontal time/sequence.

## Mind map
Use only when hierarchy is more important than sequence. Center node should be visually strongest. Limit depth visible at once.

## Domain / concept map
Use category color by semantic type, not arbitrary node color. Prefer fewer, labeled relationships over many unlabeled lines.

## Data-flow
Separate external actors, processes, data stores, and flows. Directionality matters. Do not infer data stores that are not evidenced.

## State machine
States are nouns/adjectives; transitions are events/actions. Label transition edges. Mark terminal states clearly.

## Hybrid diagrams
Combine patterns only when each region remains recognizable. Example: architecture overview at top + workflow below. Use section headers and whitespace to separate the visual grammars.
