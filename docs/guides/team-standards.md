# Team Standards

A reference list of example **Team Standards** to pick from, adapt, or ignore when you fill in the
Team Standards section of `.pmo/team.md`. ProjectFabric ships none of these as rules: every item below
is a suggestion, and any number in it is an example to replace with your own.

For how to create and fill in `team.md`, see [About `team.md`](getting-started.md#about-teammd).

## What a team standard is

A team standard is a working rule that every project of your team follows, written as one numbered
line in `team.md`. The agents read it before they act, and it sits between the framework's Ground Rules
and each project's constitution:

`Ground Rules` → `team.md` → `constitution.md`

| It is | It is not |
|---|---|
| A rule that applies to every project your team runs | A rule for one project (put that in the constitution's Principles) |
| Something an agent or person can check: who, what, when | A value for a Team Defaults row (cadence, thresholds, preset have their own rows) |
| Consistent with the framework's Ground Rules | A way around them. A standard may not contradict a Ground Rule |

Agents read and apply the standards but nothing checks them automatically, so a vague standard will be
applied loosely. A project may deviate only by naming the override in its constitution's "Overrides of
`team.md`" table, with a reason. Once `team.md` is filled in it is a baseline: change it through
[`/pf-change-request`](command-reference.md#change-and-decisions).

## How to write one

1. **One rule per line**, in a numbered list.
2. **Name the who and the when**: "The Sponsor approves every Change Request", not "Changes are
   approved".
3. **Make it checkable**: someone reading a finished artifact should be able to say whether it was
   followed.
4. **Keep only real rules.** An empty or padded list is worse than three rules the team keeps.
5. **Do not repeat the framework.** It already requires, for example, that agents never invent numbers
   and that baseline changes go through a Change Request.

## Example standards

Pick the ones that match how your team really works. The commands named are where the rule is most
likely to matter.

### Governance and approvals

| Example standard | Most relevant to |
|---|---|
| Every Change Request is approved by the Sponsor before a baseline file is edited. | `/pf-change-request` |
| Decisions that affect more than one team are logged with `/pf-log-decision` and signed off by the Sponsor. | `/pf-log-decision` |
| The charter is signed by the Sponsor before any planning command is run. | `/pf-setup-charter` |
| Status reports go to the Head of the PMO within one working day of each control cycle. | `/pf-control-cycle` |
| A project is not closed until the final report and lessons learned are reviewed with the Sponsor. | `/pf-close-project` |
| The Sponsor is named by role and person in `organization.md` before the WBS is approved. | `/pf-setup-organization` |
| Any baseline file edited outside a Change Request is reported to the Sponsor within one working day. | `/pf-change-request` |
| Every Change Request states the effect on scope, schedule, cost, and risk, even when the answer is "none". | `/pf-change-request` |

### Scope and schedule

| Example standard | Most relevant to |
|---|---|
| Every deliverable has acceptance criteria that name who accepts it. | `/pf-plan-scope-wbs` |
| No work package is larger than 10 working days; split larger ones. | `/pf-plan-scope-wbs` |
| Every milestone has a named owner. | `/pf-plan-schedule` |
| Schedule changes of more than one week are raised as a Change Request, however small the work package. | `/pf-change-request` |
| Every work package lists its predecessors; none is started while a predecessor is open without the Project Manager's agreement. | `/pf-plan-schedule` |
| Scope is stated as exclusions as well as inclusions, so what is not being done is written down. | `/pf-plan-scope-wbs` |
| Work that is not in the WBS is not started; add it through a Change Request first. | `/pf-plan-scope-wbs` |
| Schedule dates are planned with a buffer before external deadlines, and the buffer is stated. | `/pf-plan-schedule` |

### Cost

| Example standard | Most relevant to |
|---|---|
| Any spend above a stated amount needs the budget holder's written approval before it is committed. | `/pf-plan-cost` |
| Contingency reserve is held by the Sponsor, not the Project Manager. | `/pf-plan-cost` |
| Actual cost is reported in the same currency as the budget baseline. | `/pf-control-cycle` |
| Every cost estimate states its basis (quote, past project, expert judgment); estimates without one stay `TBD`. | `/pf-plan-cost` |
| Cost is reviewed at every control cycle, not only when the budget is nearly spent. | `/pf-control-cycle` |
| Management reserve is released only on the Sponsor's written approval. | `/pf-plan-cost` |

### Risk

| Example standard | Most relevant to |
|---|---|
| Every risk has a named owner and a response before it is accepted. | `/pf-plan-risk` |
| Risks scored at or above a stated level are reviewed with the Sponsor at every control cycle. | `/pf-control-cycle` |
| A risk is closed only with a written reason and a date. | `/pf-plan-risk` |
| Risks are identified with at least two people from different roles, not by the Project Manager alone. | `/pf-plan-risk` |
| A risk that has occurred is moved to the issues in the status report the same cycle. | `/pf-control-cycle` |
| Every risk scored above the acceptance ceiling has a response other than Accept unless the Sponsor signs off. | `/pf-plan-risk` |

### Quality

| Example standard | Most relevant to |
|---|---|
| A work package is not marked Done until the quality gate passes. | `/pf-check-report` |
| Customer-facing content, such as packaging claims or published copy, is reviewed by Legal before release. | `/pf-plan-quality` |
| Every deliverable has a second reviewer who did not produce it. | `/pf-plan-quality` |
| A defect found after a work package is Done reopens it; it is not fixed silently. | `/pf-check-report` |
| Quality criteria are agreed with whoever accepts the deliverable before work starts. | `/pf-plan-quality` |
| A failed quality gate is logged with its cause, not only its result. | `/pf-check-report` |

### Procurement

| Example standard | Most relevant to |
|---|---|
| All vendor contracts are reviewed by Legal before signature. | `/pf-plan-procurement` |
| Purchases above a stated value need at least three quotes. | `/pf-plan-procurement` |
| No work starts with a vendor before the contract is in the register as active. | `/pf-assign-task` |
| Every vendor has a named internal owner who tracks delivery. | `/pf-plan-procurement` |
| Contracts record the notice period and the exit terms before they are signed. | `/pf-plan-procurement` |
| A vendor that misses a deliverable date twice is reviewed with the Sponsor. | `/pf-control-cycle` |

### People, resources, and AI team members

| Example standard | Most relevant to |
|---|---|
| No one is allocated above 80% across all projects. | `/pf-plan-resources` |
| Every AI team member has a named human who is accountable for its output. | `/pf-plan-organization` |
| Ratings of named people in the skill matrix are not shared outside the project. | `/pf-plan-skills` |
| AI team members never send external messages or publish; they prepare drafts for a person to send. | `/pf-start-team-member` |
| Every team member has a named backup for each role they hold alone. | `/pf-plan-organization` |
| Skill gaps found in planning have an owner and an action (train, hire, contract, reassign, or accept) before work starts. | `/pf-plan-skills` |
| No person or AI team member is given a work package until its inputs are available. | `/pf-assign-task` |
| An AI team member's output is reviewed by a person before it is marked Done. | `/pf-check-report` |

### Stakeholders and communications

| Example standard | Most relevant to |
|---|---|
| The stakeholder register is shared only with the Project Manager, the Sponsor, and the Stakeholder Manager. | `/pf-plan-stakeholders` |
| Anything sent to a broad audience is approved by the Sponsor first. | `/pf-plan-stakeholders` |
| Every stakeholder group has a named contact on the project. | `/pf-plan-stakeholders` |
| Stakeholders with high power and high interest are contacted before a decision that affects them, not after. | `/pf-plan-stakeholders` |
| Bad news is communicated to the Sponsor the same day it is known. | `/pf-control-cycle` |
| The communications plan is reviewed when a new stakeholder group joins. | `/pf-plan-stakeholders` |

### Records and documentation

| Example standard | Most relevant to |
|---|---|
| Every Change Request and decision is referenced by its ID in commit messages and status reports. | `/pf-change-request`, `/pf-log-decision` |
| Project files are kept in the team's shared repository, not on personal drives. | all |
| Reference material is written in plain language: no abbreviations without a definition on first use. | all |
| Dates are written in one format across all project files (for example `2026-10-06`). | all |
| Each file has one owner; others propose changes to the owner instead of editing it. | all |
| Meeting outcomes that change a decision, risk, or action are written into the project files within one working day. | `/pf-log-decision` |

### Security and sensitive information

| Example standard | Most relevant to |
|---|---|
| No passwords, keys, or tokens are written into any project file or chat. | all |
| Personal data about named people is limited to what the project needs and is not copied into status reports. | `/pf-control-cycle` |
| Cost figures and risk details are shared outside the project only with the Sponsor's approval. | `/pf-control-cycle` |
| Confidential vendor terms stay in the vendor register and are not repeated elsewhere. | `/pf-plan-procurement` |

### Escalation and issues

| Example standard | Most relevant to |
|---|---|
| A blocked work package is raised to the Project Manager the same day, with what is needed to unblock it. | `/pf-check-report` |
| A blocker open for more than three working days is escalated to the Sponsor. | `/pf-control-cycle` |
| Every issue has a named owner and a due date. | `/pf-control-cycle` |
| Disagreements about scope or priority go to the Sponsor, not to the people doing the work. | `/pf-log-decision` |

### Handover and session continuity

| Example standard | Most relevant to |
|---|---|
| A conversation that is nearly full is handed over with `/pf-session-handoff` before work continues in a new one. | `/pf-session-handoff` |
| A finished stage is archived with `/pf-session-archive-stage` before the next one is planned in detail. | `/pf-session-archive-stage` |
| Nothing is deleted from a project folder; superseded items are marked Superseded. | all |

### Closing and learning

| Example standard | Most relevant to |
|---|---|
| Lessons learned are collected from at least the Sponsor, the Project Manager, and one team member. | `/pf-close-project` |
| Every lesson has a recommendation for the next project, not only an observation. | `/pf-close-project` |
| Open risks, issues, and vendor contracts are listed and handed to a named owner at close. | `/pf-close-project` |

### Agile track (agile-hybrid or lean with ceremonies)

| Example standard | Most relevant to |
|---|---|
| A work item is not pulled into a sprint until it meets the Definition of Ready. | `/pf-agile-sprint-planning` |
| The user accepts or rejects every item at sprint review; nothing is accepted by default. | `/pf-agile-sprint-review` |
| Every retro produces at least one action item with an owner. | `/pf-agile-sprint-retro` |
| Sprint scope changes mid-sprint only with the user's agreement, and the change is noted in the sprint backlog. | `/pf-agile-sprint-planning` |
| The backlog is refined at least once before every sprint planning. | `/pf-agile-backlog-refinement` |
| Standups record blockers; blockers are not left in conversation only. | `/pf-agile-standup` |

## Putting them in `team.md`

Copy the lines you want into the numbered list under **Team Standards** in `.pmo/team.md`, replacing
the example amounts and names with your own:

```markdown
## Team Standards

1. Every Change Request is approved by the Sponsor before a baseline file is edited.
2. All vendor contracts are reviewed by Legal before signature.
3. Status reports go to the Head of the PMO within one working day of each control cycle.
```

At least one standard is required before `/pf-setup-init` pass 2 will run. Start with the two or three
your team already follows; add more through a Change Request when you find a rule you keep repeating.
