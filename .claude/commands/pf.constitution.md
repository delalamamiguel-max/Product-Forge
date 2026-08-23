---
name: pf.constitution
description: Establish the non-negotiable principles governing this product. Run once, first.
---

# /pf.constitution

Create or amend `products/$PF_SLUG/00-constitution.md` from `templates/00-constitution.md`.

The constitution is the permanent rules file. Every later phase re-reads it and must not contradict it.

## Process

1. Read `templates/00-constitution.md`.
2. Ask the user, **one question at a time**, for anything not supplied:
   - What must always be true of this product? (e.g. "works offline", "no PII leaves the tenant")
   - What is explicitly out of scope, forever?
   - Quality floor: accessibility target, performance budget, browser/device support
   - Stack constraints the org has already locked
   - Compliance regime, if any (HIPAA, SOC 2, FedRAMP, PCI-DSS, GDPR, WCAG level)
3. Write each principle as a testable statement, not an aspiration.
   - Bad: "The app should be fast."
   - Good: "P95 interactive response under 200ms on a mid-tier Android device over 4G."
4. Assign IDs `PRIN-01`…`PRIN-nn`. Register them in `product-packet.yaml` under `constitution.principles`.

## Output

`products/$PF_SLUG/00-constitution.md` + packet entries.

<HARD-GATE>
Do NOT proceed to /pf.discover until the user has read back and approved the principle list.
A constitution written without the user's confirmation is a guess, and every downstream artifact inherits the guess.
</HARD-GATE>
