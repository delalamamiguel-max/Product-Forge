# Examples

Worked examples live here. The intended first entry is a real product taken end to end — see `docs/PRODUCT-PLAN.md`, implementation step 10.

Until then, `docs/PRODUCT-PLAN.md` is itself a worked example: the PM package for Product Forge, written in Product Forge's own format, with requirements, roadmap, stories, implementation steps, risks, and metrics.

To generate a fresh workspace to inspect:

```bash
./scripts/pf-init.sh sandbox
python3 scripts/pf-validate.py products/sandbox/product-packet.yaml
```

The validator will fail loudly on the empty packet. That is the correct behavior — it demonstrates the gate.
