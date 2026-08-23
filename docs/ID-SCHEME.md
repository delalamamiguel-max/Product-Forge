# ID Scheme

Traceability is the whole point. IDs are the mechanism.

## Namespaces

| Prefix | Artifact | Example |
|---|---|---|
| `PRIN-nn` | Constitution principle | `PRIN-03` |
| `DOM-nn` | Domain finding, JTBD, or constraint | `DOM-07` |
| `BM-nn` | Benchmark reference | `BM-04` |
| `FR-nnn` | Functional requirement | `FR-014` |
| `NFR-nnn` | Non-functional requirement | `NFR-002` |
| `RULE-FRnnn-nn` | Business rule scoped to a parent FR | `RULE-FR014-02` |
| `DS-nn` | Design token | `DS-06` |
| `CMP-nn` | Component | `CMP-11` |
| `UX-nn` | User flow | `UX-03` |
| `ADR-nnn` | Architecture decision record | `ADR-005` |
| `EPIC-nn` | Epic | `EPIC-02` |
| `US-nnn` | User story | `US-031` |
| `RISK-nn` | Risk | `RISK-08` |
| `KPI-nn` | Key metric | `KPI-04` |
| `GRD-nn` | Guardrail metric | `GRD-01` |

## Rules

1. **Stable forever.** Never renumber. Renumbering breaks every downstream reference, and the break is invisible until implementation.
2. **Never reuse.** A deleted ID stays deleted. Reuse makes git history lie.
3. **Deprecate, don't delete.** `status: superseded_by: FR-047`.
4. **Scoped rules carry their parent.** `RULE-FR014-02` is unambiguous three months later; `RULE-23` is not.
5. **Assign at creation.** An artifact written without IDs cannot be audited and will have to be rewritten.

## The trace graph

```
PRIN-nn ──────────────────▶ NFR-nnn ──▶ ADR-nnn
                               │
DOM-nn ──┐                     │
         ├──▶ FR-nnn ──────────┼──▶ US-nnn ──▶ task ──▶ code
BM-nn  ──┘       │             │        │
                 ├─▶ RULE-     │        └──▶ verification
                 └─▶ UX-nn ──▶ CMP-nn ──▶ DS-nn
                                              │
KPI-nn ◀────── EPIC-nn ◀──────────────────────┘
```

Every node needs a parent and at least one child, except leaves. `scripts/pf-validate.py` enforces this.

## What the graph buys you

**Change impact in one query.** "The API turned out to refresh daily, not in real time" → find every FR touching that integration, every RULE under them, every story tracing to those FRs, every UX flow promising freshness. Amend deliberately instead of discovering the inconsistency in QA.

**Scope defense.** A feature request with no parent DOM or BM is visibly ungrounded. The graph makes the argument for you.

**Agent auditability.** Code traces to a task traces to `US-031` traces to `FR-014` traces to `DOM-07`. When a reviewer asks why something works this way, the answer is a path, not a memory.

**Honest deletion.** Cutting `FR-014` shows you exactly which stories, components, and flows die with it — before you cut, not after.
