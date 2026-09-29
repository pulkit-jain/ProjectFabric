---
description: Capture what went well, what didn't, and action items at a sprint boundary (Agile ceremony layer).
---

# /pf-11b-sprint-retro

Act as the `pf-scrum-master` agent. Read `standup-log.md` and `tracker.md` for the sprint just
ended; append to `.pmo/retro-log.md`.

## Steps

1. Ask the user (or infer from `standup-log.md`/`tracker.md`) what went well, what didn't, and
   any action items for the sprint just ended.
2. Append a dated Sprint Retro section to `retro-log.md` using
   `templates/retro-log.template.md`, with action items in a table (Action / Owner / Status).
3. If an action item requires a scope, schedule, or budget change, tell the user
   `/pf-12-change-request` is needed rather than editing baseline documents directly.
4. Tell the user the retro is logged and, if the project is continuing, the next ceremony is
   `/pf-7b-sprint-planning` for the next sprint.
