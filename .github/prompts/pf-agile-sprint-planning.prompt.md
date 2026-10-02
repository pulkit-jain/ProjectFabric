---
description: Select the sprint's scope from the WBS backlog and agree a sprint goal (Agile ceremony layer).
---

# /pf-agile-sprint-planning

Act as the `pf-scrum-master` agent. Read `constitution.md`, `wbs.md`, `tracker.md`, and (if it
exists) `resource-allocation.md`; write `.pmo/sprint-backlog.md`.

## Steps

1. Check `constitution.md`'s Workflow Preset. Under classic-waterfall or lean, ask once whether
   this ceremony is actually wanted before proceeding (see
   `docs/knowledge-areas.md#workflow-presets`); under agile-hybrid, proceed directly.
2. From `wbs.md`, list leaf work packages not yet "Done" in `tracker.md` whose predecessors (per
   `schedule.md`) are already satisfied — these are sprint-eligible.
3. Agree the sprint boundary dates and a sprint goal with the user.
4. Ask the user (or cross-reference `resource-allocation.md` if it exists) how much capacity is
   available this sprint; select work packages up to that capacity — never overcommit by guessing.
5. Write the selected scope and goal to `sprint-backlog.md` using
   `templates/sprint-backlog.template.md`'s current-sprint section.
6. Tell the user the next command is `/pf-assign-task` to start dispatching the sprint's work
   packages to Team Members.
