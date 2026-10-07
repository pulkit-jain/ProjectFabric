# Command Reference

Every ProjectFabric command, with what to give it and what you get back. For a story-style walk
through, see [scenarios.md](scenarios.md). For the concepts behind the three conversations and the
presets, see [how-a-project-runs.md](how-a-project-runs.md).

## How to read the tables

| Column | Meaning |
|---|---|
| Command | The slash command to type in Copilot Chat. |
| Run in | The conversation to use. **Planner** for setup and planning, **Manager** for running the project, **Team Member** for an AI member's work. Each is a separate chat; they share nothing except the `.pmo/` files. |
| When to run | The moment in the project when the command fits. |
| You provide | What the agent will ask you for. It never invents these; if you do not know, say so and it records `TBD`. |
| You get | What the command produces, and what you review. |
| Files | The `.pmo/` files it reads and writes. |
| Next | The command the agent will point you to afterwards. |
| Preset | Whether the command is required under each Workflow Preset, in this order: classic-waterfall / agile-hybrid / lean. **R** required, **O** optional (the agent asks once), **Rec** recommended, **On** engaged by default, **Off** not offered. **All** means the preset does not change it. |

The tables below are generated from the prompt files and [command-notes.md](command-notes.md).
Do not edit them by hand; run `python tools/gen_command_reference.py` instead.

## The usual order

Setup: `/pf-setup-init`, `/pf-setup-project-constitution`, `/pf-setup-charter`, `/pf-setup-organization`.
Planning: `/pf-plan-scope-wbs`, `/pf-plan-schedule`, `/pf-plan-cost`, `/pf-plan-risk`,
`/pf-plan-quality`, `/pf-plan-procurement`, `/pf-plan-stakeholders`, `/pf-plan-skills`,
`/pf-plan-organization`, `/pf-plan-resources`. Then the work loop starts with `/pf-start-manager`.
Under the agile-hybrid and lean presets some planning commands are optional, and the agent asks
once whether to run them.

## Setup

Run these once, in the Planner conversation, to create the project's files and agree how it will be
governed. Nothing here plans any work yet.

<!-- BEGIN GENERATED: setup -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-setup-init` | Planner | Twice, at the very start, in an empty project. The first run creates `team.md`; run it again once `team.md` is filled in. | Nothing on the first run. Between the runs, fill in `.pmo/team.md`: team name, every Team Defaults value (including the Workflow Preset: classic-waterfall, agile-hybrid, or lean), and at least one Team Standard. There is no separate preset question. | First run: `.pmo/team.md` from the blank template. Second run: a `.pmo/` folder with a blank file for each artifact, with the preset from `team.md` recorded in the constitution. The second run refuses to start, and lists what is missing, while `team.md` is incomplete. | reads: `templates/`, and `.pmo/team.md` on the second run<br>writes: `.pmo/`, `team.md` | `/pf-setup-project-constitution` after the second run | All |
| `/pf-setup-project-constitution` | Planner | Right after init. Recommended for every project, optional for very small ones. | Your non-negotiable principles, who approves scope, schedule, budget and risk decisions, who reviews status reports, and when a deviation becomes a Change Request. The reporting cadence and the cost and risk thresholds come from `team.md` and are not asked again. | `project-constitution.md` for your review, with team defaults applied where a `team.md` exists. | writes: `project-constitution.md` | `/pf-setup-charter` | Rec / Rec / O |
| `/pf-setup-charter` | Planner | After the constitution, to define what the project is for. | Answers to the discovery questions: the business need, objectives and how success is measured, what is in and out of scope, constraints, known risks, the sponsor and key stakeholders, and rough milestones. | `charter.md` with measurable objectives, ready for your approval. | writes: `charter.md` | `/pf-setup-organization` | R / R / R |
| `/pf-setup-organization` | Planner | After the charter, before the WBS. It sets up who decides and who is on the team. | Who sponsors the project, who can approve changes, who is on the team so far and whether each is a person, an AI agent, or a vendor, and what roles the project needs. | `organization.md` with a governance structure, role definitions, and a first roster where each member is Proposed, Confirmed, or Open. | reads: `charter.md`, `project-constitution.md`<br>writes: `organization.md` | `/pf-plan-scope-wbs` | R / R / O |
<!-- END GENERATED: setup -->

## Plan

Planning builds the baselines: scope, schedule, cost, risk, quality, vendors, stakeholders, skills,
roster, and resources. Each command ends with your review, and approving it makes the file a
baseline. After that, changes go through `/pf-change-request`.

<!-- BEGIN GENERATED: plan -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-plan-scope-wbs` | Planner | After the charter and organization are approved. | Confirmation of the deliverables, how finely to break them down, and your review of each work package's acceptance criteria. | `scope-statement.md` and `wbs.md`, with a dictionary entry and testable acceptance criteria for every work package. | reads: `charter.md`<br>writes: `scope-statement.md`, `wbs.md` | `/pf-plan-schedule` | R / R / R |
| `/pf-plan-schedule` | Planner | After the WBS is approved. | Which work packages depend on which, and any fixed dates (otherwise the schedule uses relative weeks). | `schedule.md` with milestones, the sequence of work, and a plain-language critical path. | reads: `wbs.md`<br>writes: `schedule.md` | `/pf-plan-cost` | R / R / R |
| `/pf-plan-cost` | Planner | After the schedule, if your preset requires it or you want to track spend. | Lightweight or Full EVM tracking, an estimate and its basis for each work package (or TBD), contingency, and the variance that should trigger a Change Request. | `cost-management-plan.md` with a budget baseline and control thresholds. | reads: `wbs.md`, `schedule.md`, `risk-register.md`<br>writes: `cost-management-plan.md` | `/pf-plan-risk` | R / O / O |
| `/pf-plan-risk` | Planner | After the schedule or cost plan. Re-run it any time to add a new risk. | The risks you already know about, and a probability and impact (1 to 5) for each candidate, a response strategy, and an owner. | `risk-register.md`, scored and sorted with the highest risk first. | reads: `charter.md`, `wbs.md`<br>writes: `risk-register.md` | `/pf-plan-quality` | R / R / O |
| `/pf-plan-quality` | Planner | After the risk register, if the project needs a quality gate. | The standards that apply, a measurable target for each type of deliverable, and how you want reviews and inspections done. | `quality-management-plan.md` with QA gate criteria, and an empty `quality-control-log.md`. | reads: `wbs.md`, `risk-register.md`<br>writes: `quality-management-plan.md`, `quality-control-log.md` | `/pf-plan-procurement` | R / O / O |
| `/pf-plan-procurement` | Planner | After the quality plan, if any work might be bought rather than done in-house. | Which work could be outsourced, how you would choose a vendor, and your preferred contract type. | `procurement-management-plan.md` with make-or-buy results, and a `vendor-contract-register.md`. | reads: `wbs.md`, `cost-management-plan.md`, `risk-register.md`<br>writes: `procurement-management-plan.md`, `vendor-contract-register.md` | `/pf-plan-stakeholders` | R / O / O |
| `/pf-plan-stakeholders` | Planner | After the earlier plans, once you know who is affected by the project. | Who is affected or influential, how much power and interest each has, how supportive each is today, and how supportive you need them to be. | `stakeholder-register.md` (sensitive) and `communications-plan.md`. | reads: `charter.md`<br>writes: `stakeholder-register.md`, `communications-plan.md` | `/pf-plan-skills` | R / R / O |
| `/pf-plan-skills` | Planner | After the stakeholders, before the RACI. It checks the team can actually do the work. | The skills the work needs, and your honest rating (1 to 4) of each team member for each skill. Leave a rating as TBD if you do not know. | `skill-matrix.md` with coverage and a gap analysis. Each gap has a proposed action: train, hire, contract, reassign, or accept. | reads: `wbs.md`, `organization.md`, `project-constitution.md`<br>writes: `skill-matrix.md` | `/pf-plan-organization` | R / R / O |
| `/pf-plan-organization` | Planner | After the skills assessment. It settles who is on the team and who owns each work package. | Your decision on each skill gap, the final roster (type, role, allocation, status), and who is Responsible and who is Accountable for each work package. | An updated `organization.md`, and `raci.md` with exactly one Accountable per work package. | reads: `wbs.md`, `organization.md`, `skill-matrix.md`<br>writes: `organization.md`, `raci.md` | `/pf-plan-resources` | R / R / R |
| `/pf-plan-resources` | Planner | After the RACI, if you need capacity planning. | Effort estimates, availability and time off for each person, how each role is staffed, and an over-allocation threshold. | `resource-management-plan.md` and `resource-allocation.md`. | reads: `wbs.md`, `raci.md`, `schedule.md`<br>writes: `resource-management-plan.md`, `resource-allocation.md` | `/pf-start-manager` | R / O / O |
<!-- END GENERATED: plan -->

## Work loop

The core cycle: the Manager dispatches a work package, a team member does it, the Manager checks the
report, and a control cycle reviews the whole project. Repeat until every work package is done.

<!-- BEGIN GENERATED: work -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-start-manager` | Manager | Once planning is done. Open it in a new, dedicated conversation. | Nothing, other than the new conversation. The agent reads the plan files itself. | A summary of the project's state (work packages, high risks, stakeholders to engage), and a `tracker.md` with one row per work package. | reads: `project-constitution.md`, `charter.md`, `scope-statement.md`, `wbs.md`, `schedule.md`, `raci.md`, `tracker.md`<br>writes: `tracker.md` (one row per work package, if still blank) | `/pf-assign-task` | All |
| `/pf-assign-task` | Manager | Whenever work packages are ready to start. Run it again for each round. | Which work package(s) to dispatch, your approval of the proposed list, and a decision on any readiness check that fails (fix it or waive it). | A self-contained task for each work package, tracker rows set to In Progress, and instructions on which conversation to open next. | reads: `tracker.md`, `schedule.md`, `raci.md`<br>writes: `bus/<member>/task.md` | `/pf-start-team-member` | All |
| `/pf-start-team-member` | Team Member | In a new conversation for each AI team member that has a task. Person and Vendor members do not use this. | Which team member this conversation is (for example `agenda-agent`), and answers to any questions the task raises. | The work package done, a working log, and a report to take back to the Manager. | reads: `bus/<member>/task.md`<br>writes: `bus/<member>/report.md`, `memory/work-packages/WP-<id>.md` | `/pf-check-report` | All |
| `/pf-check-report` | Manager | After a team member reports. Run it once per report. | The report (for a person or vendor, their status in your own words), and your decision if a quality gate fails. | An updated `tracker.md`, a quality-gate result when there is a quality plan, and pointers for any new risk or Change Request. | reads: `bus/<member>/report.md`, `quality-management-plan.md`<br>writes: `tracker.md`, `quality-control-log.md` | `/pf-assign-task` | All |
| `/pf-control-cycle` | Manager | On the cadence set in the constitution, usually weekly. | Your review of the draft status report, and any figures the agent cannot read from the files (actual spend, availability). | `reports/status-<date>.md` with an overall Green, Yellow, or Red, validator findings, triggered rules, and refreshed cost, resource, quality, and vendor data. | reads: `tracker.md`, `schedule.md`, `risk-register.md`, `stakeholder-register.md`, `cost-management-plan.md`, `resource-management-plan.md`, `quality-management-plan.md`, `procurement-management-plan.md`<br>writes: `reports/status-<date>.md`, `cost-performance.md`, `resource-allocation.md`, `quality-control-log.md`, `vendor-contract-register.md` | `/pf-assign-task` (or `/pf-change-request` if a baseline is breached) | All |
<!-- END GENERATED: work -->

## Change and decisions

Two ways to record that something was decided. Use a Change Request when a baseline (scope,
schedule, budget, resources) changes. Use a decision when the choice does not touch any baseline.

<!-- BEGIN GENERATED: change -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-change-request` | Manager | When scope, schedule, or budget must change after the baselines are approved. | What happened and why it needs a change, your choice among two or three options, and your approval, rejection, or deferral. | `changes/CR-<id>.md` with the impact on every dimension. If approved, the affected baseline files are updated. | writes: `changes/CR-<id>.md` | `/pf-assign-task` | All |
| `/pf-log-decision` | Manager | When a judgment call does not change any baseline and should still be on record. | The question, the options you considered, and your choice. | `decisions/DEC-<id>.md`, first Draft and then Signed-off. If it turns out to change a baseline, you are sent to `/pf-change-request` instead. | writes: `decisions/DEC-<id>.md` | Whatever you were doing | All |
<!-- END GENERATED: change -->

## Agile

An optional layer of Scrum ceremonies that runs alongside the plan. It is on by default under
agile-hybrid and offered once under the other presets. There is no Product Owner agent: you play
that role when you accept or reject work at the sprint review.

<!-- BEGIN GENERATED: agile -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-agile-sprint-planning` | Manager | At the start of each sprint, if you use the Agile layer. | The sprint dates, a sprint goal, and how much capacity the team has. | A new sprint section in `sprint-backlog.md` with the chosen work packages. | reads: `project-constitution.md`, `wbs.md`, `tracker.md`, `resource-allocation.md`<br>writes: `sprint-backlog.md` | `/pf-assign-task` | Off / On / O |
| `/pf-agile-standup` | Manager | As often as you hold a standup during a sprint. | For each work package in the sprint: what is done, in progress, or blocked. | A dated entry in `standup-log.md`, with blockers flagged and a pointer to a Change Request if one is needed. | reads: `tracker.md`, `sprint-backlog.md`<br>writes: `standup-log.md` | `/pf-assign-task` or `/pf-check-report` (or `/pf-change-request` if a blocker affects a baseline) | Off / On / O |
| `/pf-agile-backlog-refinement` | Manager | Before the next sprint, to get upcoming work ready. | Answers to missing inputs and your priority for upcoming work. | Upcoming candidates in `sprint-backlog.md`, each marked Ready or Not Ready with the reason. | reads: `wbs.md`, `tracker.md`<br>writes: `sprint-backlog.md` | `/pf-agile-sprint-planning` | Off / On / O |
| `/pf-agile-sprint-review` | Manager | At the end of a sprint, once its work packages are Done. | As Product Owner, your decision to accept or reject each finished work package. | The review outcome for each work package recorded in `sprint-backlog.md`. | reads: `sprint-backlog.md`, `tracker.md`<br>writes: `sprint-backlog.md` | `/pf-agile-sprint-retro` | Off / On / O |
| `/pf-agile-sprint-retro` | Manager | After the sprint review. | What went well, what did not, and what to change next sprint. | A dated entry in `retro-log.md` with action items, each with an owner. | reads: `standup-log.md`, `tracker.md`, `sprint-backlog.md`<br>writes: `retro-log.md` | `/pf-agile-sprint-planning` | Off / On / O |
<!-- END GENERATED: agile -->

## Session

Housekeeping for long projects. Chat conversations have a size limit, and old history makes the
files long.

<!-- BEGIN GENERATED: session -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-session-handoff` | The conversation that is full | When a Manager or Team Member conversation is close to its context limit. | Nothing, apart from pasting the prompt it gives you into a new conversation. | A handoff note saved in the project files, and a short prompt that resumes the work in a fresh conversation. | reads: nothing; it summarises the conversation<br>writes: `tracker.md` Handoff Notes (Manager) or `memory/work-packages/WP-<id>.md` (Team Member) | Paste the handoff prompt into a new conversation | All |
| `/pf-session-archive-stage` | Manager | After a sprint, milestone, or phase is finished and its history is making files long. | The stage label, the work packages it covers, and your approval of the exact list of files to move. | `archives/<stage>/stage-summary.md`, and the finished work-package history moved out of the live folders. Nothing is deleted. | reads: `tracker.md`, `memory/work-packages/`, `bus/`, `reports/`, `standup-log.md`, `sprint-backlog.md`<br>writes: `archives/<stage>/stage-summary.md` | `/pf-assign-task` | All |
<!-- END GENERATED: session -->

## Close

<!-- BEGIN GENERATED: close -->
| Command | Run in | When to run | You provide | You get | Files | Next | Preset |
|---|---|---|---|---|---|---|---|
| `/pf-close-project` | Manager | When the work is finished. | A decision on any work package that is still open (finish, descope, or wait), and your lessons learned. | `closing/lessons-learned.md` and `closing/final-report.md`. | writes: `closing/lessons-learned.md`, `closing/final-report.md` | None (the project is closed) | All |
<!-- END GENERATED: close -->
