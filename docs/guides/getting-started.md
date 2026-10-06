# Getting Started

This tutorial takes you from an empty folder to a finished mini project, using the **lean** preset so
there are few steps. By the end you will
have run every kind of command once and know what each file is for.

The project in this tutorial is deliberately tiny: **start a monthly internal newsletter**. Replace
it with your own project whenever you like; the commands are the same.

## Before you start

1. **Install.** Copy this repository's `.github/` and `templates/` folders into your project folder.
2. **Open Copilot Chat in VS Code** in agent mode, in that project folder.
3. **Python is optional.** With Python 3.9 or newer, agents can run helper scripts for consistency
   checks and cost maths. Without it they do the same tasks by hand. Nothing needs installing.

## Choose how to read this page

| You are | Read like this |
|---|---|
| **New to project management** | Read everything, including the "New to PM" notes. Read [How a project runs](how-a-project-runs.md) first if you want the ideas up front. |
| **An experienced project manager** | Skim the table below, then follow the "Experienced" notes. Your main questions will be which files are baselines and when you are asked to approve. |

**Fast path for experienced readers:** `/pf-setup-init` (twice: fill in `team.md` with lean between the runs) → `/pf-setup-charter` →
`/pf-plan-scope-wbs` → `/pf-plan-schedule` → `/pf-plan-organization` → *new chat:*
`/pf-start-manager` → `/pf-assign-task` → *new chat:* `/pf-start-team-member` → back in the Manager
chat `/pf-check-report` → `/pf-control-cycle` → `/pf-close-project`. Optional phases are offered once
and can be declined.

## Step 1: Create the project files

**Conversation:** Planner (open a new chat and keep it for all planning steps).

This step has two passes, because the team defaults (including the preset) must exist first.

**Pass 1.** Type: `/pf-setup-init`

| You provide | You get |
|---|---|
| Nothing. | A `.pmo/` folder holding only `team.md`, from the blank template. |

Then fill in `.pmo/team.md` (see [About `team.md`](#about-teammd)). For this tutorial use:

| Field | Value for this tutorial |
|---|---|
| Team | Internal Communications |
| Workflow Preset | lean |
| Cost tracking mode | Lightweight |
| Control cycle cadence | per milestone |
| Cost variance escalation threshold | N/A |
| Risk acceptance score ceiling | N/A |
| Team Standards | 1. Status reports go to the Head of Communications. |

**Pass 2.** Type `/pf-setup-init` again, in the same chat.

| You provide | You get |
|---|---|
| Nothing. There is no preset question: the preset comes from `team.md`. If `team.md` is incomplete the agent lists what is missing and stops. | The rest of `.pmo/`: a blank file for each artifact, and `lean` recorded in `constitution.md`. |

**New to PM:** `.pmo/` is the project's memory. Every later command reads and writes files in it.

**Experienced:** pass 2 creates blanks only and never overwrites an existing file.

**Check:** `.pmo/` holds the full set of files and `constitution.md` shows `**Preset:** lean`.

### About `team.md`

`team.md` holds defaults and rules shared by every project your team runs (preset, cost tracking mode,
reporting cadence, thresholds, standing rules). It is required: `/pf-setup-init` pass 2 will not run
until it is filled in. Pass 1 creates it from the blank template in `.pmo/`. If your team keeps a
shared standards file, paste its content in; otherwise fill it in by hand and keep a copy for your
next project.

It counts as filled in when the Team name is set, every Team Defaults row has a value other than
`TBD` (write `N/A` where your team has no default; the Workflow Preset must be one of the three
presets), and Team Standards has at least one rule. Amendments is optional.

| Section | What to write |
|---|---|
| **Team Name** | Your team's name. |
| **Team Defaults** | One value per setting: Workflow Preset, Cost tracking mode (Lightweight or Full EVM), Control cycle cadence, Cost variance escalation threshold, Risk acceptance score ceiling. |
| **Team Standards** | Numbered rules every project follows, such as "all vendor contracts need Legal review". At least one. See [Team standards](team-standards.md) for examples to pick from. |
| **Amendments** | Optional. A row for each change after the file is baselined, with the date and who approved it. |

What each Team Defaults setting means, and where it is used. None of them is enforced; each is
proposed as a starting value and you can pick differently per project.

| Setting | Meaning | Proposed by |
|---|---|---|
| Workflow Preset | Which knowledge areas are planned: classic-waterfall, agile-hybrid, or lean. | `/pf-setup-init` pass 2 (read, not asked) |
| Cost tracking mode | Lightweight (budget against actual) or Full EVM. | `/pf-plan-cost` |
| Control cycle cadence | How often you intend to run `/pf-control-cycle`, such as weekly. It is a reminder, not a schedule: nothing runs it for you. | `/pf-setup-constitution` (Reporting Cadence) |
| Cost variance escalation threshold | Overrun, such as 10%, beyond which a deviation becomes a Change Request instead of being absorbed. | `/pf-plan-cost` (Cost Control Thresholds) and `/pf-setup-constitution` |
| Risk acceptance score ceiling | Highest risk Score (Probability x Impact, 1 to 25) that may be accepted without sign-off. Accepting a risk above it is flagged and needs the approver named in the constitution. | `/pf-plan-risk` and `/pf-setup-constitution` (Decision Authority) |

A project's `constitution.md` may override a team default only by naming the override explicitly. Once
filled in, `team.md` is a baseline: change it through `/pf-change-request`, not by editing it directly.

## Step 2: Write the charter

Type: `/pf-setup-charter`

The agent asks discovery questions in rounds and pushes back on vague answers. Sample answers for
this tutorial:

| Question | Sample answer |
|---|---|
| Why does the project exist? | Staff do not know what other teams are working on. |
| Objectives and how success is measured | Publish 3 issues in 3 months; at least 50% of staff open each issue. |
| In and out of scope | In: writing, review, publishing. Out: a new website. |
| Constraints | No budget; one editor part-time. |
| Sponsor | Dana Okafor, Head of Communications. |

You get `charter.md`. Read it and say **approved** when it is right. Ending the conversation without
approving leaves the charter in draft, and later commands will not accept it.

**New to PM:** the charter is the "why" in one page. Spending time here saves rework later.

The constitution step (`/pf-setup-constitution`) and the organization step (`/pf-setup-organization`)
are optional under lean. The agent will offer them; for this tutorial, decline both.

## Step 3: Break the work down

Type: `/pf-plan-scope-wbs`

| You provide | You get |
|---|---|
| A review of the deliverables, and of how finely to split them. Check that each work package has an acceptance criterion you could test. | `scope-statement.md` and `wbs.md`. |

Example work packages for this tutorial:

| ID | Work package | Acceptance criterion |
|---|---|---|
| 1.1 | Choose themes for 3 issues | A list of 3 themes approved by Dana |
| 1.2 | Write issue 1 | A 600-word draft with two contributor quotes |
| 1.3 | Review and publish issue 1 | Reviewed by Dana, sent to all staff |

**New to PM:** a **work package** is a piece of work one person or agent can finish and report on.
**Acceptance criteria** say what "done" means, in words anyone could check.

## Step 4: Order the work

Type: `/pf-plan-schedule`

You tell the agent which work packages must finish before others can start. You get `schedule.md` with
milestones and a plain-language critical path. Without fixed dates, it uses relative weeks.

## Step 5: Say who does what

Type: `/pf-plan-organization`

| You provide | You get |
|---|---|
| For each work package, who is **Responsible** (does it) and who is **Accountable** (answers for it). Exactly one person is Accountable per work package. | `raci.md`. |

Under lean there is no formal roster, so the agent uses the names you give directly. For an AI team
member, use a short ID such as `writer-agent`. That ID becomes the name of its task folder.

**New to PM:** if you want to know why exactly one Accountable, see the RACI entry in the
[glossary](how-a-project-runs.md#glossary-for-newcomers).

Cost, risk, quality, procurement, stakeholder, skills, and resource planning are optional under lean
and the agent asks once for each; decline them for now. You can run any of them later.

## Step 6: Start the Manager

**Conversation:** open a **new** chat for the Manager.

Type: `/pf-start-manager`

You provide nothing. The agent reads the plan files, checks that the required ones are approved, creates
a row per work package in `tracker.md`, and summarizes where the project stands.

## Step 7: Hand out the first work package

Type: `/pf-assign-task`

| You provide | You get |
|---|---|
| Approval of the work package it proposes (it picks the first one whose predecessors are done), and a decision if a readiness check fails. | `bus/writer-agent/task.md`, and the tracker row set to In Progress. |

The agent tells you which conversation to open next.

## Step 8: Do the work

**Conversation:** open a **new** chat, one per AI team member.

Type: `/pf-start-team-member` and tell it which ID this chat represents (`writer-agent`).

The team member reads its task, does the work, logs progress to `memory/work-packages/WP-1.1.md`, and
writes `bus/writer-agent/report.md`. For a person on your team, you do the work yourself and tell the
Manager the result in step 9.

## Step 9: Check the result

**Conversation:** back in the Manager chat.

Type: `/pf-check-report`

| You provide | You get |
|---|---|
| The report (or, for a person, your status in your own words). | `tracker.md` updated; the work package set to Done only if its acceptance criteria are met. |

Repeat steps 7 to 9 for each work package.

## Step 10: Review the whole project

Type: `/pf-control-cycle`

You get `reports/status-<date>.md` with an overall Green, Yellow, or Red status, risks, and what is
next. Do this on the cadence you agreed, usually weekly. If a baseline has to change, the status report
sends you to `/pf-change-request`.

## Step 11: Close

When every work package is Done, type `/pf-close-project`. You get `closing/lessons-learned.md` and
`closing/final-report.md`.

## What next

- See a full, realistic set of files in the [example project](../example/README.md).
- Follow the [scenarios](scenarios.md) for situations such as a change request, a skill gap, or a
  conversation that has run out of space.
- Look up any command in the [command reference](command-reference.md).
