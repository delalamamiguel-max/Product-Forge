---
name: best-in-class-benchmarking
description: Use after domain discovery and before writing requirements. Researches best-in-class products on the live web and scores them on functionality, usability, visual design, and UX/UI craft, producing a cited Feature Steal List. Triggers on "what does good look like", competitive analysis, feature ideation, or benchmarking requests.
---

# Best-in-Class Benchmarking

Find what excellent looks like in this specific industry, prove it with citations, and convert it into decided scope.

<HARD-GATE>
Benchmark from the live web, never from memory. Product UIs, pricing tiers, and feature sets change quarterly; your training data does not.
Any score without a cited URL is deleted, not defended.
</HARD-GATE>

## Reference set construction

A good set is deliberately uneven:

| Type | Count | Why |
|---|---|---|
| Direct competitors in the sub-vertical | 3–5 | Table stakes — what users will expect on day one |
| Category leaders from an adjacent larger market | 1–2 | Where the sub-vertical is heading |
| Cross-industry outlier solving the same *interaction* problem | 1 | Where the differentiation comes from |

The outlier is the highest-value entry. A dispatch tool can learn its map interaction from a food-delivery app; a clinical intake form can learn its progressive disclosure from a tax filing product.

## Research passes

1. **Capability pass** — docs, changelogs, pricing tiers, API references, integration directories. Pricing tiers reveal what the market actually pays for.
2. **Flow pass** — onboarding walkthroughs, demo videos, teardowns, trial the product where possible. Count the steps to core value.
3. **Craft pass** — public design-system pages, screenshot galleries, marketing site, pattern libraries. Look specifically at empty states, error states, and data density.
4. **Critique pass** — review-site themes, community threads, support forums. Complaints are requirements in disguise; the same complaint appearing across three competitors is a market opening.

## Scoring

Score 1–5 per axis using `rubrics/benchmark-rubric.md`. Write the justification before the number, not after — it prevents anchoring. Cite a URL per axis per product.

## Feature Steal List

Every candidate feature is a row:

| `BM-nn` source | Feature | Axis it won | Why it works here | Effort | Decision |
|---|---|---|---|---|---|

Decision is **IN / OUT / LATER** with a one-line reason. There is no such thing as an undecided row — undecided rows reappear as scope creep at implementation time, when they are twenty times more expensive.

## Anti-pattern harvest

Record what every reference does badly. This is the most under-used output of benchmarking: shared weaknesses become your NFRs and your positioning.

## Output contract

`02-benchmark-report.md` + `benchmarks[]` and `feature_candidates[]` in the packet.
