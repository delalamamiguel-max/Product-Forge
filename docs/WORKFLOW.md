# Workflow

## The chain

```
00 constitution ─▶ 01 domain brief ─▶ 02 benchmark ─▶ 03 PRD ─▶ clarify
                                                                   │
   handoff ◀─ audit ◀─ 09 roadmap ◀─ 06 backlog ◀─ 05 plan ◀─ 04 design
```

Each phase reads everything before it. Nothing reads forward.

## Phases

| # | Command | Consumes | Produces | Gate |
|---|---|---|---|---|
| 0 | `/pf.constitution` | user input | `00-constitution.md`, `PRIN-nn` | User approval |
| 1 | `/pf.discover` | constitution | `01-domain-brief.md`, `DOM-nn`, glossary | **Sub-vertical named, user/buyer split, regulatory explicit, approved** |
| 2 | `/pf.benchmark` | domain brief | `02-benchmark-report.md`, `BM-nn`, Steal List | **Every Steal List row decided IN/OUT/LATER** |
| 3 | `/pf.specify` | 00–02 | `03-prd.md`, `FR-nnn`, `NFR-nnn`, `RULE-` | Self-review checklist |
| 4 | `/pf.clarify` | PRD | amended PRD, `decisions[]` | **Zero `[NEEDS CLARIFICATION]`** |
| 5 | `/pf.design` | 01–03 | `04-design-system.md`, `DS/CMP/UX-nn` | **All nine states per component; failure branches per flow** |
| 6 | `/pf.plan` | 00–04 | `05-architecture-plan.md`, `ADR-nnn` | Each stack choice justified against a principle |
| 7 | `/pf.stories` | 03–05 | `06-backlog.md`, `09-roadmap.md`, `EPIC/US` | Slice 1 is end-to-end |
| 8 | `/pf.audit` | everything | audit report | **All checks PASS** |
| 9 | `/pf.handoff` | everything | `handoff/` packet | Audit passed |

## Why the order

**Constitution before domain** — you need the non-negotiables before you can judge which domain constraints are binding.

**Domain before benchmark** — you can't pick reference products until you know the sub-vertical. Benchmarking first produces a set of whatever is famous, which is usually the wrong market.

**Benchmark before PRD** — requirements written before research are a list of what you already thought of. Requirements written after are a list of what the market has proven users need, plus your deliberate bets, and you can tell them apart.

**PRD before design** — design decisions made before requirements are decoration. Design decisions made after are solutions.

**Design before architecture** — interaction requirements shape data access patterns. A drag-to-reschedule flow implies optimistic updates and conflict resolution; discovering that after the schema is set is expensive.

**Stories last** — a story written before the design system exists cannot reference `CMP-07`, so it hand-waves the UI, so the agent invents it.

## Iterating

When something changes, amend the earliest affected artifact and re-run forward from there. Never patch a later artifact to compensate for an earlier one — that's how the trace graph breaks, silently.

The one exception: implementation discoveries. When a coding agent finds a spec defect, the fix goes into the PRD and the packet is regenerated. The packet is a build output, never edited in place.

## Reduced path for small work

For a genuinely small internal tool, `/pf.discover` → `/pf.specify` → `/pf.stories` → `/pf.handoff` is defensible. `/pf.discover` is never skippable — it is the phase that makes the output specific rather than generic, and it costs ten minutes.
