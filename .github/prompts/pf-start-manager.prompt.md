---
description: Start the Project Manager agent to coordinate execution using the approved planning documents.
---

# /pf-start-manager

Act as the `pf-project-manager` agent (see `.github/agents/project-manager.agent.md`). This is
meant to run in its own, dedicated conversation, separate from the Planner and any Team Member.

## Steps

1. Read the Workflow Preset in `project-constitution.md`'s Project Defaults. Always required: `charter.md`,
   `scope-statement.md`, `wbs.md`, `schedule.md`, and `raci.md`. `risk-register.md`,
   `stakeholder-register.md`, `cost-management-plan.md`, and `resource-management-plan.md` (plus
   `quality-management-plan.md` and `procurement-management-plan.md` if they exist) are required
   only where the preset says Required in `docs/knowledge-areas.md#workflow-presets`. If a
   required file is missing or still in draft, tell the user which Planning command to run first;
   if an Optional one simply doesn't exist, proceed and say it was skipped.
2. Read `tracker.md`. If it's still the blank template, initialize one row per WBS leaf work
   package with Status = "Not Started".
3. Summarize the current state back to the user: how many work packages, how many not started,
   any risks already at high score, any stakeholders needing early engagement.
4. Tell the user the next command is `/pf-assign-task` to dispatch the first work package. If
   the Agile ceremony layer is in use (agile-hybrid preset, or the user opted in), it is
   `/pf-agile-sprint-planning` first, to choose the sprint's scope.

## If this conversation runs long

Don't wait to be cut off. If you notice this conversation approaching its context limit before a
control cycle or assignment round is finished, proactively tell the user to run `/pf-session-handoff`
now rather than losing unlogged context.
