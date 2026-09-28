---
description: Raise a scope/schedule/risk-driven Change Request with impact analysis for user approval.
---

# /pf-12-change-request

Act as the `pf-project-manager` agent. Produce `.pmo/changes/CR-<id>.md`.

## Steps

1. Capture the trigger: what happened (Worker report, risk realized, stakeholder request,
   external event) and why it requires a baseline change.
2. Write the impact analysis across every affected dimension: scope (which WBS elements),
   schedule (which milestones/dependencies), risk (does this open or close any register entries),
   quality (does the acceptance criteria need to change). Do not skip a dimension — state "No
   impact" explicitly if true.
3. Present 2–3 options where feasible (e.g., absorb within existing schedule vs. extend a
   milestone vs. reduce scope elsewhere), with a recommendation.
4. Record the user's decision (Approved / Rejected / Deferred), approver, and date.
5. If approved: update the specific baseline document(s) — `wbs.md`, `schedule.md`, or
   `scope-statement.md` — and note in the CR which sections changed. This is the only prompt
   allowed to modify those files after Planning is baselined.
6. Tell the user to resume the assign/report loop with `/pf-8-assign-task` or `/pf-11-control-cycle`.
