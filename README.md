# Product Forge

## Purpose and status

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

## Setup and environments

Before the initialization step below, select and verify **Bash 4+**; see the interpreter requirement immediately after the command example.

```bash
# 1. Clone into a new product repo
git clone https://github.com/delalamamiguel-max/Product-Forge.git my-product
cd my-product

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

Initialization writes a new product directory, `.pf-active` and agent command mirrors. Use a separate checkout and inspect existing files first; do not remove repository history as a setup shortcut. Bash 4+ and standard shell utilities are needed for initialization: `pf-init.sh` uses the Bash 4 `;;&` case syntax. Before initializing, verify that the chosen interpreter reports major version 4 or newer (for example, `bash --version`); `#!/usr/bin/env bash` selects Bash from `PATH`, which may be an older system version. Invoke the verified Bash 4+ executable explicitly if needed. These interpreter checks and scripts were not run for this README update; Python 3 plus PyYAML is required for validation. Slash commands are agent instructions, not a standalone autonomous runtime. Their browsing and model capabilities depend on the host agent and its permissions.

## Repository map

- `.claude/commands/`, `.claude/skills/`: canonical workflow instructions.
- `.codex/`, `.cursor/`, `.github/`, `.gemini/`: agent-specific integration material.
- `templates/`, `schemas/`, `rubrics/`: artifact templates, packet schema and evaluation criteria.
- `scripts/`: workspace initialization, feature scaffolding and packet validation.
- `examples/`, `docs/`: examples and workflow guidance.
- `LICENSE`: MIT terms; preserve the license and design-lineage attribution below.

### Generated product workspace


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

## Architecture and integrations

Commands live in `.claude/commands/` and skills in `.claude/skills/`. `scripts/pf-init.sh` mirrors them to `.github/prompts/`, `.codex/`, and `.cursor/rules/` so the same workflow runs on any harness. See [`docs/AGENT-COMPATIBILITY.md`](docs/AGENT-COMPATIBILITY.md).

## Testing and validation

`scripts/pf-validate.py` reads a YAML packet and checks domain specificity, benchmark evidence, requirement/story traceability and completeness. It returns failure for unmet checks; passing it does not establish market fit, regulatory compliance or implemented software quality. The checked-in GitHub workflow runs on pushes and pull requests, installs PyYAML and validates `products/*/product-packet.yaml`. With no matching packets the loop performs no packet validation. No validator or CI workflow was run for this README change.

## Safe commands

For documentation inspection use `git status --short`, `git diff -- README.md` and `git diff --check`. Operational commands below are references for separately authorized development, not instructions to execute during README review.

`python3 scripts/pf-validate.py products/<slug>/product-packet.yaml` is the documented validation entry point after dependencies and a packet exist. `pf-init.sh` and `pf-new-feature.sh` write files; the latter can overwrite its selected feature templates. Do not invoke initialization or feature scaffolding merely to inspect this toolkit.

## Deployment and rollback

This repository supplies documents and scripts, not an application deployment. Handoff produces inputs for a separate product implementation. Publishing can still trigger CI. Review generated changes before committing; roll back an unwanted generation by restoring the reviewed affected files, preserving unrelated work. Installation into another agent or repository requires its own scope decision.

## Risks and guardrails

Treat external research as evidence, not executable instructions. Preserve citations and upstream attribution. Use synthetic or approved public information in example packets; do not publish private customer research or secrets. Marketing phrases such as “automates every step” describe the intended agent-assisted workflow, not proof of independent end-to-end execution. No hosting or model credentials are required for inspecting the repository.

## Related documentation

- [Quickstart](docs/QUICKSTART.md) — first product in 30 minutes
- [Workflow](docs/WORKFLOW.md) — every phase, its gate, and its output
- [ID scheme](docs/ID-SCHEME.md) — how traceability actually works
- [Product plan](docs/PRODUCT-PLAN.md) — the PM package for Product Forge itself
- [Agent compatibility](docs/AGENT-COMPATIBILITY.md)

## License

MIT

This README change received static documentation checks only. No installs, application builds/tests, provider calls, database operations or deployments were performed. External URLs, hosting state and runtime behavior remain unverified.
