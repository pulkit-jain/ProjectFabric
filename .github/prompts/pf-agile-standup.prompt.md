---
description: Capture a lightweight per-work-package status pulse during a sprint (Agile ceremony layer).
---

# /pf-agile-standup

Act as the `pf-scrum-master` agent. Read `tracker.md` and `sprint-backlog.md`'s current sprint;
append to `.pmo/standup-log.md`.

## Steps

1. For each work package in the current sprint (`sprint-backlog.md`), ask the user (or read
   `tracker.md` if already current) for: done since last standup, in progress, blocked.
2. Append a dated entry to `standup-log.md` using `templates/standup-log.template.md` — keep it
   to a few lines per work package, not a narrative.
3. If a status here conflicts with `tracker.md`, flag it to the user rather than silently editing
   `tracker.md` yourself — that stays the Project Manager's artifact.
4. If any work package is Blocked, tell the user whether it needs `/pf-change-request` (if the
   blocker affects baseline scope/schedule) or just a Project Manager follow-up. Otherwise the
   sprint continues: `/pf-assign-task` for the next eligible work package, or
   `/pf-check-report` when a Team Member has reported.
