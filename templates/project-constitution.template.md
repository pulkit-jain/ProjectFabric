# Project Constitution

<!-- The Project Constitution: the working agreements for THIS project. /pf-setup-init pass 2 copies
the Team Defaults and Working Rules from team.md into the Project Defaults and Team Working Rules
below; from then on agents read them here, not in team.md. Change a Project Default only if this
project needs a value different from the team's, and note the reason in the Amendments table.

Sits above individual artifacts and below the framework-wide .github/copilot-instructions.md.
Treat as baseline once approved; amend only through explicit user approval (see Amendments below). -->

## Project Defaults

<!-- Copied from team.md's Team Defaults at /pf-setup-init pass 2; same settings, one value each.
Workflow Preset: classic-waterfall / agile-hybrid / lean (governs which knowledge-area phases are
Required vs. Optional; see docs/knowledge-areas.md#workflow-presets). Cost tracking mode: Lightweight /
Full EVM (chosen at /pf-plan-cost and baselined in cost-management-plan.md). Control cycle cadence:
how often /pf-control-cycle runs. Cost variance escalation threshold: overrun beyond which a Change
Request is raised. Risk acceptance score ceiling: 1-25 (Probability x Impact); accepting a risk
above it needs sign-off. -->

| Setting | Project Default |
|---|---|
| Workflow Preset | TBD |
| Cost tracking mode | TBD |
| Control cycle cadence | TBD |
| Cost variance escalation threshold | TBD |
| Risk acceptance score ceiling | TBD |

## Team Working Rules

<!-- Copied from team.md's Working Rules at /pf-setup-init pass 2: the rules every project of your
team follows. Do not add project-specific rules here (use Project Working Rules below). -->

1.

## Project Working Rules

<!-- Non-negotiable rules for THIS PROJECT only, on top of the Team Working Rules above, e.g. "No
scope change without sponsor sign-off." A rule you want on every project of your team belongs in
team.md instead. -->

1.

## Exempted Team Working Rules

<!-- Only if a Team Working Rule above does not apply to this project: name the rule and give the
reason. Leave empty if none. A rule that is not listed here still applies. -->

-

## Decision Authority

<!-- Approver: the framework's default is the role shown; replace it with a named person or a
different role if the project needs one. The budget and risk Thresholds are not repeated here: they
are the Cost variance escalation threshold and Risk acceptance score ceiling in Project Defaults
above. Add a row for any other decision type that needs a named approver. -->

| Decision Type | Approver | Threshold |
|---|---|---|
| Scope change | Sponsor | Any change to `wbs.md` |
| Schedule change | Sponsor | Any change to baseline milestone dates |
| Budget change | Sponsor | Variance beyond the Cost variance escalation threshold |
| Risk acceptance | Sponsor | Score above the Risk acceptance score ceiling |

## Status Report Reviewers

<!-- Who must review each Status Report from /pf-control-cycle: one person or role per line. The
default is the Sponsor; add or replace as needed. How often the report is produced is the Control
cycle cadence in Project Defaults. -->

- Sponsor

## Escalation Rules

<!-- When a deviation becomes a Change Request (/pf-change-request) instead of being absorbed. The
rules below are the framework's defaults; add, change or drop a rule for this project and note the
reason in Amendments. Thresholds come from Project Defaults and the plans, not from numbers here. -->

- A change to scope (`scope-statement.md`, `wbs.md`) or to a baseline milestone date becomes a Change
  Request.
- A cost variance beyond the Cost variance escalation threshold becomes a Change Request.
- Accepting a risk scored above the Risk acceptance score ceiling needs the Decision Authority
  approver's sign-off.
- A work package that is blocked and cannot be unblocked by its owner is raised to the Project Manager
  and shown in the next Status Report.
- Anything smaller is absorbed and noted in the Variance Notes of `tracker.md`.

## Project Completion Criteria

<!-- What "closed" means for this project as a whole: the conditions /pf-close-project checks before it
closes the project. The rows below are the framework's defaults; add, change or drop one for this
project and note the reason in Amendments. The checks for a single work package (Definition of Ready
and Definition of Done) are in work-package-definitions.md. -->

- Every work package in `tracker.md` is Done (meeting the Definition of Done) or Descoped through an
  approved Change Request.
- Every deliverable in `scope-statement.md` has been accepted by the Sponsor.
- The objectives and success measures in `charter.md` have been reviewed with the Sponsor.
- Open risks, issues and vendor contracts are closed or handed to a named owner.
- Lessons learned and the final report are written and reviewed with the Sponsor.

## Amendments

<!-- Log of changes to this constitution. The agent writes Date (YYYY-MM-DD) and Change (one line, with
the CR ID if there is one); the user names who approved it, and the agent never fills Approved By
itself. Keep the Initial version row and add new rows below it; never edit or delete earlier rows. -->

| Date | Change | Approved By |
|---|---|---|
| | Initial version | |
