# Work Package Definitions

## Definition of Ready

| # | Check | If it fails, goes to |
|---|---|---|
| 1 | The WBS Dictionary gives the work package testable acceptance criteria. | Planner |
| 2 | `raci.md` names a Responsible party (a Team Member, or the vendor per `vendor-contract-register.md`) and exactly one Accountable. | Project Manager |
| 3 | Everything the Team Member needs (inputs, constraints, related artifacts) is stated or linked, so nothing has to be guessed. | Project Manager |
| 4 | If `quality-management-plan.md` exists, its QA Gate Criteria cover this deliverable type. | Quality Manager |
| 5 | If `resource-management-plan.md` exists, the assignee is not over-allocated in `resource-allocation.md`. | Resource Manager |
| 6 | If `organization.md` exists, the Responsible party is a Team Roster member with Status Confirmed (not Proposed or Open); an AI member's Member ID matches its `bus/<member>/` name. | Project Manager |
| 7 | If the work is vendor-owned, its contract in `vendor-contract-register.md` is active. | Procurement Manager |
| 8 | Any work package that commits money has the Sponsor's sign-off recorded in its task. | Project Manager |

## Definition of Done

| # | Check | If it fails |
|---|---|---|
| 1 | Every acceptance criterion in the task (from the WBS Dictionary) is met, as stated in the Team Member's report and verified by the Project Manager. | Team Member reworks; status stays In Progress or Review |
| 2 | If `quality-management-plan.md` exists, the work package passes its QA Gate Criteria and the result is logged in `quality-control-log.md`. | Team Member reworks; status stays Review or Blocked |
| 3 | The report states status, what was delivered, acceptance criteria met or unmet, any new risks or issues, and what is needed next. | Team Member completes the report |

## Amendments

| Date | Change | Approved By |
|---|---|---|
| Week 1 | Initial version, with check 8 added to the Definition of Ready | Marta Silva |
