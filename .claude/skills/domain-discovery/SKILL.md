---
name: domain-discovery
description: Use BEFORE any product work — specifying, designing, planning, or building. Establishes the industry, sub-vertical, ICP, jobs-to-be-done, regulatory profile, and operating constraints that make a product specific rather than generic. Triggers on any new product idea, feature concept, or "build me a..." request.
---

# Domain Discovery

Turn a product idea into a grounded domain brief through one-question-at-a-time dialogue.

<HARD-GATE>
You MUST NOT write requirements, propose an architecture, choose a stack, design a UI, or scaffold a project until this skill has produced an approved domain brief.
This applies to EVERY product regardless of perceived simplicity — a "simple internal tool" for a hospital and for a skate shop are different products, and the difference lives entirely in this phase.
</HARD-GATE>

## Method

**One question at a time.** Batched questions get batched, shallow answers. Wait for each response before forming the next question — the next question should depend on the last answer.

**Refuse abstraction.** If the answer is "healthcare," ask which setting, which practice size, which staff role. If it's "small businesses," ask which trade, which revenue band, which state of digital maturity. Keep pushing until the answer would let a stranger picture a specific person at a specific desk.

**Separate user from buyer.** In B2B they are almost never the same, and they want different things. The user wants fewer clicks; the buyer wants a report. Both shape the spec.

**Mine the current alternative.** What someone does today — including the spreadsheet, the group text, the clipboard — is the highest-signal requirements source available. Ask what they love about it, not just what they hate. The loved parts are the ones you must not break.

**Surface constraints early.** Offline operation, shared devices, gloves, sunlight, interruption, one-handed use, and 15-year-old browsers are all cheap to design for up front and brutal to retrofit.

## Regulatory sweep

Always ask explicitly, and record "none identified" as an answer rather than leaving it blank. Common triggers: health data (HIPAA), payment data (PCI-DSS), student records (FERPA), EU residents (GDPR), consumer credit (FCRA), federal contracting (FAR/FedRAMP/CUI), children (COPPA), accessibility mandates for public entities (Section 508 / WCAG).

## Glossary

Produce 10–20 domain terms an outsider would get wrong, with definitions and — importantly — the terms you must **avoid** because they mean something else in this industry. This glossary propagates to the PRD, the UI microcopy, and the coding agent's context file. It is the cheapest accuracy lever in the entire process.

## Output contract

`01-domain-brief.md` with `DOM-nn` IDs, plus `domain.*` populated in `product-packet.yaml`, plus the 3–8 benchmark candidates that `/pf.benchmark` will investigate.

## Self-review

- [ ] Sub-vertical named, not just industry
- [ ] Primary user distinguished from buyer
- [ ] JTBD phrased in the user's words, not product-speak
- [ ] Current alternative documented including what works about it
- [ ] Regulatory answer explicit
- [ ] Glossary written
- [ ] Benchmark candidates include one adjacent-industry outlier
- [ ] User has approved
