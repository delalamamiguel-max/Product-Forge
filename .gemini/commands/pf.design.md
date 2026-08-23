---
name: pf.design
description: Derive the design system and UX flows from benchmark evidence, not from taste.
---

# /pf.design

Invoke the `design-reference-harvest` skill. Produce `products/$PF_SLUG/04-design-system.md`.

## Process

1. Read the visual reference set from `02-benchmark-report.md`. Every design decision below must cite a `BM-nn` or an explicit domain constraint from `DOM-nn`.
2. **Industry fit first.** Density, tone, and chrome are industry decisions, not aesthetic ones:
   - Clinical / operational / financial → dense, keyboard-first, muted, high information ratio
   - Consumer / marketplace → generous spacing, imagery-forward, thumb-reachable
   - Field / industrial → large targets, high contrast, glove- and sunlight-tolerant
   - Prosumer tooling → command palette, shortcuts, progressive disclosure
3. Define **tokens** (`DS-nn`): type scale and font pairing with rationale, spacing scale, color roles (not hex swatches — semantic roles: surface, elevated, accent, destructive, focus), radius, elevation, motion durations and easing.
4. Define the **component inventory** (`CMP-nn`): only components the FRs actually require. For each, specify **all** of: default, hover, focus-visible, active, disabled, loading, empty, error, and overflow behavior. Missing states are the single most common cause of agent-built UI looking unfinished.
5. Define **UX flows** (`UX-nn`) for each primary job: entry point → steps → decision points → success state → every failure branch. Count the steps to the core action and justify anything over three.
6. Set the **accessibility baseline** from the constitution: contrast ratio, focus order, keyboard-only path for every flow, screen-reader labeling, motion-reduction behavior, minimum target size.
7. Write **microcopy rules**: voice, error message pattern, empty-state pattern, confirmation-vs-undo policy.

## Output

`04-design-system.md` + packet `design.tokens[]`, `design.components[]`, `design.flows[]`.

<HARD-GATE>
No component ships in this doc without its empty, loading, and error states defined.
No flow ships without its failure branches.
</HARD-GATE>
