---
description: Decompose the approved Charter into a Scope Statement and Work Breakdown Structure.
---

# /pf-2-plan-scope-wbs

Act as the `pf-planner` agent. Read `.pmo/charter.md` and produce `.pmo/scope-statement.md` and
`.pmo/wbs.md`.

## Steps

1. Require an approved `charter.md` — if it's missing or still in draft, stop and point the user
   to `/pf-1-initiate-planner`.
2. Draft the Scope Statement: project scope description, deliverables, acceptance criteria at the
   deliverable level, exclusions, constraints, assumptions. Confirm with the user.
3. Decompose each deliverable into a Work Breakdown Structure:
   - Use a numbered hierarchical outline (1, 1.1, 1.1.1, ...).
   - Apply the 100% rule: the WBS must represent all the work, with no gaps or overlaps.
   - Stop decomposing when a work package is sized for one Worker to complete and report on as a
     single reviewable increment.
   - For every leaf work package, write a WBS Dictionary entry: description, deliverable,
     acceptance criteria, and an owner placeholder (filled in later by `/pf-6-plan-organization`).
4. Present the WBS to the user for review before treating it as baseline.
5. Tell the user the next command is `/pf-3-plan-schedule`.
