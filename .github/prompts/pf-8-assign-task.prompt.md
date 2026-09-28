---
description: Select the next work package and write a self-contained Task Prompt to the Worker's bus.
---

# /pf-8-assign-task

Act as the `pf-project-manager` agent. Read `tracker.md`, `schedule.md`, and `raci.md`; write
`.pmo/bus/<worker>/task.md`.

## Steps

1. Select the next eligible work package: Status = "Not Started" in `tracker.md`, and all its
   `schedule.md` predecessors are already "Done".
2. Identify the Responsible Worker from `raci.md` for that work package.
3. Write `bus/<worker>/task.md` using `templates/work-package.template.md`, filled in with:
   objective, WBS Dictionary description, acceptance criteria, constraints/guiding notes,
   dependencies already satisfied, and exact reporting instructions (write to
   `bus/<worker>/report.md`, log to `memory/work-packages/WP-<id>.md`).
4. Update `tracker.md`: set the work package's Status to "In Progress" and record the assignment
   date.
5. Tell the user to open a new conversation for that Worker and run `/pf-9-initiate-worker`.
