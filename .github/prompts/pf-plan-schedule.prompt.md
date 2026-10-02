---
description: Sequence WBS work packages into a schedule with dependencies and milestones.
---

# /pf-plan-schedule

Act as the `pf-planner` agent. Read `.pmo/wbs.md` and produce `.pmo/schedule.md`.

## Steps

1. Require an approved `wbs.md` — if missing, point the user to `/pf-plan-scope-wbs`.
2. For every leaf work package, identify its predecessors (which other work packages must
   complete first) based on genuine logical or resource dependency, not assumed ordering.
3. Define milestones: meaningful points where a deliverable or phase completes, each with a
   target date only if the user provides one or explicitly asks for an estimate — otherwise
   express milestones in relative sequence.
4. Identify the critical path in plain language: the chain of dependent work packages with no
   slack, i.e. the one that determines the earliest possible finish.
5. Present the schedule to the user for review before treating it as baseline.
6. Tell the user the next command is `/pf-plan-cost`.
