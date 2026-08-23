# Product Plan — Product Forge

The PM package for the toolkit itself, written in its own format. If the framework can't specify itself, it can't specify anything.

---

## 1. Problem

Coding agents are now good enough that implementation is no longer the bottleneck. The bottleneck moved upstream: agents produce technically correct, contextually wrong software because nobody told them the industry, the user, or what excellent looks like in this market.

The existing tools address the half of the problem after the spec exists. Spec Kit structures spec → plan → tasks → implement, but assumes you arrived with a spec. Superpowers enforces discipline during implementation, but its brainstorming skill is a design conversation, not market research. Neither researches the domain, neither benchmarks best-in-class, and neither produces a design system grounded in evidence.

The result is a repeatable failure: three days of agent-built work that runs correctly and solves the wrong problem, at the wrong density, with the wrong vocabulary, missing the two features every competitor has had for five years.

## 2. Product statement

For product managers and technical founders who hand work to coding agents, who need specifications that are specific to their industry rather than generic, **Product Forge** is an agnostic pre-implementation toolkit that grounds a product in its domain, benchmarks best-in-class references from the live web across four axes, and emits a traceable handoff packet — unlike Spec Kit and Superpowers, which begin after those decisions are already made.

## 3. Scope

**In scope**
- Ten-phase workflow from idea to agent handoff
- Hard gates that refuse to proceed on missing domain or benchmark grounding
- Live-web benchmarking with a four-axis scored rubric
- Design system derivation from benchmark evidence
- Stable-ID traceability enforced by a CI-runnable validator
- Handoff packets for Claude Code, Codex, Cursor, Copilot, Gemini CLI
- Reusable across any industry and any product type

**Out of scope (permanent)**
- Writing implementation code — that is the coding agent's job
- Hosting, project management, or ticketing integrations
- Being a Spec Kit replacement — it is a complement
- Opinions about stack beyond what a product's own constitution declares

**Deferred**

| Item | Condition that pulls it in |
|---|---|
| Jira / Linear export from `06-backlog.md` | Second user asks; the packet schema already supports it |
| Screenshot capture during benchmarking | A stable headless-browser path exists in the target environments |
| Multi-product portfolio view | Three or more products under management in one repo |
| Web UI over the packet | The CLI workflow proves sticky for 90 days first |

## 4. Requirements

### Functional

| ID | Requirement | Traces to |
|---|---|---|
| FR-001 | The workflow blocks all downstream phases until a domain brief names a specific sub-vertical, distinguishes user from buyer, and states a regulatory answer explicitly | Original bet: specificity at phase 1 is the dominant quality lever |
| FR-002 | Benchmarking researches the live web and scores each reference 1–5 on functionality, usability, visual, and UX/UI craft, with a cited URL per score | Original bet: uncited scores are recalled, not researched, and models' product knowledge decays quarterly |
| FR-003 | The reference set includes at least one cross-industry outlier solving the same interaction problem | Benchmarking practice; the outlier is where differentiation originates |
| FR-004 | Every Feature Steal List row carries an explicit IN / OUT / LATER decision before the PRD may be written | Undecided rows reappear as scope creep at 20× the cost |
| FR-005 | Every requirement, story, component, flow, risk, and metric carries a stable ID that is never renumbered or reused | Spec Kit traceability practice |
| FR-006 | Every component specification defines nine states: default, hover, focus-visible, active, disabled, loading, empty, error, overflow | Missing states are the top cause of unfinished-looking agent UI |
| FR-007 | The validator blocks handoff on any failed traceability, coverage, or quality check, and reports offending IDs plus a remediation | Superpowers verification-before-completion |
| FR-008 | The handoff packet is emitted in Spec Kit-compatible form plus agent-neutral context files | Interoperability, not replacement |
| FR-009 | The toolkit carries no industry-specific content; all domain knowledge enters at `/pf.discover` | Agnosticism is the core constraint |
| FR-010 | Adding a feature to an existing product inherits the constitution and domain brief and restarts at benchmarking | Re-running discovery per feature is waste |

### Non-functional

| ID | Requirement | Measurement |
|---|---|---|
| NFR-001 | Full workflow completable in under 3 hours for a medium product | Timed dogfood run |
| NFR-002 | Validator runs in under 5 seconds on a 200-requirement packet | `time python3 scripts/pf-validate.py` |
| NFR-003 | Handoff packet under 8,000 tokens so it reloads every session without crowding the working set | Token count at generation |
| NFR-004 | Zero runtime dependencies beyond Python 3.11 and pyyaml | `pip list` after clean install |
| NFR-005 | Every command file readable and executable by a harness with no plugin support | Manual run on 3 harnesses |

## 5. Roadmap

### Slice 1 — One product taken end to end (this release)
**Outcome:** A user takes a real product idea from a sentence to a handoff packet a coding agent builds from without asking clarifying questions.
- Ten commands, seven skills, ten templates, packet schema, validator, agent mirroring
- **Entry:** repo cloned
- **Exit:** one real product completed end to end; agent builds slice 1 with zero spec questions
- **Moves:** KPI-01, KPI-02

### Slice 2 — Sharpen the benchmark
**Outcome:** Benchmark reports are good enough to circulate to stakeholders unedited.
- Worked example benchmark in `examples/`, per-industry reference-source hints, richer visual-pattern extraction
- **Entry:** slice 1 exit met on two products
- **Exit:** a benchmark report shared with a stakeholder without edits
- **Moves:** KPI-03

### Slice 3 — CI enforcement
**Outcome:** Spec regressions are caught by machine, not by memory.
- GitHub Action running the validator, packet diffing between commits, drift detection against shipped code
- **Entry:** slice 2 complete
- **Exit:** a PR blocked by a real spec regression
- **Moves:** KPI-04

### Slice 4 — Portfolio
**Outcome:** Multiple products managed from one repo without artifact collision.
- Cross-product pattern reuse, shared constitution inheritance, portfolio dashboard
- **Entry:** three products under management
- **Exit:** a decision made using cross-product data

## 6. Representative stories

**US-001 — Refuse a generic domain**
As a PM in a hurry, when I answer "small businesses" to the industry question, I want the agent to push back and ask which trade and which revenue band, so that I don't get a generic product.
```
GIVEN /pf.discover has asked for the sub-vertical
WHEN the user answers with a generic category
THEN the agent names why it is insufficient and asks a narrower question
GIVEN the user insists after two attempts (edge)
WHEN they ask to proceed anyway
THEN the agent records the ambiguity as RISK-nn with an owner and proceeds
GIVEN the validator later runs (failure)
WHEN sub_vertical is generic
THEN the check fails and blocks handoff
```
Traces to: FR-001 · Verification: `pf-validate.py` GENERIC list test

**US-002 — Benchmark with citations**
As a PM, I want every benchmark score backed by a URL, so that I can defend the scope decisions to stakeholders and re-verify them in six months.
```
GIVEN /pf.benchmark has produced a scored matrix
WHEN any axis score lacks a source URL
THEN the validator fails with the offending BM IDs
```
Traces to: FR-002 · Verification: validator uncited-score check

**US-003 — Block handoff on an orphan story**
As a tech lead, I want stories that trace to no requirement to fail the audit, so that scope creep is caught before implementation rather than in review.
```
GIVEN a story with no traces_to intersecting the requirement set
WHEN /pf.audit runs
THEN the check fails, names the story, and recommends finding its FR or deleting it
```
Traces to: FR-005, FR-007 · Verification: validator orphan check

**US-004 — Nine states or it isn't specified**
As a PM, I want components without empty, loading, and error states to fail the audit, so that agent-built UI doesn't invent them inconsistently in nine places.
```
GIVEN a component in the packet missing any of the nine states
WHEN /pf.audit runs
THEN the check fails and names the component
```
Traces to: FR-006 · Verification: validator NINE-state check

## 7. Implementation steps

| # | Step | Output | Done when |
|---|---|---|---|
| 1 | Repo scaffold, license, README | Structure | `pf-init.sh` runs clean |
| 2 | Command files, all ten phases | `.claude/commands/` | Each is standalone-executable by an agent |
| 3 | Skill files with hard gates | `.claude/skills/` | Gates verifiably refuse to proceed |
| 4 | Artifact templates | `templates/` | Every template ID-ready |
| 5 | Packet schema | `schemas/` | Covers every artifact's IDs |
| 6 | Validator with 28 checks | `scripts/pf-validate.py` | Empty packet at a late phase fails loudly |
| 7 | Benchmark rubric | `rubrics/` | Four axes, anchored 1–5 descriptors |
| 8 | Agent mirroring | `pf-init.sh` | Five harness paths populated |
| 9 | Docs | `docs/` | A stranger can run it unaided |
| 10 | **Dogfood on a real product** | `examples/` | Agent builds slice 1 with zero spec questions |
| 11 | CI action | `.github/workflows/` | Validator blocks a real regression |

Step 10 is the real acceptance test. Everything before it is scaffolding.

## 8. Risks

| ID | Risk | L | I | Observable trigger | Mitigation | Contingency |
|---|---|---|---|---|---|---|
| RISK-01 | Process is heavy enough that it gets skipped under deadline | H | H | A product ships without a packet | Reduced path documented; discover is the only unskippable phase | Ship a `/pf.express` three-phase variant |
| RISK-02 | Benchmark research returns thin or stale results in low-visibility verticals | M | M | Fewer than 3 references found | Adjacent-market and outlier references are required, not optional | Practitioner-interview fallback path in the skill |
| RISK-03 | Hard gates become friction users route around by prompting past them | M | H | Users invoke phases out of order | Gates cite the specific downstream cost, not just "you must" | Validator catches skipped phases regardless of how the artifact was produced |
| RISK-04 | Spec Kit or Superpowers absorbs this layer | M | M | Either ships domain/benchmark phases | Stay complementary; keep the handoff Spec Kit-compatible | Contribute the layer upstream as an extension |
| RISK-05 | Packet grows past the point where agents can carry it | M | M | Handoff exceeds 8k tokens | NFR-003 with compression rules in the packaging skill | Split into always-loaded core and on-demand reference |
| RISK-06 | Traceability becomes bookkeeping nobody maintains | M | H | IDs drift out of the packet | Validator enforces; agents write the IDs, not humans | Auto-derive packet entries from the markdown artifacts |
| RISK-07 | Four-axis scoring is applied inconsistently across sessions | M | L | Same product scored differently twice | Anchored 1–5 descriptors; justification written before the number | Add a worked scoring example to the rubric |

## 9. Success metrics

**North star:** proportion of agent-built features accepted without a spec-driven rework cycle. Baseline before adoption: measure on the next three features.

| ID | Metric | Target | Window | Instrumentation |
|---|---|---|---|---|
| KPI-01 | Clarifying questions the coding agent asks during slice 1 | ≤ 2 | Per product | Count in the implementation session |
| KPI-02 | Rework cycles caused by spec ambiguity | ≤ 1 per slice | Per slice | Tagged commits / session notes |
| KPI-03 | Requirements traceable to a DOM or BM parent | 100% | Per audit | Validator output |
| KPI-04 | Time from idea to audited handoff packet | < 3 hours, medium product | Per product | Wall clock |
| KPI-05 | Products reusing the toolkit without modifying it | ≥ 3 across ≥ 2 industries | 90 days | Repo count |

**Guardrails**

| ID | Guardrail | Threshold | Action if breached |
|---|---|---|---|
| GRD-01 | Time spent in pre-implementation | Must stay under 25% of total delivery time | Cut phases, not depth within phases |
| GRD-02 | Handoff packet size | 8,000 tokens | Compress; move detail to on-demand reference |
| GRD-03 | Validator false-failure rate | < 5% of runs | Loosen the specific check; never disable the gate |

## 10. Open questions

1. Should `/pf.benchmark` cache reference data across products in the same vertical? Saves time; risks staleness, which is the exact failure mode the phase exists to prevent. **Recommendation: no cache, but a `benchmarked_on` date on every reference so staleness is visible.**
2. Does the validator belong in CI or as a pre-handoff manual gate? **Recommendation: both — manual during authoring, CI at merge, same script.**
3. Should the constitution be shared across a portfolio? **Recommendation: yes, with per-product override, once slice 4 exists. Not before.**
