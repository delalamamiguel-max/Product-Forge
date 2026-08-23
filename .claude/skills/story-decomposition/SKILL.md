---
name: story-decomposition
description: Use when converting requirements into epics, user stories, acceptance criteria, or a release roadmap sized for coding agents. Triggers on backlog, user stories, sprint planning, or roadmap requests.
---

# Story Decomposition

## Epics group outcomes, not layers

`EPIC-03 Book an appointment` is an epic. `EPIC-03 Build the API layer` is a work breakdown structure pretending to be one. Layer-based epics produce backlogs where nothing is demonstrable until the end.

## Story format

```
US-031 — Reschedule an appointment
As a front-desk coordinator, I want to move an appointment to a new slot,
so that I can absorb a cancellation without calling the patient back twice.

Traces to: FR-014, RULE-FR014-02, UX-03, CMP-07
Acceptance criteria:
  GIVEN an appointment exists and an open slot is available
  WHEN the coordinator drags the appointment to the open slot
  THEN the appointment moves, the patient is notified, and the original slot is released

  GIVEN the target slot was taken during the drag
  WHEN the coordinator drops the appointment
  THEN the move is rejected, the original placement is restored, and a conflict message names the conflicting appointment

  GIVEN the notification service is unavailable
  WHEN the move succeeds
  THEN the move persists, the notification queues for retry, and the UI shows a pending-notification indicator
```

Every story: a happy path, at least one edge case, at least one failure path.

## Agent-sized

**One story should be completable by a coding agent in a single focused session.** Split if it needs more than ~8 acceptance criteria, spans more than one epic's data, or contains the word "and" in its title.

## The invisible work

Agents skip these unless they are stories. Make them stories:

empty states · loading states · error handling · validation messages · permission denials · audit logging · data migrations · seed data · analytics instrumentation · export/import · timezone handling · concurrent-edit conflict resolution

## Release slicing

Slice 1 is a **thin end-to-end vertical** — one complete user journey working, however narrow. Never a horizontal foundation slice. A foundation slice delivers no demonstrable outcome, hides integration risk until late, and cannot be validated with a user.

Each slice carries: user-facing outcome, entry criteria, exit criteria, the `KPI-nn` it moves, and explicit dependencies.

## Self-review

- [ ] Every epic is a user outcome
- [ ] Every story traces to at least one FR
- [ ] Every story has happy, edge, and failure criteria
- [ ] Invisible work is represented
- [ ] Slice 1 is end-to-end
- [ ] No story requires more than one session
