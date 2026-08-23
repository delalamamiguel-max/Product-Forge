---
name: handoff-packaging
description: Use when packaging a completed product spec for a coding agent (Claude Code, Codex, Cursor, Copilot, Gemini CLI). Generates Spec Kit-compatible artifacts plus agent context files. Triggers on handoff, hand this to Claude Code, package the spec, or ready for implementation.
---

# Handoff Packaging

Convert the product artifacts into context a coding agent carries in every session.

## Compression principle

The packet enters the agent's context on every turn. Prose is expensive and low-signal. Keep **decisions, IDs, constraints, and vocabulary**; cut narrative, justification, and history. The full artifacts remain in the repo for humans; the packet is for the machine.

Target: the packet should be readable in under five minutes and reloadable in every session without crowding out the working set.

## Files

**`spec.md` / `plan.md` / `tasks.md`** — Spec Kit-compatible, so the packet drops into a `/speckit.*` workflow directly. Tasks are ordered, dependency-aware, and each carries its `US-nnn` and `FR-nnn`.

**`CLAUDE.md` / `AGENTS.md`** — same content, two formats. Contains:
1. One-paragraph product statement
2. **Domain glossary, verbatim** — the cheapest correctness lever available
3. Constitution principles as hard rules
4. Design tokens and the component state contract
5. Conventions: naming, file layout, testing expectations
6. **The negative space** — do not build, do not use, already decided against, with reasons

**`design-tokens.json`** — machine-readable, imported directly rather than transcribed.

**`.cursor/rules/product.mdc`** — Cursor rules format.

## The negative space

The most valuable section and the most often omitted. An explicit "already decided against" list with reasons prevents the expensive agent detour where it re-derives a rejected approach, implements it, and you discover it in review.

## Verification per task

Each task states **how the agent proves it's done** — the command to run, the state to observe, the criterion to check. "Implement the reschedule flow" without a verification method returns as "done" whether or not it works.

## Regeneration, not editing

If the agent finds a spec defect, fix the **source artifact** and regenerate the packet. The packet is a build output. Editing it in place forks the truth, and the fork is discovered three weeks later.
