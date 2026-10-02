---
description: Archive a completed stage's history out of the live .pmo/ folders and leave a stage summary in its place.
---

# /pf-session-archive-stage

Act as the `pf-project-manager` agent. Read `tracker.md`, `memory/work-packages/`, `bus/`,
`reports/`, and (if it exists) `standup-log.md` and `sprint-backlog.md`; write
`.pmo/archives/<stage>/stage-summary.md`.

Use this once a stage (a sprint, a milestone, or a phase) is finished and its history is
inflating what agents must read. Never archive a baseline document, a register, `changes/`, or
`decisions/` — those stay live. This is only for finished, work-package-level history.

Moving files is done from the terminal, and only after the user approves the exact list —
consistent with the user being the checkpoint. Nothing is ever deleted.

## Steps

1. Ask the user for the stage label (e.g. `sprint-3`, `milestone-1`) and which work packages it
   covers.
2. Confirm every one of those work packages is "Done" in `tracker.md`. If the Agile ceremony layer
   is in use, also confirm each is "Accepted" in `sprint-backlog.md`'s Sprint Review Outcome. If
   any is not, stop and say which — do not archive unfinished work.
3. Build the candidate list, only for those work packages:
   - `memory/work-packages/WP-<id>.md`
   - `bus/<member>/task.md` and `bus/<member>/report.md` (only if that Team Member has no work package
     still in progress)
   - `reports/status-<date>.md` dated within the stage, except the most recent report (the next
     control cycle compares against it, and it describes work that is still open)
   - the stage's dated entries in `standup-log.md`, if present
4. Write `archives/<stage>/stage-summary.md` from `templates/stage-summary.template.md` with Move
   Status "Pending", using facts from the files above and `tracker.md` — do not invent outcomes.
   List every candidate under Archived Files with its target path under `archives/<stage>/`.
5. Present the candidate list to the user. Once they approve it, create the target folders and
   run `git mv <original> <archived>` per file (a plain move if `.pmo/` isn't in git). If you
   can't run terminal commands, give the user the same command block and wait for them to confirm
   it's done. Standup-log entries can't be moved by command; ask the user whether to leave them or
   have you copy them to `archives/<stage>/standup-log.md` and cut them from the live file.
6. Once the moves are done, use search to verify each original is gone and each archived path
   exists. Only then set the summary's Move Status to "Done".
7. Tell the user the next command — `/pf-assign-task` to continue the loop, or
   `/pf-agile-sprint-planning` if the Agile ceremony layer is in use.
