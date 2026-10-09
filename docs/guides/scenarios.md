# Scenarios

Situations you will meet on a real project, with the commands to run, what you give each command,
and what you get back. Examples use the fictional [offsite event](../example/README.md) project, so
you can open the files named here and see them.

For the full list of commands see the [command reference](command-reference.md).

| # | Scenario | When you need it |
|---|---|---|
| 1 | [Start a small project](#1-start-a-small-project) | A short project with few people |
| 2 | [Start a full project with a team roster](#2-start-a-full-project-with-a-team-roster) | A project with governance, vendors, and several kinds of team member |
| 3 | [Find and close a skill gap](#3-find-and-close-a-skill-gap) | The team may not be able to do some of the work |
| 4 | [A vendor joins mid-project](#4-a-vendor-joins-mid-project) | You decide to buy part of the work |
| 5 | [Something changes the plan](#5-something-changes-the-plan) | A date, scope, or budget must move |
| 6 | [A work package fails its quality gate](#6-a-work-package-fails-its-quality-gate) | Delivered work is not good enough |
| 7 | [Spending is running over](#7-spending-is-running-over) | Costs exceed the plan |
| 8 | [A conversation is full](#8-a-conversation-is-full) | The chat is slowing down or forgetting |
| 9 | [Run a sprint](#9-run-a-sprint) | You use the Agile layer |
| 10 | [Close the project](#10-close-the-project) | The work is done, or has to stop |
| 11 | [Plan and close a Program Increment](#11-plan-and-close-a-program-increment) | A product team on the pi-cadence preset |

---

## 1. Start a small project

**Use the lean preset.** The [getting started tutorial](getting-started.md) walks through this one
step by step. In short: `/pf-setup-init`, `/pf-setup-charter`, `/pf-plan-scope-wbs`, `/pf-plan-schedule`,
`/pf-plan-organization`, then the work loop.

**What good looks like:** after planning, `charter.md`, `wbs.md`, `schedule.md`, and `raci.md` are
approved; every work package has a testable acceptance criterion and exactly one Accountable.

---

## 2. Start a full project with a team roster

**Situation:** a 10-week event with two people, an AI helper, and a venue vendor. You choose
agile-hybrid, so Organization and Skills are required.

| Step | Command (conversation) | You provide | You get |
|---|---|---|---|
| 1 | `/pf-setup-init` (Planner), run twice | First run: nothing. Then fill in `.pmo/team.md` (preset: agile-hybrid) and run it again. | `team.md` first, then the blank `.pmo/` files with the team defaults copied into the constitution. |
| 2 | `/pf-setup-project-constitution` | Working rules ("nothing that costs money without Sponsor sign-off"), who approves what, weekly reports. | `project-constitution.md`. |
| 3 | `/pf-setup-charter` | Need, objectives, success measures, in and out of scope, sponsor. | `charter.md`. |
| 4 | `/pf-setup-organization` | Who is the Sponsor and who can approve changes; the people on the team so far; whether each is a person, an AI agent, or a vendor. | `organization.md` with a governance structure and a first roster. |
| 5 | `/pf-plan-scope-wbs` and `/pf-plan-schedule` | Review of deliverables and acceptance criteria; dependencies. | `scope-statement.md`, `wbs.md`, `schedule.md`. |
| 6 | `/pf-plan-risk` and `/pf-plan-stakeholders` | Known risks with a score you agree; who is affected and how supportive they are. | `risk-register.md`, `stakeholder-register.md`, `communications-plan.md`. |
| 7 | `/pf-plan-skills` | The skills needed, and your rating (1 to 4) of each member for each skill. | `skill-matrix.md` with a gap analysis. |
| 8 | `/pf-plan-organization` | Decisions on each gap; the final roster; who is Responsible and Accountable. | Updated `organization.md`, and `raci.md`. |
| 9 | `/pf-start-manager` (new chat) | Nothing. | A project summary and a populated `tracker.md`. |

**What good looks like:** `python .github/skills/pf-helper-scripts/scripts/pf_validate.py --pmo .pmo`
shows no FAIL lines. A WARN for an unconfirmed roster member or an open skill gap is normal. See the
finished files in [offsite-event/.pmo/](../example/offsite-event/.pmo/).

---

## 3. Find and close a skill gap

**Situation:** the agenda for the offsite needs someone who can design and run a workshop for 40 people
(skill S-02, level 3). The best person on the team is level 2.

| Step | Command | You provide | You get |
|---|---|---|---|
| 1 | `/pf-plan-skills` (Planner) | An honest rating for each member. For Priya, "has attended workshops, not designed one" is level 2. | A gap row in `skill-matrix.md`: needed 3, best 2, proposed action. |
| 2 | Decide | Choose: train, hire, contract, reassign, or accept the risk. In the example you choose **contract**. | The gap's Action and Owner are recorded. |
| 3 | `/pf-plan-organization` | Add a `facilitator` as an Open vendor role. | `organization.md` shows the role as Open; the Org Change Log records why. |
| 4 | `/pf-plan-organization` again, once a facilitator is signed | Their name and Confirmed status. Re-run `/pf-plan-skills` to record their rating. | The roster is updated and the gap closes in the Gap Analysis. `/pf-assign-task` now passes its readiness check for them. |

**What good looks like:** the validator warns until a Confirmed member covers the skill at the needed
level, then the warning disappears. Skill ratings of named people are sensitive: keep that file inside the
project.

**Key rule:** an agent never invents a rating. If you do not know someone's level, it records `TBD`.

---

## 4. A vendor joins mid-project

**Situation:** you decide the catering should be done by the venue instead of in-house.

| Step | Command | You provide | You get |
|---|---|---|---|
| 1 | `/pf-plan-procurement` (Planner) | What is being bought, how you chose, the contract type (fixed price, time and materials, cost-reimbursable). | A make-or-buy result in `procurement-management-plan.md`; a row in `vendor-contract-register.md`. |
| 2 | `/pf-plan-organization` | Add the vendor as a roster member of type Vendor, with its role and a note pointing to the contract. | A new row in `organization.md`; the RACI gets a column for the vendor. |
| 3 | `/pf-change-request` (Manager), only if the budget or schedule moves | What changed and your approval. | `changes/CR-<id>.md` and updated baselines. |
| 4 | `/pf-assign-task` | Approval of the brief the Manager prepares for the vendor. | A brief for you to hand over; the tracker row set to In Progress. |
| 5 | `/pf-check-report` | The vendor's progress in your own words. | `tracker.md` updated. |

**What good looks like:** the vendor has a Member ID, a Confirmed status, a contract entry, and a RACI column,
and the Definition of Ready check passes when you assign them work.

---

## 5. Something changes the plan

**Situation:** the preferred venue is only free one week later than planned (risk R-001 has happened).

| Step | Command (conversation) | You provide | You get |
|---|---|---|---|
| 1 | `/pf-change-request` (Manager) | What happened and why it needs a change. | A draft with the impact on scope, schedule, cost, resources, risk, quality, and procurement. |
| 2 | Same command | Choose among the options (here: move to Week 9, keep the second-choice venue, or move to Week 11). | A recommendation, with the trade-offs for each option. |
| 3 | Same command | Your decision: Approved, Rejected, or Deferred. | `changes/CR-001.md`. If approved, `schedule.md` and `charter.md` are updated. |
| 4 | `/pf-assign-task` or `/pf-control-cycle` | Carry on. | The tracker links CR-001 to the affected work package. |

**What good looks like:** open [CR-001](../example/offsite-event/.pmo/changes/CR-001.md). Every impact
dimension is filled in (including "None"), and exactly one option is recommended.

**Change Request or decision?** If scope, schedule, budget, or resources change, it is a Change
Request. If you are only choosing between two equally good options, use `/pf-log-decision`, as in
[DEC-001](../example/offsite-event/.pmo/decisions/DEC-001.md).

---

## 6. A work package fails its quality gate

**Situation:** the project has a quality plan with QA gate criteria. An AI team member reports a work package
as done, but it misses a criterion.

| Step | Command (conversation) | You provide | You get |
|---|---|---|---|
| 1 | `/pf-start-team-member` (Team Member) | Nothing new. The agent writes its report. | `bus/<member>/report.md`. |
| 2 | `/pf-check-report` (Manager) | Your view of the gate result, or a waiver if you accept the shortfall. | A failed gate in `quality-control-log.md`; the work package stays in **Review** or **Blocked**, not Done. |
| 3 | `/pf-assign-task` | Approve sending the work back with the defects listed. | A new task for rework. |
| 4 | `/pf-check-report` again | The new report. | The gate passes; the work package is Done. |
| 5 | `/pf-control-cycle` | Nothing. | A **trend note** if the same kind of defect has happened twice or more. |

**What good looks like:** the work package is never marked Done while a gate criterion is unmet, unless
you explicitly waive it and the waiver is recorded.

---

## 7. Spending is running over

**Situation:** the weekly review shows that actual cost is higher than the budget at this point.

| Step | Command | You provide | You get |
|---|---|---|---|
| 0 | `/pf-plan-cost` (once, earlier) | Tracking mode (Lightweight or Full EVM), an estimate per work package, and the variance that triggers a Change Request. | `cost-management-plan.md` with a threshold. Without it there is nothing to compare against. |
| 1 | `/pf-control-cycle` (Manager) | The actual spend figures, which the agent cannot read from files. | `cost-performance.md` refreshed (in Full EVM mode, computed by a script, not by hand); a breach flagged in the status report. |
| 2 | `/pf-change-request` | Your decision: absorb it, cut scope, or raise the budget. | `changes/CR-<id>.md` and an updated budget baseline if approved. |

**What good looks like:** the status report is Yellow or Red for cost, and the breach is either
resolved by an approved Change Request or accepted on record.

---

## 8. A conversation is full

**Situation:** the Manager chat has run for a long time and is slowing down or forgetting things.

| Step | Command (conversation) | You provide | You get |
|---|---|---|---|
| 1 | `/pf-session-handoff` (the full chat) | Nothing. | A handoff note saved in `tracker.md` (Manager) or the work package log (Team Member), and a short prompt to paste. |
| 2 | Open a **new** chat and paste the prompt | The pasted prompt. | A fresh agent that reads the files and continues. |

The agents also remind you to do this before the limit, not after.

**What good looks like:** the new chat can say where the project stands without you re-explaining,
because everything it needs is in `.pmo/`.

---

## 9. Run a sprint

**Situation:** you use the Agile layer (default under agile-hybrid). You act as Product Owner.

| Step | Command | You provide | You get |
|---|---|---|---|
| 1 | `/pf-agile-backlog-refinement` | Missing inputs and priorities for upcoming work. | Candidates in `sprint-backlog.md` marked Ready or Not Ready. |
| 2 | `/pf-agile-sprint-planning` | Sprint dates, a goal, and the team's capacity. | A sprint section in `sprint-backlog.md`. |
| 3 | `/pf-assign-task`, then the work loop | As in the [command reference](command-reference.md). | Work packages dispatched and checked. |
| 4 | `/pf-agile-standup` (as often as you meet) | What is done, in progress, or blocked, per work package. | A dated entry in `standup-log.md`. |
| 5 | `/pf-agile-sprint-review` | Accept or reject each finished work package. | The outcome per package in `sprint-backlog.md`. |
| 6 | `/pf-agile-sprint-retro` | What went well, what did not, what to change. | A dated entry in `retro-log.md` with actions. |
| 7 | `/pf-session-archive-stage` (optional) | The stage label and approval of the files to move. | The sprint's history archived; nothing deleted. |

**What good looks like:** see [sprint-backlog.md](../example/offsite-event/.pmo/sprint-backlog.md): one
accepted sprint, one in progress, and refined candidates for the next.

---

## 10. Close the project

**Situation:** the offsite has run, feedback is in, and one work package was cancelled along the way.

| Step | Command (conversation) | You provide | You get |
|---|---|---|---|
| 1 | `/pf-close-project` (Manager) | For each work package still open: finish it, descope it, or wait. | The agent checks `tracker.md` and sends you to `/pf-change-request` for any descoping. |
| 2 | Same command | Your lessons learned: what went well, what did not, recommendations. | `closing/lessons-learned.md`. |
| 3 | Same command | Your review. | `closing/final-report.md`: objectives against what was delivered, schedule and scope variances, risks that did and did not happen. |

**What good looks like:** every work package is Done or Descoped through an approved Change Request,
and the final report points to all the `.pmo/` files as the permanent record.

---

## 11. Plan and close a Program Increment

**Situation:** a product team uses the pi-cadence preset. The charter is approved and the PI Practices in
the constitution say which practices you use. This scenario has no example files in the offsite project.

| Step | Command (conversation) | You provide | You get |
|---|---|---|---|
| 1 | `/pf-plan-roadmap` (Planner), once a year | Themes, the planned PIs with dates if you have them, and confidence for each. | `roadmap.md`. Only the next PI is detailed. |
| 2 | `/pf-plan-pi` (Planner) | The backlog items, each iteration's capacity, and per the practices: business value and who scored it, the confidence votes, WSJF figures, ROAM statuses. | `pi-plan.md` with the cut line, and `product-backlog.md` ranked. |
| 3 | `/pf-plan-scope-wbs`, `/pf-plan-schedule` | Review of the PI's work packages and iterations. | A new PI branch in `wbs.md` and `schedule.md`; no Change Request. |
| 4 | The work loop and the Agile layer | As in scenario 9. | Iterations run inside the PI. |
| 5 | `/pf-close-pi` (Manager), on the PI's end date | What carries over, the achieved value of each objective, the demo feedback and retrospective. | The review in `pi-plan.md`, the predictability percentage if that practice is on, unfinished items back in the backlog, the PI Closed in the roadmap. |
| 6 | `/pf-plan-pi` again | As in step 2. | The next PI plan. |

**What good looks like:** the PI ends on its date whether or not everything is finished, the cut line shows
what was dropped, and every number was given by a person, not by the agent.
