---
description: Select the next work package(s) and write a self-contained Task Prompt to each Worker's bus. Dispatches a single work package, or a batch of independent ones in one action.
---

# /pf-8-assign-task

Act as the `pf-project-manager` agent. Read `tracker.md`, `schedule.md`, and `raci.md`; write
`.pmo/bus/<worker>/task.md` for each work package dispatched.

## Steps

1. Build the eligible set: Status = "Not Started" in `tracker.md`, and all `schedule.md`
   predecessors already "Done". If the Agile ceremony layer is in use and `sprint-backlog.md` has
   a current sprint, only work packages in that sprint are eligible.
2. Choose what to dispatch. Default to the single next eligible work package by schedule. If more
   than one is eligible, offer a batch — or use one if the user already asked for it — chosen
   under these independence rules:
   - One work package per Worker. If two eligible packages share a Responsible Worker, the earlier
     by schedule goes in the batch and the other stays queued.
   - Assignees across the whole batch together must stay within capacity in
     `resource-allocation.md` (when `resource-management-plan.md` exists).
   - If two packages look like they touch the same deliverable or file, don't guess — ask the
     user whether they can safely run in parallel.
3. For each work package chosen, identify the Responsible Worker from `raci.md`, then run the
   Definition of Ready check. Every item must pass:
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
   If any item fails, that work package is not dispatched and the rest of the batch is unaffected.
   Tell the user which item failed and who fixes it (acceptance criteria → Planner; RACI →
   Project Manager; capacity → Resource Manager; contract → Procurement Manager). The user may
   explicitly waive a failed item; record the waiver, don't skip the item silently.
4. Present the proposed dispatch to the user before writing anything: each work package, its
   Worker, and its Definition of Ready result. The user approves the list, or removes items.
   Approving the batch approves each assignment in it.
5. For each approved work package, write `bus/<worker>/task.md` using
   `templates/work-package.template.md`, filled in with: objective, WBS Dictionary description,
   acceptance criteria, constraints/guiding notes, dependencies already satisfied, the Definition
   of Ready result (Passed, or Passed with waiver plus what was waived), and exact reporting
   instructions (write to `bus/<worker>/report.md`, log to `memory/work-packages/WP-<id>.md`).
6. Update `tracker.md` for every dispatched work package: Status "In Progress" and the assignment
   date.
7. Tell the user to open one new conversation per dispatched Worker and run
   `/pf-9-initiate-worker` in each, listing which Worker takes which work package. Each Worker
   reports back separately, so run `/pf-10-check-report` once per report.
