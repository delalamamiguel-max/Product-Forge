# Quickstart — your first product in 30 minutes

## Install

```bash
git clone https://github.com/<you>/product-forge.git my-product
cd my-product && rm -rf .git && git init
pip install pyyaml
```

## Initialize

```bash
./scripts/pf-init.sh clinic-scheduler
```

This creates `products/clinic-scheduler/` with all ten artifact templates and an empty `product-packet.yaml`, and mirrors the command files into `.github/prompts/`, `.codex/prompts/`, `.cursor/rules/`, and `.gemini/commands/` so the same workflow runs on any agent.

## Run the phases

Open your agent in the repo root and run in order. Each phase reads the previous artifacts, so don't skip.

| Command | Time | Output |
|---|---|---|
| `/pf.constitution` | 5 min | Non-negotiables |
| `/pf.discover` | 10 min | Domain brief — **the gate that matters most** |
| `/pf.benchmark` | 10 min | Scored matrix + Feature Steal List |
| `/pf.specify` | 10 min | PRD with FR/NFR IDs |
| `/pf.clarify` | 5 min | Every ambiguity resolved |
| `/pf.design` | 10 min | Design system + UX flows |
| `/pf.plan` | 10 min | Architecture + ADRs |
| `/pf.stories` | 10 min | Backlog + roadmap |
| `/pf.audit` | 2 min | PASS/FAIL gate |
| `/pf.handoff` | 2 min | Agent packet |

Thirty minutes is the floor for a small product. A real one takes a few hours across a couple of sessions — still a fraction of the rework it prevents.

## Validate

```bash
python3 scripts/pf-validate.py products/clinic-scheduler/product-packet.yaml
```

Exit 0 = ready for handoff. Wire it into CI to block merges on spec regressions.

## Hand off

```bash
cd products/clinic-scheduler/handoff
claude          # or: codex, cursor .
```

The agent reads `CLAUDE.md` / `AGENTS.md` and starts from `tasks.md`.

## Adding a feature later

```bash
./scripts/pf-new-feature.sh clinic-scheduler waitlist
```

Constitution and domain brief are inherited. You start at `/pf.benchmark`, re-benchmarking only this feature's interaction problem.

## The one habit that matters

**Answer `/pf.discover` honestly and specifically.** Every downstream artifact inherits its precision. "A scheduling app for small businesses" produces a generic calendar. "A scheduling app for 3-provider dermatology practices where a no-show costs $240 and front-desk staff are interrupted every 90 seconds" produces a product.
