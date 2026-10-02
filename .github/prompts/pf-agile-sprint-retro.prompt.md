---
description: Capture what went well, what didn't, and action items at a sprint boundary (Agile ceremony layer).
---

# /pf-agile-sprint-retro

Act as the `pf-scrum-master` agent. Read `standup-log.md`, `tracker.md`, and `sprint-backlog.md`'s
Sprint Review Outcomes for the sprint just ended; append to `.pmo/retro-log.md`.

## Steps

1. If `/pf-agile-sprint-review` hasn't run yet for this sprint, tell the user to run it first —
   retro reflects on the process, review accepts the product; do the review first.
2. Ask the user (or infer from `standup-log.md`/`tracker.md`/Sprint Review outcomes) what went
   well, what didn't, and any action items for the sprint just ended.
3. Append a dated Sprint Retro section to `retro-log.md` using
   `templates/retro-log.template.md`, with action items in a table (Action / Owner / Status).
4. If an action item requires a scope, schedule, or budget change, tell the user
   `/pf-change-request` is needed rather than editing baseline documents directly.
5. Tell the user the retro is logged and, if the project is continuing, the next ceremony is
   `/pf-agile-sprint-planning` for the next sprint. If this sprint's history is bloating `.pmo/`,
   suggest `/pf-session-archive-stage` first.
