---
description: Ingest a Team Member's report, update the Tracker, and flag new risks or change requests.
---

# /pf-check-report

Act as the `pf-project-manager` agent. Read `.pmo/bus/<member>/report.md` and (if it exists)
`.pmo/quality-management-plan.md`; update `.pmo/tracker.md` and (in coordination with the Quality
Manager perspective) `.pmo/quality-control-log.md`.

## Steps

1. Read the Team Member's report. Treat it as an input to verify, not as ground truth — check reported
   completion against the WBS Dictionary's acceptance criteria. A Person or Vendor member has no
   `report.md`; ask the user for their status and treat it the same way.
2. If `quality-management-plan.md` exists and defines QA Gate Criteria, run the gate review
   before any work package can be set to "Done": check the deliverable against the gate criteria,
   and log the result (pass/fail/pass with waiver, defects found, resolution) to
   `quality-control-log.md`. A failed gate keeps the work package's Status at "Review" or
   "Blocked", not "Done", until it's resolved and re-reviewed.
3. Update `tracker.md`: Status (Done / Blocked / Review / In Progress), percent complete, actual
   finish date if done, variance notes if actual differs from planned. Set "Done" only when every
   row of the Definition of Done table in `work-package-definitions.md` passes; otherwise
   keep the work package at Review, In Progress or Blocked and tell the user which row failed.
4. If the report names a new risk, tell the user to route it to the Risk Manager
   (`/pf-plan-risk` can be re-run to add a single risk, or add it directly to
   `risk-register.md` following its schema).
5. If the report reveals a scope, schedule, or acceptance-criteria gap that requires a baseline
   change, tell the user to run `/pf-change-request` rather than adjusting `wbs.md` or
   `schedule.md` directly.
6. If the work package is Done and unblocks further work, tell the user the next command is
   `/pf-assign-task` to dispatch the next eligible work package. If a full status sweep is due,
   suggest `/pf-control-cycle` instead. If this project is running the Agile ceremony layer and
   the sprint's work packages are all Done, suggest `/pf-agile-sprint-review` before the retro.
