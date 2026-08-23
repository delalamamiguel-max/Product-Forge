---
name: pf.plan
description: Technical architecture, stack, data model, and integrations — the how.
---

# /pf.plan

Produce `products/$PF_SLUG/05-architecture-plan.md` from `templates/05-architecture-plan.md`.

## Process

1. Re-read the constitution. Stack constraints there are binding.
2. Choose the stack and **justify each choice against a constitution principle or a domain constraint**, not against popularity. Record each as an ADR (`ADR-nnn`): context, options considered, decision, consequences.
3. Data model: entities, relationships, cardinality, ownership, tenancy boundary, retention policy per entity. Map each entity back to the FRs that need it.
4. Integrations: for every external system, capture **the constraints that shape the product** — rate limits, data freshness (real-time vs. daily batch), auth model, failure mode, cost per call. Freshness and rate limits routinely change what the product can promise the user; when they do, amend the PRD rather than papering over it in code.
5. Security & compliance posture derived from `domain.regulatory`: authN/authZ model, encryption at rest and in transit, audit logging, PII/PHI handling, data residency.
6. Environments, deployment topology, observability plan, rollback strategy.
7. Sequencing constraints: what must be built before what, and why.

## Output

`05-architecture-plan.md` + packet `architecture`, `adrs[]`, `integrations[]`.
