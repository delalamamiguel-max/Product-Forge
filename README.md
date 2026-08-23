# Product Forge

**An industry-agnostic, agent-native toolkit that automates every product development step *before* handoff to a coding agent.**

Spec Kit starts when you already know what to build. Superpowers starts when you already know what "good" looks like. Product Forge covers the part neither does: grounding a product in its **industry and user**, harvesting **best-in-class references** from the live web across functionality, usability, visual design, and UX/UI, and turning all of it into a traceable spec packet that Claude Code, Codex, Cursor, Copilot, or Gemini CLI can execute without further interpretation.

```
IDEA ──▶ DISCOVER ──▶ BENCHMARK ──▶ SPECIFY ──▶ CLARIFY ──▶ DESIGN ──▶ PLAN ──▶ STORIES ──▶ AUDIT ──▶ HANDOFF ──▶ [coding agent]
         who/where     best-in-class   FR/NFR    ambiguity   UX + DS    arch     backlog     gate     packet
```

---

## Why this exists

| Problem | What Product Forge does |
|---|---|
| Agents build generic software because nobody told them the industry | `/pf.discover` is a **hard gate**. No spec is written until domain, ICP, jobs-to-be-done, regulatory profile, and competitive frame are on paper. |
| Nobody researches what best-in-class looks like | `/pf.benchmark` scans the live web and scores 5–8 reference products on a four-axis rubric, producing a Feature Steal List with citations. |
| "Make it look good" is not a requirement | `/pf.design` derives a real design system — tokens, components, flows — from benchmark evidence, not from taste. |
| Requirements drift from stories drift from code | Every artifact shares one `product-packet.yaml` with stable IDs (`FR-014`, `RULE-FR014-02`, `US-031`). `/pf.audit` fails the build on any orphan. |
| Handoff is a copy-paste of a Google Doc | `/pf.handoff` emits an agent-native packet: Spec Kit-compatible `spec.md` / `plan.md` / `tasks.md`, plus `CLAUDE.md`, `AGENTS.md`, and `.cursor/rules/`. |

---

## Quick start

```bash
# 1. Clone into a new product repo
git clone https://github.com/<you>/product-forge.git my-product
cd my-product && rm -rf .git && git init

# 2. Initialize a product workspace
./scripts/pf-init.sh "clinic-scheduler"

# 3. Open your agent and run the phases in order
/pf.constitution     # non-negotiables for this product
/pf.discover         # HARD GATE: industry, ICP, JTBD, regulatory
/pf.benchmark        # best-in-class scan + scored matrix
/pf.specify          # PRD with FR-nnn / NFR-nnn
/pf.clarify          # kill every [NEEDS CLARIFICATION]
/pf.design           # design system + UX flows from benchmark evidence
/pf.plan             # architecture, stack, data model
/pf.stories          # epics + user stories with Given/When/Then
/pf.audit            # traceability gate — must pass
/pf.handoff          # emit the coding-agent packet
```

Then hand `products/clinic-scheduler/handoff/` to Claude Code, Codex, or Cursor and start building.

---

## What lands on disk

```
products/<slug>/
├── product-packet.yaml          # single source of truth — every ID lives here
├── 00-constitution.md           # non-negotiable principles
├── 01-domain-brief.md           # industry, ICP, JTBD, regulatory, glossary
├── 02-benchmark-report.md       # scored best-in-class matrix + Feature Steal List
├── 03-prd.md                    # FR-nnn / NFR-nnn / RULE-FRnnn-nn
├── 04-design-system.md          # tokens, components, UX flows, a11y baseline
├── 05-architecture-plan.md      # stack, data model, integrations, ADRs
├── 06-backlog.md                # EPIC-nn / US-nnn with acceptance criteria
├── 07-risk-register.md          # RISK-nn with owner, trigger, mitigation
├── 08-metrics-plan.md           # KPI-nn, instrumentation, guardrails
├── 09-roadmap.md                # release slices with entry/exit criteria
└── handoff/
    ├── spec.md                  # Spec Kit-compatible
    ├── plan.md
    ├── tasks.md
    ├── CLAUDE.md
    ├── AGENTS.md
    └── .cursor/rules/product.mdc
```

---

## The four-axis benchmark rubric

Every reference product is scored 1–5 on each axis with a cited justification. No score without a URL.

| Axis | What it measures |
|---|---|
| **Functionality** | Depth of the core job, edge-case coverage, integration surface, data model sophistication |
| **Usability** | Time-to-first-value, steps-to-core-action, error recovery, learnability, information scent |
| **Visual** | Typography system, spatial rhythm, color discipline, density fit for the industry, motion restraint |
| **UX/UI craft** | Empty/loading/error states, keyboard + screen-reader support, responsive behavior, microcopy |

Output is a **Feature Steal List**: every candidate feature carries `BM-nn` provenance, a scored axis, and an in/out decision — so the PRD can cite *why* a feature exists.

See [`rubrics/benchmark-rubric.md`](rubrics/benchmark-rubric.md).

---

## Design lineage

| Borrowed from | What we took | What we changed |
|---|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) | Constitution as a permanent rules file; phase-per-artifact markdown chain; cross-artifact analysis as a gate; agent-neutral command files | Added the pre-spec product layer (discover, benchmark, design) that Spec Kit assumes you did offline |
| [obra/superpowers](https://github.com/obra/superpowers) | `SKILL.md` composable skills; auto-triggering; `<HARD-GATE>` blocks that refuse to proceed; one-question-at-a-time Socratic dialogue; verification-before-completion | Retargeted from code quality to **product quality** — the gates protect requirements integrity, not test coverage |

Product Forge is complementary to both. It ends where Spec Kit's `/speckit.implement` begins.

---

## Agent compatibility

Commands live in `.claude/commands/` and skills in `.claude/skills/`. `scripts/pf-init.sh` mirrors them to `.github/prompts/`, `.codex/`, and `.cursor/rules/` so the same workflow runs on any harness. See [`docs/AGENT-COMPATIBILITY.md`](docs/AGENT-COMPATIBILITY.md).

## Docs

- [Quickstart](docs/QUICKSTART.md) — first product in 30 minutes
- [Workflow](docs/WORKFLOW.md) — every phase, its gate, and its output
- [ID scheme](docs/ID-SCHEME.md) — how traceability actually works
- [Product plan](docs/PRODUCT-PLAN.md) — the PM package for Product Forge itself
- [Agent compatibility](docs/AGENT-COMPATIBILITY.md)

## License

MIT
