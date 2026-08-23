---
name: pf.discover
description: Drill down on who this product is for and what industry it lives in. The mandatory first product gate.
---

# /pf.discover

Invoke the `domain-discovery` skill. Produce `products/$PF_SLUG/01-domain-brief.md` from `templates/01-domain-brief.md`.

## Why this is a gate

An agent handed "build a scheduling app" builds a generic calendar. An agent handed "build a scheduling app for a 3-provider dermatology clinic in the US, where no-shows cost $240 each, staff are non-technical, and PHI is in scope" builds a different, correct product. This phase manufactures that difference.

## Process

Ask **one question at a time**. Do not batch. Do not accept "you decide" on the first four.

1. **Industry & sub-vertical** — not "healthcare" but "outpatient dermatology, private practice, 1–5 providers"
2. **Primary user** — role, daily context, technical fluency, device, hands-free/interrupted?
3. **Secondary users & the buyer** — who signs the check is often not who uses it
4. **Job to be done** — the functional, emotional, and social job, in the user's own words
5. **Current alternative** — what they do today, including spreadsheets, paper, and "nothing"
6. **Trigger & frequency** — what makes someone open this, and how often
7. **Success in the user's terms** — what has to change in their week
8. **Regulatory & data sensitivity** — PHI, PII, PCI, FERPA, ITAR, export control, records retention
9. **Operating constraints** — offline, shared devices, kiosk, low bandwidth, gloves, sunlight, noise
10. **Competitive frame** — the 3–8 products you will benchmark next, plus one adjacent-industry outlier

Then produce a **domain glossary** (`DOM-nn`): the 10–20 terms an outsider would get wrong. This glossary is inherited by every later artifact and by the coding agent.

## Output

- `01-domain-brief.md` with `DOM-nn` findings and glossary
- `product-packet.yaml` populated: `domain.industry`, `domain.icp`, `domain.jtbd`, `domain.regulatory`, `domain.constraints`, `domain.benchmark_candidates`

<HARD-GATE>
Do NOT invoke /pf.benchmark, /pf.specify, or any design or implementation skill until:
(a) industry AND sub-vertical are named specifically,
(b) primary user and buyer are distinguished,
(c) the regulatory profile is explicit — including an explicit "none identified",
(d) the user has approved the brief.
"Generic B2B SaaS" is not an industry. Push back and ask again.
</HARD-GATE>
