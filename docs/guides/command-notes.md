# Command Notes

Hand-written input for `tools/gen_command_reference.py`, which builds the tables in
[command-reference.md](command-reference.md). Each entry needs four lines: **When**, **You provide**,
**You get**, and **Preset** (the row of the Workflow Presets table in
[knowledge-areas.md](../knowledge-areas.md#workflow-presets) that governs the command, or `All`).
The generator derives everything else from the prompt files. Three optional lines override a
derived value: **Reads**, **Writes**, **Next**, and **Run in**.

Run `python tools/gen_command_reference.py` after editing this file or any prompt.

## /pf-setup-init

- **When:** Twice, at the very start, in an empty project. The first run creates `team.md`; run it again once `team.md` is filled in.
- **You provide:** Nothing on the first run. Between the runs, fill in `.pmo/team.md`: team name, every Team Defaults value (including the Workflow Preset: classic-waterfall, agile-hybrid, or lean), and at least one Working Rule. There is no separate preset question.
- **You get:** First run: `.pmo/team.md` from the blank template. Second run: a `.pmo/` folder with a blank file for each artifact. Your team defaults and working rules are copied into `project-constitution.md`. The second run refuses to start, and lists what is missing, while `team.md` is incomplete.
- **Preset:** All
- **Reads:** `templates/`, and `.pmo/team.md` on the second run
- **Next:** `/pf-setup-project-constitution` after the second run

## /pf-setup-project-constitution

- **When:** Right after init. Recommended for every project, optional for very small ones.
- **You provide:** Your project-only working rules, and any changes to the defaults already filled in: who approves scope, schedule, budget and risk decisions (the Sponsor by default), who reviews status reports (the Sponsor by default), when a deviation becomes a Change Request, and what "closed" means for the project. For each project default copied from `team.md` (preset, cost mode, cadence, cost threshold, risk ceiling) you say only whether this project needs a different value, and which team working rules do not apply. You also say whether a work package needs an extra ready or done check.
- **You get:** `project-constitution.md` for your review: the copied Project Defaults and Team Working Rules, plus your project working rules, any exempted team rules, and the decision authority, status report reviewers, escalation rules and project completion criteria (framework defaults unless you changed them). `work-package-definitions.md` is tailored with any extra checks.
- **Preset:** Constitution

## /pf-setup-charter

- **When:** After the constitution, to define what the project is for.
- **You provide:** Answers to the discovery questions: the business need, objectives and how success is measured, what is in and out of scope, constraints, known risks, the sponsor and key stakeholders, and rough milestones.
- **You get:** `charter.md` with measurable objectives, ready for your approval.
- **Preset:** Charter

## /pf-setup-organization

- **When:** After the charter, before the WBS. It sets up who decides and who is on the team.
- **You provide:** Who sponsors the project, who can approve changes, who is on the team so far and whether each is a person, an AI agent, or a vendor, and what roles the project needs.
- **You get:** `organization.md` with a governance structure, role definitions, and a first roster where each member is Proposed, Confirmed, or Open.
- **Preset:** Organization (governance + roster)

## /pf-plan-scope-wbs

- **When:** After the charter and organization are approved.
- **You provide:** Confirmation of the deliverables, how finely to break them down, and your review of each work package's acceptance criteria.
- **You get:** `scope-statement.md` and `wbs.md`, with a dictionary entry and testable acceptance criteria for every work package.
- **Preset:** Scope + WBS

## /pf-plan-schedule

- **When:** After the WBS is approved.
- **You provide:** Which work packages depend on which, and any fixed dates (otherwise the schedule uses relative weeks).
- **You get:** `schedule.md` with milestones, the sequence of work, and a plain-language critical path.
- **Preset:** Schedule

## /pf-plan-cost

- **When:** After the schedule, if your preset requires it or you want to track spend.
- **You provide:** Lightweight or Full EVM tracking, an estimate and its basis for each work package (or TBD), contingency, and the variance that should trigger a Change Request.
- **You get:** `cost-management-plan.md` with a budget baseline and control thresholds.
- **Preset:** Cost Management

## /pf-plan-risk

- **When:** After the schedule or cost plan. Re-run it any time to add a new risk.
- **You provide:** The risks you already know about, and a probability and impact (1 to 5) for each candidate, a response strategy, and an owner.
- **You get:** `risk-register.md`, scored and sorted with the highest risk first.
- **Preset:** Risk Management

## /pf-plan-quality

- **When:** After the risk register, if the project needs a quality gate.
- **You provide:** The standards that apply, a measurable target for each type of deliverable, and how you want reviews and inspections done.
- **You get:** `quality-management-plan.md` with QA gate criteria, and an empty `quality-control-log.md`.
- **Preset:** Quality Management

## /pf-plan-procurement

- **When:** After the quality plan, if any work might be bought rather than done in-house.
- **You provide:** Which work could be outsourced, how you would choose a vendor, and your preferred contract type.
- **You get:** `procurement-management-plan.md` with make-or-buy results, and a `vendor-contract-register.md`.
- **Preset:** Procurement Management

## /pf-plan-stakeholders

- **When:** After the earlier plans, once you know who is affected by the project.
- **You provide:** Who is affected or influential, how much power and interest each has, how supportive each is today, and how supportive you need them to be.
- **You get:** `stakeholder-register.md` (sensitive) and `communications-plan.md`.
- **Preset:** Stakeholder + Communications

## /pf-plan-skills

- **When:** After the stakeholders, before the RACI. It checks the team can actually do the work.
- **You provide:** The skills the work needs, and your honest rating (1 to 4) of each team member for each skill. Leave a rating as TBD if you do not know.
- **You get:** `skill-matrix.md` with coverage and a gap analysis. Each gap has a proposed action: train, hire, contract, reassign, or accept.
- **Preset:** Skills assessment

## /pf-plan-organization

- **When:** After the skills assessment. It settles who is on the team and who owns each work package.
- **You provide:** Your decision on each skill gap, the final roster (type, role, allocation, status), and who is Responsible and who is Accountable for each work package.
- **You get:** An updated `organization.md`, and `raci.md` with exactly one Accountable per work package.
- **Preset:** RACI

## /pf-plan-resources

- **When:** After the RACI, if you need capacity planning.
- **You provide:** Effort estimates, availability and time off for each person, how each role is staffed, and an over-allocation threshold.
- **You get:** `resource-management-plan.md` and `resource-allocation.md`.
- **Preset:** Resource Management (depth)

## /pf-start-manager

- **When:** Once planning is done. Open it in a new, dedicated conversation.
- **You provide:** Nothing, other than the new conversation. The agent reads the plan files itself.
- **You get:** A summary of the project's state (work packages, high risks, stakeholders to engage), and a `tracker.md` with one row per work package.
- **Preset:** All
- **Reads:** `project-constitution.md`, `charter.md`, `scope-statement.md`, `wbs.md`, `schedule.md`, `raci.md`, `tracker.md`
- **Writes:** `tracker.md` (one row per work package, if still blank)

## /pf-assign-task

- **When:** Whenever work packages are ready to start. Run it again for each round.
- **You provide:** Which work package(s) to dispatch, your approval of the proposed list, and a decision on any readiness check that fails (fix it or waive it).
- **You get:** A self-contained task for each work package, tracker rows set to In Progress, and instructions on which conversation to open next.
- **Preset:** All

## /pf-start-team-member

- **When:** In a new conversation for each AI team member that has a task. Person and Vendor members do not use this.
- **You provide:** Which team member this conversation is (for example `agenda-agent`), and answers to any questions the task raises.
- **You get:** The work package done, a working log, and a report to take back to the Manager.
- **Preset:** All
- **Reads:** `bus/<member>/task.md`
- **Writes:** `bus/<member>/report.md`, `memory/work-packages/WP-<id>.md`

## /pf-check-report

- **When:** After a team member reports. Run it once per report.
- **You provide:** The report (for a person or vendor, their status in your own words), and your decision if a quality gate fails.
- **You get:** An updated `tracker.md`, a quality-gate result when there is a quality plan, and pointers for any new risk or Change Request.
- **Preset:** All

## /pf-control-cycle

- **When:** On the cadence set in the constitution, usually weekly.
- **You provide:** Your review of the draft status report, and any figures the agent cannot read from the files (actual spend, availability).
- **You get:** `reports/status-<date>.md` with an overall Green, Yellow, or Red, validator findings, triggered rules, and refreshed cost, resource, quality, and vendor data.
- **Preset:** All
- **Next:** `/pf-assign-task` (or `/pf-change-request` if a baseline is breached)

## /pf-change-request

- **When:** When scope, schedule, or budget must change after the baselines are approved.
- **You provide:** What happened and why it needs a change, your choice among two or three options, and your approval, rejection, or deferral.
- **You get:** `changes/CR-<id>.md` with the impact on every dimension. If approved, the affected baseline files are updated.
- **Preset:** All

## /pf-log-decision

- **When:** When a judgment call does not change any baseline and should still be on record.
- **You provide:** The question, the options you considered, and your choice.
- **You get:** `decisions/DEC-<id>.md`, first Draft and then Signed-off. If it turns out to change a baseline, you are sent to `/pf-change-request` instead.
- **Preset:** All
- **Next:** Whatever you were doing

## /pf-agile-sprint-planning

- **When:** At the start of each sprint, if you use the Agile layer.
- **You provide:** The sprint dates, a sprint goal, and how much capacity the team has.
- **You get:** A new sprint section in `sprint-backlog.md` with the chosen work packages.
- **Preset:** Agile Ceremony Layer (Scrum Master track)

## /pf-agile-standup

- **When:** As often as you hold a standup during a sprint.
- **You provide:** For each work package in the sprint: what is done, in progress, or blocked.
- **You get:** A dated entry in `standup-log.md`, with blockers flagged and a pointer to a Change Request if one is needed.
- **Preset:** Agile Ceremony Layer (Scrum Master track)
- **Next:** `/pf-assign-task` or `/pf-check-report` (or `/pf-change-request` if a blocker affects a baseline)

## /pf-agile-backlog-refinement

- **When:** Before the next sprint, to get upcoming work ready.
- **You provide:** Answers to missing inputs and your priority for upcoming work.
- **You get:** Upcoming candidates in `sprint-backlog.md`, each marked Ready or Not Ready with the reason.
- **Preset:** Agile Ceremony Layer (Scrum Master track)

## /pf-agile-sprint-review

- **When:** At the end of a sprint, once its work packages are Done.
- **You provide:** As Product Owner, your decision to accept or reject each finished work package.
- **You get:** The review outcome for each work package recorded in `sprint-backlog.md`.
- **Preset:** Agile Ceremony Layer (Scrum Master track)

## /pf-agile-sprint-retro

- **When:** After the sprint review.
- **You provide:** What went well, what did not, and what to change next sprint.
- **You get:** A dated entry in `retro-log.md` with action items, each with an owner.
- **Preset:** Agile Ceremony Layer (Scrum Master track)

## /pf-session-handoff

- **When:** When a Manager or Team Member conversation is close to its context limit.
- **You provide:** Nothing, apart from pasting the prompt it gives you into a new conversation.
- **You get:** A handoff note saved in the project files, and a short prompt that resumes the work in a fresh conversation.
- **Preset:** All
- **Reads:** nothing; it summarises the conversation
- **Writes:** `tracker.md` Handoff Notes (Manager) or `memory/work-packages/WP-<id>.md` (Team Member)
- **Next:** Paste the handoff prompt into a new conversation

## /pf-session-archive-stage

- **When:** After a sprint, milestone, or phase is finished and its history is making files long.
- **You provide:** The stage label, the work packages it covers, and your approval of the exact list of files to move.
- **You get:** `archives/<stage>/stage-summary.md`, and the finished work-package history moved out of the live folders. Nothing is deleted.
- **Preset:** All

## /pf-close-project

- **When:** When the work is finished.
- **You provide:** A decision on any work package that is still open (finish, descope, or wait), and your lessons learned.
- **You get:** `closing/lessons-learned.md` and `closing/final-report.md`.
- **Preset:** All
- **Next:** None (the project is closed)
