---
name: pf.benchmark
description: Research best-in-class products on the live web and score them on functionality, usability, visual, and UX/UI.
---

# /pf.benchmark

Invoke the `best-in-class-benchmarking` and `design-reference-harvest` skills. Produce `products/$PF_SLUG/02-benchmark-report.md`.

## Process

1. Read `01-domain-brief.md`. Take `domain.benchmark_candidates` as the starting set.
2. **Search the live web.** Do not benchmark from memory — product UIs change quarterly and your training data is stale. For each candidate, gather:
   - Feature inventory (docs, changelog, pricing page tiers)
   - Onboarding and core-flow walkthroughs (reviews, demo videos, teardowns)
   - Visual and interaction reference (design-system pages, public screenshots, Dribbble/Mobbin-style galleries, the vendor's own marketing site)
   - Third-party critique (G2/Capterra themes, HN/Reddit threads, UX teardowns)
3. Widen the set deliberately:
   - 3–5 **direct** competitors in the sub-vertical
   - 1–2 **category leaders** from a larger adjacent market
   - 1 **outlier** from an unrelated industry that solves the same interaction problem beautifully
4. Score every reference on the four axes using `rubrics/benchmark-rubric.md`. **Every score needs a cited URL.** An uncited score is deleted.
5. Build the **Feature Steal List**: each candidate feature gets `BM-nn` provenance, the axis it won on, an effort estimate, and an explicit IN / OUT / LATER decision with a one-line reason.
6. Extract a **visual and interaction reference set**: 8–15 specific patterns worth adopting (empty states, density model, nav shape, primary-action placement, data-table behavior, color role assignment), each tied to `BM-nn`.
7. Note the **anti-patterns**: what every reference does badly. These become NFRs and differentiation.

## Output

- `02-benchmark-report.md`: scored matrix, Feature Steal List, visual reference set, anti-patterns
- `product-packet.yaml`: `benchmarks[]` with `id`, `name`, `url`, `scores`, `notes`; `feature_candidates[]` with decisions

<HARD-GATE>
Do NOT write the PRD until the Feature Steal List has an explicit IN/OUT/LATER decision on every row.
Undecided rows become scope creep during implementation.
</HARD-GATE>
