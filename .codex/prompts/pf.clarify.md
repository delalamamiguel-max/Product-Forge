---
name: pf.clarify
description: Eliminate every ambiguity in the PRD through structured Q&A and bake the answers back in.
---

# /pf.clarify

## Process

1. Scan `03-prd.md` for every `[NEEDS CLARIFICATION]` marker.
2. Additionally hunt for *unmarked* ambiguity in these categories — these are where specs silently fail:
   - Data lifecycle: retention, deletion, archival, export, audit trail
   - Multi-user: roles, permissions, concurrency, conflict resolution
   - Failure: what happens offline, on timeout, on partial write, on third-party outage
   - Boundaries: pagination limits, file sizes, rate limits, quota behavior at the ceiling
   - Enumerations: is this a closed set or an open string owned by someone else?
   - Time: timezone authority, business hours, scheduling conflicts, DST
   - Money & units: currency, rounding, tax, unit-of-measure conversion
   - Identity: auth method, session lifetime, account recovery, tenant isolation
3. Ask **one question at a time**, each with 2–4 concrete options and a recommended default with its rationale. Never ask an open-ended "how should this work?"
4. Write each answer back into the PRD as a new `RULE-FRnnn-nn` or an amended FR. Delete the marker.
5. Log every decision in `product-packet.yaml` `decisions[]` with date and rationale — so nobody relitigates it in month three.

<HARD-GATE>
Do NOT proceed to /pf.design or /pf.plan while any [NEEDS CLARIFICATION] marker remains.
Ambiguity that survives this phase becomes an agent's improvisation during implementation.
</HARD-GATE>
