# Four-Axis Benchmark Rubric

Score every reference product 1–5 on each axis. **Write the justification before the number** — writing the number first anchors the justification. **Every score requires a cited URL.** Uncited scores are deleted, not defended.

---

## Axis 1 — Functionality

Depth of the core job, edge-case coverage, integration surface, data model sophistication.

| Score | Standard |
|---|---|
| 5 | Handles the core job plus the messy real-world cases practitioners actually hit. Rich integration surface. Data model supports workflows the vendor didn't anticipate. |
| 4 | Core job handled thoroughly; common edge cases covered; solid integrations. |
| 3 | Core job handled. Edge cases require workarounds. Basic integrations. |
| 2 | Core job partially handled; users maintain a parallel system for the rest. |
| 1 | Demo-grade. |

**Evidence sources:** docs, changelog, pricing tiers, API reference, integration directory. Pricing tiers are the highest-signal source here — they reveal what the market actually pays for.

---

## Axis 2 — Usability

Time-to-first-value, steps-to-core-action, error recovery, learnability, information scent.

| Score | Standard |
|---|---|
| 5 | Value in the first session without training. Core action in ≤3 steps. Errors are recoverable in place. Navigation is self-evident. |
| 4 | Brief orientation needed; core action efficient; errors explained clearly. |
| 3 | Training or documentation required; core action works but is longer than necessary. |
| 2 | Users develop workarounds and tribal knowledge to operate it. |
| 1 | Requires a dedicated internal expert. |

**Evidence sources:** onboarding walkthroughs, demo videos, teardowns, free trial, review-site complaint themes.

---

## Axis 3 — Visual

Typography system, spatial rhythm, color discipline, density fit for the industry, motion restraint.

| Score | Standard |
|---|---|
| 5 | Coherent type scale, disciplined spacing, color used semantically rather than decoratively, density correct for the industry's use context, motion purposeful. |
| 4 | Systematic and consistent, with minor lapses. |
| 3 | Competent, generic. Looks like the framework's defaults. |
| 2 | Inconsistent spacing, arbitrary color, mismatched density. |
| 1 | Actively hard to look at or read. |

**Note:** density fit is judged against the industry, not in the abstract. A dense operational console scores 5 for the same layout that would score 2 in a consumer app.

**Evidence sources:** public design-system pages, marketing site, screenshot galleries, pattern libraries.

---

## Axis 4 — UX/UI craft

Empty and loading and error states, keyboard and screen-reader support, responsive behavior, microcopy.

| Score | Standard |
|---|---|
| 5 | Every state designed. Full keyboard path. Correct semantics for assistive tech. Genuinely responsive, not just reflowed. Microcopy is specific and helpful. |
| 4 | Most states designed; keyboard support broad; responsive at the main breakpoints. |
| 3 | Happy path polished; empty and error states default or missing. |
| 2 | Visible cracks: spinners with no context, generic errors, broken mobile layouts. |
| 1 | Unhandled states leak raw system behavior to users. |

This axis is the one most likely to be under-scored from marketing materials alone. Trial the product or find a teardown.

**Evidence sources:** hands-on trial, UX teardowns, accessibility audits, mobile screenshots, support forum threads.

---

## Composite

Report the four scores individually; do not average them into a single ranking. The point of the rubric is that different references win on different axes, and the Feature Steal List should take from each where it is strongest. A product scoring 5/2/2/2 is a functionality reference, not a bad product.

## Outlier scoring

The cross-industry outlier is scored on the interaction problem it shares with your product, not on its overall category. Note explicitly which axis it is being consulted for.
