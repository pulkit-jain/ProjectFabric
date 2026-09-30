---
description: Establish project-specific working agreements — decision authority, cadence, escalation rules — before planning begins.
---

# /pf-0b-constitution

Act as the `pf-planner` agent (see `.github/agents/planner.agent.md`). Produce
`.pmo/constitution.md`.

This sits above individual artifacts and below the framework-wide `.github/copilot-instructions.md`:
copilot-instructions.md governs how ProjectFabric agents behave on every project;
`constitution.md` governs how *this* project's people and agents make decisions. If `.pmo/team.md`
exists, it sits between the two — read it first, and don't restate anything it already covers.

## Steps

0. Read `.pmo/team.md` if it exists. Team Defaults (decision thresholds, cadence) and Team
   Standards already apply to this project; propose them as starting points rather than asking
   from scratch. If the user wants this project to deviate from a team item, record it under the
   constitution's "Overrides of team.md" section with a reason — never silently contradict it.

1. Ask the user for this project's non-negotiable principles — rules that override default
   agent behavior specifically for this project (e.g. "no scope change without sponsor sign-off",
   "all vendor commitments need Legal review"). Don't invent principles; if the user has none
   beyond the framework defaults, say so explicitly rather than padding the list.
2. Establish Decision Authority: who can approve scope, schedule, budget, and risk-acceptance
   decisions, and at what threshold escalation is required.
3. Agree a Reporting Cadence — how often `/pf-11-control-cycle` should run (e.g. weekly) and who
   must review each Status Report.
4. Agree Escalation Rules — the conditions under which a deviation becomes a Change Request
   (`/pf-12-change-request`) rather than being absorbed silently. Cross-reference thresholds
   already set in `cost-management-plan.md` and `risk-register.md` once they exist, rather than
   duplicating numbers.
5. Capture a project-level Definition of Done — what "closed" means for this project overall,
   beyond individual work package acceptance criteria.
6. Present the Constitution to the user for review before treating it as baseline. Once approved,
   changes go through the same Change Control as other baseline documents (Ground Rule 5).
7. Tell the user the next command is `/pf-1-initiate-planner`.
