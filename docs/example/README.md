# Example Project: Company Offsite Event

A small, fictional project that shows what a ProjectFabric `.pmo/` folder looks like part-way
through a real run. Read the files to see what each command produces; nothing here is a template.

**The project:** a two-day offsite for a 40-person department, planned over ten weeks.
**Workflow Preset:** agile-hybrid, so Organization and Skills are required. Cost, Quality, and
Resource planning were skipped, and Procurement was pulled in only for the venue contract.
**Where it stands:** the end of Week 3. Two of nine work packages are done, the event has already
moved one week through a Change Request, and one skill gap is still open.

The team has all three kinds of member: two **people** (Priya, Tom), one **AI** member
(`agenda-agent`), and one **vendor** (the venue), plus an open vendor role for a facilitator.

Check it yourself:

```
python .github/skills/pf-helper-scripts/scripts/pf_validate.py --pmo docs/example/offsite-event/.pmo
```

It reports two warnings on purpose: the `facilitator` role is still Open, and skill S-02 has a gap.
Those are the project's real open issues, not mistakes.

## Which command made which file

Folder: [offsite-event/.pmo/](offsite-event/.pmo/)

| File | Produced by | Look at it to see |
|---|---|---|
| `team.md` | `/pf-setup-init` | Team-wide defaults, filled in before the rest of `.pmo/` is created |
| `project-constitution.md` | `/pf-setup-project-constitution` | The copied team defaults, decision authority, and the project completion criteria |
| `work-package-definitions.md` | `/pf-setup-init`, then `/pf-setup-project-constitution` | The standard Definition of Ready and Definition of Done, plus one project-specific check |
| `charter.md` | `/pf-setup-charter` | Objectives, scope, and success criteria written from the discovery questions |
| `organization.md` | `/pf-setup-organization`, then `/pf-plan-organization` | Governance, roles, and a roster with a Person, an AI, and Vendors |
| `scope-statement.md`, `wbs.md` | `/pf-plan-scope-wbs` | Four deliverables broken into nine work packages with acceptance criteria |
| `schedule.md` | `/pf-plan-schedule` | Sequencing and a critical path, revised once by CR-001 |
| `risk-register.md` | `/pf-plan-risk` | Three scored risks, one already closed |
| `stakeholder-register.md`, `communications-plan.md` | `/pf-plan-stakeholders` | Who needs what, and how often |
| `skill-matrix.md` | `/pf-plan-skills` | A catalog, requirements per work package, coverage, and one gap |
| `raci.md` | `/pf-plan-organization` | Roster members as columns; exactly one Accountable per row |
| `vendor-contract-register.md` | `/pf-plan-procurement` (pulled in for the venue) | A single fixed-price contract |
| `sprint-backlog.md` | `/pf-agile-sprint-planning`, `/pf-agile-sprint-review`, `/pf-agile-backlog-refinement` | Two sprints and refined candidates |
| `tracker.md` | `/pf-assign-task` and `/pf-check-report` | Live status of every work package |
| `bus/agenda-agent/task.md` | `/pf-assign-task` | A self-contained task for an AI member |
| `bus/agenda-agent/report.md` | `/pf-start-team-member` | What the AI member sends back |
| `memory/work-packages/WP-2.1.md` | `/pf-start-team-member` | The AI member's working log |
| `changes/CR-001.md` | `/pf-change-request` | A schedule change, with options and an approval |
| `decisions/DEC-001.md` | `/pf-log-decision` | A judgment call that does not change any baseline |
| `reports/status-week-03.md` | `/pf-control-cycle` | A status report with the Optional areas marked as not tracked |

## A suggested reading order

1. `charter.md`, to see what the project is for.
2. `organization.md` and `skill-matrix.md`, to see who does the work and where the gaps are.
3. `wbs.md`, `schedule.md`, and `raci.md`, to see how the work is split and owned.
4. `tracker.md` and `reports/status-week-03.md`, to see where things stand.
5. `changes/CR-001.md` and `decisions/DEC-001.md`, to see the difference between a change and a decision.
