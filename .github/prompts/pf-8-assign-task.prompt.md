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
3. Run the Definition of Ready check before anything is dispatched. Every item must pass:
   - The WBS Dictionary gives the work package testable acceptance criteria.
   - `raci.md` names a Responsible party (a Worker, or the vendor per
     `vendor-contract-register.md`) and exactly one Accountable.
   - Everything the Worker needs — inputs, constraints, related artifacts — is stated or linked,
     so nothing has to be guessed.
   - If `quality-management-plan.md` exists, its QA Gate Criteria cover this deliverable type.
   - If `resource-management-plan.md` exists, the assignee is not over-allocated in
     `resource-allocation.md`.
   - If the work is vendor-owned, its contract in `vendor-contract-register.md` is active.
   - Any project-level Definition of Ready additions in `constitution.md` are met.
   If any item fails, do not write the task. Tell the user which item failed and who fixes it
   (acceptance criteria → Planner; RACI → Project Manager; capacity → Resource Manager; contract
   → Procurement Manager). The user may explicitly waive a failed item; record the waiver, don't
   skip the item silently.
4. Write `bus/<worker>/task.md` using `templates/work-package.template.md`, filled in with:
   objective, WBS Dictionary description, acceptance criteria, constraints/guiding notes,
   dependencies already satisfied, the Definition of Ready result (Passed, or Passed with waiver
   plus what was waived), and exact reporting instructions (write to
   `bus/<worker>/report.md`, log to `memory/work-packages/WP-<id>.md`).
5. Update `tracker.md`: set the work package's Status to "In Progress" and record the assignment
   date.
6. Tell the user to open a new conversation for that Worker and run `/pf-9-initiate-worker`.
