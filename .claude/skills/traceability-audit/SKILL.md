---
name: traceability-audit
description: Use before handing any spec package to a coding agent. Verifies cross-artifact traceability, coverage, and completeness, and blocks handoff on failure. Triggers on audit, review the spec, is this ready, pre-handoff check, or completeness verification.
---

# Traceability Audit

The quality gate. Its job is to fail.

<HARD-GATE>
Handoff is blocked while any check is FAIL.
An audit that passes on the first run usually means the checks were run too leniently, not that the spec was perfect. Look harder.
</HARD-GATE>

## Trace graph

```
DOM-nn ──┐
         ├──▶ FR-nnn ──▶ US-nnn ──▶ task
BM-nn  ──┘      │
                ├──▶ RULE-FRnnn-nn
                ├──▶ UX-nn ──▶ CMP-nn
                └──▶ NFR-nnn ──▶ ADR-nnn
```

Every node must have a parent and at least one child, except leaves.

## Checks

**Upward** — every FR traces to a DOM, BM, or flagged bet · every US traces to an FR · every RULE has a live parent · every CMP and UX is used by a story

**Downward** — every FR has a US · every IN feature has an FR · every constitution principle has an enforcing NFR or ADR · every persona appears in a story · every regulatory obligation maps to an NFR *and* an architecture control

**Integrity** — no duplicate IDs · no gaps indicating silent deletion · no dangling references to deprecated IDs

**Quality** — zero `[NEEDS CLARIFICATION]` · zero placeholders · every NFR numbered and measurable · every AC in Given/When/Then and independently verifiable · every risk has owner + trigger + mitigation · every KPI has baseline + target + window + instrumentation point

## Reporting

Per check: **PASS / FAIL**, the specific offending IDs, and a concrete remediation. Never report a bare "FAIL — traceability issues."

An issue may only be closed by fixing the artifact, or by recording it as an accepted risk with a named owner in the risk register — which is itself audited. "Acceptable for now" without an owner is not a resolution.
