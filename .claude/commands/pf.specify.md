---
name: pf.specify
description: Write the PRD with stable, traceable requirement IDs.
---

# /pf.specify

Invoke the `requirements-authoring` skill. Produce `products/$PF_SLUG/03-prd.md` from `templates/03-prd.md`.

## Process

1. Read `00-constitution.md`, `01-domain-brief.md`, `02-benchmark-report.md`. Every requirement must trace to a `DOM-nn` need or a `BM-nn` benchmark decision — or be flagged as a deliberate original bet.
2. Write **what and why**, never how. No framework names, no table schemas, no API shapes. Those belong in `/pf.plan`.
3. ID discipline:
   - `FR-nnn` functional requirement — one behavior, testable, in domain vocabulary
   - `NFR-nnn` non-functional — performance, security, accessibility, availability, compliance. Each carries a number.
   - `RULE-FRnnn-nn` business rule scoped to a parent FR
   - Never renumber. Deprecate with `status: superseded_by: FR-nnn`.
4. Mark every unknown inline as `[NEEDS CLARIFICATION: question]`. Do not guess. Do not silently choose a default.
5. Define scope boundaries explicitly: **In scope / Out of scope / Deferred (with the condition that would pull it in)**.
6. Write personas and primary flows in the domain glossary's language.

## Self-review before finishing

- [ ] Every FR is independently testable by someone who has not read the rest of the doc
- [ ] No implementation detail leaked in
- [ ] Every IN feature from the Steal List has an FR; every FR traces to `DOM-nn`, `BM-nn`, or an explicit bet
- [ ] No placeholder text, no "TBD" that isn't a `[NEEDS CLARIFICATION]`
- [ ] Constitution principles are not contradicted anywhere

## Output

`03-prd.md` + `product-packet.yaml` `requirements[]`.
