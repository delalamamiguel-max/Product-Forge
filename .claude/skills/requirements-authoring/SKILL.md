---
name: requirements-authoring
description: Use when writing a PRD, functional requirements, non-functional requirements, or business rules. Enforces stable ID discipline, testability, traceability to domain and benchmark evidence, and explicit ambiguity marking. Triggers on PRD, requirements, spec writing, or scope definition.
---

# Requirements Authoring

## ID discipline

| Pattern | Meaning |
|---|---|
| `FR-nnn` | Functional requirement — one behavior, testable |
| `NFR-nnn` | Non-functional — always carries a number and a measurement method |
| `RULE-FRnnn-nn` | Business rule scoped to a parent FR |
| `ADR-nnn` | Architecture decision record |

IDs are **stable forever**. Never renumber, never reuse. Deprecate with `status: superseded_by: FR-nnn`. Renumbering silently breaks every downstream trace, and the break is invisible until implementation.

## What belongs where

The PRD carries **what and why**. No framework names, no schemas, no endpoints, no library choices. Those go in the architecture plan. This separation is what lets you change stack without rewriting requirements.

## Testability

Every FR must be verifiable by someone who has read only that FR.

- Bad: "The system should handle errors gracefully."
- Good: "FR-042 — When a sync fails, the system retains the last successful record set, surfaces the failure time and cause in the header, and offers a manual retry. NFR-011 — Sync failure is surfaced within 5s of detection."

Every NFR carries a number and how you measure it. "Fast," "secure," and "intuitive" are not requirements.

## Traceability up

Every FR traces to one of exactly three things:
1. A `DOM-nn` domain need
2. A `BM-nn` benchmark decision
3. An **explicitly flagged original bet** — with the hypothesis and how you'll know if it was wrong

If an FR traces to none of these, it is a feature someone wanted for no reason. Delete it or find its parent.

## Ambiguity

Mark inline: `[NEEDS CLARIFICATION: does an appointment reminder go to the patient, the guardian, or both?]`

<HARD-GATE>
NEVER resolve an ambiguity by silently choosing a plausible default.
A silent default is a decision made by the person with the least context — you — and it will be discovered in production.
Mark it and let /pf.clarify resolve it with the user.
</HARD-GATE>

## Scope boundaries

Three explicit lists: **In scope**, **Out of scope** (permanent), **Deferred** (with the specific condition that would pull it back in). The deferred list with conditions is what stops the "while we're in here..." conversation during implementation.

## Self-review before finishing

- [ ] Every FR independently testable
- [ ] Every NFR has a number and a measurement method
- [ ] Zero implementation detail
- [ ] Every FR traces up; every IN feature has an FR
- [ ] Zero placeholders that aren't marked `[NEEDS CLARIFICATION]`
- [ ] No constitution principle contradicted
- [ ] Domain glossary vocabulary used consistently
