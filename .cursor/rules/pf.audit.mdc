---
name: pf.audit
description: Cross-artifact traceability, coverage, and completeness gate. Must pass before handoff.
---

# /pf.audit

Invoke the `traceability-audit` skill. Run `scripts/pf-validate.py products/$PF_SLUG/product-packet.yaml`.

## Checks

**Traceability**
- Every `FR-nnn` traces up to a `DOM-nn` need, a `BM-nn` decision, or a flagged original bet
- Every `FR-nnn` traces down to at least one `US-nnn`
- Every `US-nnn` traces up to at least one `FR-nnn` — orphan stories are scope creep
- Every `RULE-FRnnn-nn` has a live parent FR
- Every `CMP-nn` and `UX-nn` is referenced by at least one story
- No duplicate IDs; no gaps that indicate a silent deletion

**Coverage**
- Every IN row on the Feature Steal List has an FR
- Every constitution principle has an NFR or an explicit ADR enforcing it
- Every persona in the domain brief appears in at least one story
- Every regulatory obligation maps to an NFR and an architecture control

**Quality**
- Zero `[NEEDS CLARIFICATION]` markers anywhere
- Zero placeholder text, lorem ipsum, or "TBD"
- Every NFR carries a number and a measurement method
- Every acceptance criterion is Given/When/Then and independently verifiable
- Every risk has an owner, a trigger, and a mitigation — not just a description
- Every KPI has a baseline, a target, a measurement window, and an instrumentation point

## Output

An audit report with **PASS / FAIL per check** and a concrete remediation for every failure.

<HARD-GATE>
Do NOT run /pf.handoff while any check is FAIL.
Fix the artifacts and re-run. Do not annotate a failure as "acceptable" — either fix it or record it as an accepted risk with an owner in the risk register, which itself must pass.
</HARD-GATE>
