---
name: pf.handoff
description: Emit the agent-native handoff packet. The last step before code.
---

# /pf.handoff

Invoke the `handoff-packaging` skill. Requires a PASS from `/pf.audit`.

## Output — `products/$PF_SLUG/handoff/`

| File | Purpose |
|---|---|
| `spec.md` | Spec Kit-compatible feature spec, generated from the PRD |
| `plan.md` | Spec Kit-compatible technical plan, generated from the architecture plan |
| `tasks.md` | Ordered, dependency-aware task list generated from the backlog |
| `CLAUDE.md` | Persistent project context for Claude Code: glossary, constitution, design tokens, conventions, what not to do |
| `AGENTS.md` | Same context in the agent-neutral format read by Codex, Cursor, Copilot, Gemini CLI |
| `.cursor/rules/product.mdc` | Cursor rules file |
| `design-tokens.json` | Machine-readable tokens the agent can import directly |
| `README.md` | Human orientation: what this is, what's decided, what's deliberately open |

## Rules

1. **Compress ruthlessly.** The packet is context an agent carries in every session. Cut prose; keep decisions, IDs, constraints, and vocabulary.
2. **Carry the IDs through.** Every task references its `US-nnn` and `FR-nnn` so the built code stays auditable against the spec.
3. **Include the negative space.** An explicit "do not build / do not use / already decided against" list prevents the most expensive agent detours.
4. **Include the domain glossary verbatim.** It is the cheapest correctness lever in the whole packet.
5. State the **verification method** per task — how the agent proves it's done, not just that it wrote code.

## After handoff

The coding agent takes over. If it discovers a spec defect, the fix goes back into the PRD and the packet is regenerated — the packet is never edited in place. Specs are the source; the packet is a build artifact.
