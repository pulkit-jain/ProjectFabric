# Work Package Definitions

<!-- The checks every work package goes through: when it is ready to be assigned (Definition of Ready)
and when it can be set to Done (Definition of Done). Owned by the Planner; /pf-setup-init pass 2 creates
this file with the framework's standard rows, and /pf-setup-project-constitution lets the project add,
change or drop rows. Treat as baseline once approved; to add, change or drop a row afterwards, use
/pf-change-request and note the reason in Amendments. Project-level agreements are in
project-constitution.md. -->

## Definition of Ready

<!-- The checks a work package must pass before /pf-assign-task dispatches it. /pf-assign-task and
/pf-agile-backlog-refinement run every row. Add a row for a check specific to this project (and name
who fixes a failure). -->

| # | Check | If it fails, goes to |
|---|---|---|
| 1 | The WBS Dictionary gives the work package testable acceptance criteria. | Planner |
| 2 | `raci.md` names a Responsible party (a Team Member, or the vendor per `vendor-contract-register.md`) and exactly one Accountable. | Project Manager |
| 3 | Everything the Team Member needs (inputs, constraints, related artifacts) is stated or linked, so nothing has to be guessed. | Project Manager |
| 4 | If `quality-management-plan.md` exists, its QA Gate Criteria cover this deliverable type. | Quality Manager |
| 5 | If `resource-management-plan.md` exists, the assignee is not over-allocated in `resource-allocation.md`. | Resource Manager |
| 6 | If `organization.md` exists, the Responsible party is a Team Roster member with Status Confirmed (not Proposed or Open); an AI member's Member ID matches its `bus/<member>/` name. | Project Manager |
| 7 | If the work is vendor-owned, its contract in `vendor-contract-register.md` is active. | Procurement Manager |

## Definition of Done

<!-- The checks a work package must pass before /pf-check-report sets it to "Done" in tracker.md; every
row must pass. Add a row for a project-specific check. Under the Agile layer, the user's acceptance at
/pf-agile-sprint-review comes after Done and is not a row here. -->

| # | Check | If it fails |
|---|---|---|
| 1 | Every acceptance criterion in the task (from the WBS Dictionary) is met, as stated in the Team Member's report and verified by the Project Manager. | Team Member reworks; status stays In Progress or Review |
| 2 | If `quality-management-plan.md` exists, the work package passes its QA Gate Criteria and the result is logged in `quality-control-log.md`. | Team Member reworks; status stays Review or Blocked |
| 3 | The report states status, what was delivered, acceptance criteria met or unmet, any new risks or issues, and what is needed next. | Team Member completes the report |

## Amendments

<!-- Log of changes to this file. The agent writes Date (YYYY-MM-DD) and Change (one line, with the CR
ID if there is one); the user names who approved it, and the agent never fills Approved By itself.
Keep the Initial version row and add new rows below it; never edit or delete earlier rows. -->

| Date | Change | Approved By |
|---|---|---|
| | Initial version | |
