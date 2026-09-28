---
description: Start the Project Manager agent to coordinate execution using the approved planning documents.
---

# /pf-7-initiate-manager

Act as the `pf-project-manager` agent (see `.github/agents/project-manager.agent.md`). This is
meant to run in its own, dedicated conversation, separate from the Planner and any Worker.

## Steps

1. Read `charter.md`, `scope-statement.md`, `wbs.md`, `schedule.md`, `cost-management-plan.md`,
   `risk-register.md`, `stakeholder-register.md`, `raci.md`, and `resource-management-plan.md`.
   If any are missing or still in draft, tell the user which Planning command to run first.
2. Read `tracker.md`. If it's still the blank template, initialize one row per WBS leaf work
   package with Status = "Not Started".
3. Summarize the current state back to the user: how many work packages, how many not started,
   any risks already at high score, any stakeholders needing early engagement.
4. Tell the user the next command is `/pf-8-assign-task` to dispatch the first work package.

## If this conversation runs long

Don't wait to be cut off. If you notice this conversation approaching its context limit before a
control cycle or assignment round is finished, proactively tell the user to run `/pf-13-handoff`
now rather than losing unlogged context.
