---
description: Select the next work package(s) and write a self-contained Task Prompt to each Team Member's bus. Dispatches a single work package, or a batch of independent ones in one action.
---

# /pf-assign-task

Act as the `pf-project-manager` agent. Read `tracker.md`, `schedule.md`, and `raci.md`; write
`.pmo/bus/<member>/task.md` for each work package dispatched.

## Steps

1. Build the eligible set: Status = "Not Started" in `tracker.md`, and all `schedule.md`
   predecessors already "Done". If the Agile ceremony layer is in use and `sprint-backlog.md` has
   a current sprint, only work packages in that sprint are eligible.
2. Choose what to dispatch. Default to the single next eligible work package by schedule. If more
   than one is eligible, offer a batch — or use one if the user already asked for it — chosen
   under these independence rules:
   - One work package per Team Member. If two eligible packages share a Responsible Team Member, the earlier
     by schedule goes in the batch and the other stays queued.
   - Assignees across the whole batch together must stay within capacity in
     `resource-allocation.md` (when `resource-management-plan.md` exists).
   - If two packages look like they touch the same deliverable or file, don't guess — ask the
     user whether they can safely run in parallel.
3. For each work package chosen, identify the Responsible Team Member from `raci.md`, then run the
   Definition of Ready check: every row of the Definition of Ready table in
   `work-package-definitions.md` must pass (the standard checks plus any this project added).
   If any row fails, that work package is not dispatched and the rest of the batch is unaffected.
   Tell the user which check failed and who fixes it (the table's "If it fails, goes to" column). The
   user may explicitly waive a failed check; record the waiver, don't skip the check silently.
4. Present the proposed dispatch to the user before writing anything: each work package, its
   Team Member, and its Definition of Ready result. The user approves the list, or removes items.
   Approving the batch approves each assignment in it.
5. For each approved work package, write `bus/<member>/task.md` using
   `templates/work-package.template.md`, filled in with: objective, WBS Dictionary description,
   acceptance criteria, constraints/guiding notes, dependencies already satisfied, the Definition
   of Ready result (Passed, or Passed with waiver plus what was waived), and exact reporting
   instructions (write to `bus/<member>/report.md`, log to `memory/work-packages/WP-<id>.md`).
   Only AI members use the bus. For a Person or Vendor member, prepare the same brief, show it to
   the user to hand over, and note that the user brings progress back through `/pf-check-report`.
6. Update `tracker.md` for every dispatched work package: Status "In Progress" and the assignment
   date.
7. Tell the user to open one new conversation per dispatched AI Team Member and run
   `/pf-start-team-member` in each, listing which Team Member takes which work package. Each Team Member
   reports back separately, so run `/pf-check-report` once per report.
