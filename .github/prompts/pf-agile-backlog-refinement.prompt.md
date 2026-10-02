---
description: Groom upcoming WBS work packages into sprint-ready state ahead of the next Sprint Planning (Agile ceremony layer).
---

# /pf-agile-backlog-refinement

Act as the `pf-scrum-master` agent. Read `wbs.md` and `tracker.md`; update
`.pmo/sprint-backlog.md`'s Upcoming Sprint Candidates section.

## Steps

1. Identify the next 1–2 sprints' worth of not-yet-started work packages from `wbs.md`.
2. For each, run the Definition of Ready check from `/pf-assign-task` step 3 — except the
   predecessors-Done test, which isn't expected to hold yet. Do not invent an acceptance
   criterion the Planner hasn't stated; flag it back to the Planner instead. Note any open
   question.
3. Record refinement notes and a Ready/Not Ready flag in `sprint-backlog.md`'s Upcoming Sprint
   Candidates table using `templates/sprint-backlog.template.md`. Ready means every checked item
   passed; Not Ready notes which item failed.
4. Tell the user refinement is complete and the next ceremony is `/pf-agile-sprint-planning` at the
   start of the next sprint.
