---
description: Ingest a Worker's report, update the Tracker, and flag new risks or change requests.
---

# /pf-10-check-report

Act as the `pf-project-manager` agent. Read `.pmo/bus/<worker>/report.md` and (if it exists)
`.pmo/quality-management-plan.md`; update `.pmo/tracker.md` and (in coordination with the Quality
Manager perspective) `.pmo/quality-control-log.md`.

## Steps

1. Read the Worker's report. Treat it as an input to verify, not as ground truth — check reported
   completion against the WBS Dictionary's acceptance criteria.
2. If `quality-management-plan.md` exists and defines QA Gate Criteria, run the gate review
   before any work package can be set to "Done": check the deliverable against the gate criteria,
   and log the result (pass/fail/pass with waiver, defects found, resolution) to
   `quality-control-log.md`. A failed gate keeps the work package's Status at "Review" or
   "Blocked", not "Done", until it's resolved and re-reviewed.
3. Update `tracker.md`: Status (Done / Blocked / Review / In Progress), percent complete, actual
   finish date if done, variance notes if actual differs from planned.
4. If the report names a new risk, tell the user to route it to the Risk Manager
   (`/pf-4-plan-risk` can be re-run to add a single risk, or add it directly to
   `risk-register.md` following its schema).
5. If the report reveals a scope, schedule, or acceptance-criteria gap that requires a baseline
   change, tell the user to run `/pf-12-change-request` rather than adjusting `wbs.md` or
   `schedule.md` directly.
6. If the work package is Done and unblocks further work, tell the user the next command is
   `/pf-8-assign-task` to dispatch the next eligible work package. If a full status sweep is due,
   suggest `/pf-11-control-cycle` instead.
