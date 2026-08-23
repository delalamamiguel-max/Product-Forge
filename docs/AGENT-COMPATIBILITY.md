# Agent Compatibility

Product Forge is harness-neutral. Commands are plain markdown; skills use the open `SKILL.md` format.

## Where files go

| Agent | Commands | Skills | Context file |
|---|---|---|---|
| Claude Code | `.claude/commands/` | `.claude/skills/` | `CLAUDE.md` |
| Codex | `.codex/prompts/` | `.codex/skills/` | `AGENTS.md` |
| Cursor | `.cursor/rules/*.mdc` | — | `AGENTS.md` |
| GitHub Copilot | `.github/prompts/*.prompt.md` | — | `AGENTS.md` |
| Gemini CLI | `.gemini/commands/` | — | `AGENTS.md` |
| Anything else | invoke by reading the file | — | `AGENTS.md` |

`./scripts/pf-init.sh <slug> [agent]` mirrors the command files into all of these. Pass a specific agent to mirror only one.

## Invocation

Slash-command syntax varies (`/pf.discover`, `$pf-discover`, `/skill:pf-discover`). All harnesses also accept conversational invocation: *"Use the domain-discovery skill to work through this idea."* The steps are identical either way.

## Skills-mode harnesses

Agents that read `SKILL.md` (Claude Code, Codex) get auto-triggering: describing a new product idea activates `domain-discovery` without an explicit command. Agents without skills support need the explicit command — the frontmatter `description` fields are written so that either path works.

## Relationship to Spec Kit

Product Forge ends where Spec Kit begins. `/pf.handoff` emits `spec.md`, `plan.md`, and `tasks.md` in Spec Kit-compatible form, so you can run:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init . --integration claude
cp products/<slug>/handoff/{spec,plan,tasks}.md specs/001-<slug>/
/speckit.implement
```

Or skip Spec Kit entirely and point a coding agent at the handoff directory. Both work; the packet is designed for either.

## Relationship to Superpowers

Superpowers governs **how code gets written** — TDD, systematic debugging, verification before completion. Product Forge governs **what gets specified**. Install both: Product Forge takes the idea to a handoff packet, Superpowers takes the packet to verified code. Their gates don't overlap and don't conflict.
