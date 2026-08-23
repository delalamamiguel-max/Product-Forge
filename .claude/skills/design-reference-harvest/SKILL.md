---
name: design-reference-harvest
description: Use when defining the visual language, design system, or UX flows for a product. Converts benchmark evidence into tokens, a component inventory with full state coverage, and flow definitions. Triggers on design system, UI direction, visual identity, or UX flow work.
---

# Design Reference Harvest

Turn benchmark evidence into a specification a coding agent can build from without guessing.

## Principle

Visual decisions are **industry decisions before they are aesthetic ones**. Density, chrome, tone, and motion are determined by who uses the product, in what environment, under what time pressure. A trading terminal and a meditation app can both be beautifully designed and share no visual decisions whatsoever.

## Density model — choose one and commit

| Model | Fits | Characteristics |
|---|---|---|
| Operational | Clinical, logistics, finance, ops consoles | Dense tables, keyboard-first, muted palette, high information ratio, minimal motion |
| Consumer | Marketplaces, social, booking | Generous spacing, imagery-forward, thumb-reachable, expressive motion |
| Field | Construction, utilities, warehouse, delivery | Large targets, extreme contrast, glove/sunlight tolerant, offline-visible state |
| Prosumer tool | Developer and creator tooling | Command palette, shortcuts, progressive disclosure, dark-mode-first |

## Tokens (`DS-nn`)

Define **semantic roles**, not swatches. `color.surface.raised`, `color.action.destructive`, `color.feedback.focus` survive a rebrand; `blue-500` does not. Include: type scale with a named pairing and rationale, spacing scale, color roles, radius scale, elevation, motion durations and easing curves, and the breakpoint set.

## Component inventory (`CMP-nn`)

Only components the FRs actually require. For each, **all nine states**: default, hover, focus-visible, active, disabled, loading, empty, error, overflow.

<HARD-GATE>
A component with undefined empty, loading, and error states is not specified.
Missing states are the single largest cause of agent-built interfaces looking unfinished — the agent invents them, inconsistently, in nine different places.
</HARD-GATE>

## Flows (`UX-nn`)

Per primary job: entry point, ordered steps, decision points, success state, and **every failure branch**. Count steps to the core action; anything above three needs a written justification.

## Accessibility baseline

Inherit the target from the constitution. Specify: contrast ratio, complete keyboard-only path per flow, focus order, screen-reader labeling convention, reduced-motion behavior, minimum target size, and error-announcement pattern.

## Microcopy rules

Voice, error message pattern, empty-state pattern, and the confirmation-vs-undo policy. Agents write filler copy unless given a pattern; give them the pattern.
