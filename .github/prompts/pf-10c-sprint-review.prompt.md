---
description: Review the sprint's completed work packages with the user (acting as Product Owner) and record acceptance before the retro (Agile ceremony layer).
---

# /pf-10c-sprint-review

Act as the `pf-scrum-master` agent. Read `sprint-backlog.md`'s current sprint and `tracker.md`;
update `sprint-backlog.md`'s Sprint Review Outcome column.

ProjectFabric has no dedicated Product Owner agent — the user plays that role here, per Design
Principle 3 (the user is the checkpoint). This ceremony is where that acceptance authority is
exercised explicitly, rather than implicitly via `tracker.md`'s Done status alone.

## Steps

1. For each work package in the current sprint marked "Done" in `tracker.md` (see
   `/pf-10-check-report`), show the user its WBS Dictionary acceptance criteria and ask them to
   accept or reject it as Product Owner — do not assume acceptance just because a QA gate passed.
2. Record the outcome per work package in `sprint-backlog.md`'s Sprint Review Outcome column:
   Accepted, or Rejected (rework needed).
3. For any Rejected item, tell the user whether it needs the Project Manager to reopen the work
   package's `tracker.md` status (rework within existing scope) or a Change Request
   (`/pf-12-change-request`, if the rejection implies the acceptance criteria themselves were
   wrong or incomplete) — never silently reopen or silently edit baseline documents yourself.
4. Tell the user the review is logged and the next ceremony is `/pf-11b-sprint-retro`.
