---
name: pf.stories
description: Decompose the PRD into epics and user stories sized for a coding agent.
---

# /pf.stories

Invoke the `story-decomposition` skill. Produce `products/$PF_SLUG/06-backlog.md` and `09-roadmap.md`.

## Process

1. Group FRs into epics (`EPIC-nn`) around **user outcomes**, not system layers. "Book an appointment" is an epic; "build the API layer" is not.
2. Write stories (`US-nnn`):
   - `As a <persona from the domain brief>, I want <capability>, so that <outcome in the user's terms>`
   - Acceptance criteria in **Given / When / Then**, covering the happy path, at least one edge case, and at least one failure path
   - `traces_to: [FR-014, RULE-FR014-02, UX-03, CMP-07]`
   - Sizing: **one story should be completable by a coding agent in a single focused session.** If it needs more than ~8 acceptance criteria or touches more than one epic's data, split it.
3. Add the invisible work explicitly — it's what agents skip: empty states, loading states, error handling, validation messages, permission denials, audit logging, migrations, seed data, analytics instrumentation.
4. Sequence into release slices in `09-roadmap.md`. Each slice needs:
   - A user-facing outcome (not "phase 2")
   - Entry criteria and exit criteria
   - The `KPI-nn` it moves
   - Explicit dependencies on other slices
5. Slice 1 must be a **thin end-to-end vertical** — one complete user journey working — not a horizontal foundation layer.

## Output

`06-backlog.md`, `09-roadmap.md` + packet `epics[]`, `stories[]`, `roadmap[]`.
