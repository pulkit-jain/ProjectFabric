---
description: Plan the next Program Increment in detail — backlog ranking, objectives, confidence, risks — and write the PI plan.
---

# /pf-plan-pi

Act as the `pf-planner` agent (see `.github/agents/planner.agent.md`). Read `.pmo/roadmap.md`,
`.pmo/project-constitution.md`, `.pmo/product-backlog.md` and `.pmo/risk-register.md`; produce
`.pmo/pi-plan.md` and update `.pmo/product-backlog.md`.

## Steps

1. Check the Workflow Preset in `project-constitution.md`'s Project Defaults. This command is only for
   `pi-cadence`; under any other preset say so and stop. Require `roadmap.md` (else point the user to
   `/pf-plan-roadmap`) and read the constitution's PI Practices: PI length, iteration length and which
   practices are Yes. If a needed value is blank, ask for it and stop until it is filled in.
2. Find the next PI: the first roadmap row whose Status is Planned. The previous PI must be Closed;
   if it is not, stop and point the user to `/pf-close-pi`, unless the user explicitly says the PIs may
   overlap (record that in the PI Change Log).
3. Backlog: create `product-backlog.md` from `templates/product-backlog.template.md` if it does not
   exist. Bring the items for this PI into shape with the user (the roadmap theme, a one-line item,
   Type). If WSJF prioritization is Yes, ask for each feature's Cost of Delay and Job Size on a
   relative scale the user chooses, calculate WSJF = Cost of Delay / Job Size, and rank by it; never
   invent either number. If it is No, rank in the order the user gives.
4. Capacity: ask the user for the capacity of each iteration (or cross-reference `resource-allocation.md`
   if it exists) and select items in rank order up to that capacity — never overcommit by guessing. The
   line between items inside capacity and items below it is the cut line: inside is Committed, below is
   Uncommitted.
5. If PI objectives is Yes: for each objective record the text, a Business Value (1-10) and who scored
   it, the team's Confidence vote (1-5) as the user gives it, and Committed or Uncommitted. Never invent
   a score or a vote. If it is No, write "Not used" in that section.
6. If ROAM risk handling is Yes: list the risks raised in planning, add each new one to
   `risk-register.md` (or tell the user to route it to the Risk Manager), and give each a ROAM status
   (Resolved / Owned / Accepted / Mitigated) and an owner. If it is No, write "Not used".
7. If `pi-plan.md` already exists for an earlier PI, check that `archives/<PI>/pi-plan.md` holds a copy
   (`/pf-close-pi` writes it); if not, copy it there first. Never overwrite a plan that is not
   archived. Then write `pi-plan.md` from `templates/pi-plan.template.md` and update the PI's `product-backlog.md`
   Target PI column. Present both to the user for review; once approved, set the PI's roadmap Status to
   In Progress.
8. Tell the user the next command is `/pf-plan-scope-wbs`, to add this PI's work packages as a new
   top-level branch of `wbs.md`; then `/pf-plan-schedule` for its iterations, `/pf-plan-organization` to
   add the new work packages to `raci.md`, `/pf-start-manager` to add them to `tracker.md`, and
   `/pf-agile-sprint-planning` for the first iteration.
