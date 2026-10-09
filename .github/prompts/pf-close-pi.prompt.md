---
description: Close a Program Increment — record achieved value, run the PI review, return unfinished items to the backlog and update the roadmap.
---

# /pf-close-pi

Act as the `pf-planner` and `pf-project-manager` agents together. Read `.pmo/pi-plan.md`,
`.pmo/roadmap.md`, `.pmo/tracker.md` and `.pmo/project-constitution.md`; update `.pmo/pi-plan.md`,
`.pmo/roadmap.md`, `.pmo/product-backlog.md`, `.pmo/retro-log.md`, `.pmo/risk-register.md` and
`.pmo/tracker.md`, and write `.pmo/archives/<PI>/pi-plan.md`.

## Steps

1. Check the Workflow Preset in `project-constitution.md`'s Project Defaults. This command is only for
   `pi-cadence`; under any other preset say so and stop. The PI to close is the roadmap row whose
   Status is In Progress; read its `pi-plan.md` and the constitution's PI Practices.
2. Check the PI's work packages in `tracker.md`: each is Done (meeting the Definition of Done in
   `work-package-definitions.md`) or Descoped. For any still open, confirm with the user which items
   carry over to the next PI, and record that in the PI Change Log. The train leaves on its date, so
   do not hold the close for unfinished work. Set each carried-over or dropped work package to
   Descoped in `tracker.md`, with a Variance Notes entry such as "Carried over to the next PI as
   B-002". This is the one case where Descoped needs no Change Request: the work is re-planned as a
   new work package in the next PI, and this keeps `/pf-close-project` from being blocked by an old
   PI's open rows.
3. If PI objectives is Yes: ask for the Achieved Value of each objective (on the same 1-10 scale, from
   the user or the named scorer) and write it in. Never invent it.
4. If PI review is Yes: record in the Review section the demo (what was shown and the feedback), the
   measures, the retrospective (also append an entry to `retro-log.md` with action items) and the
   problems and actions. If it is No, write "Not used".
5. If the PI predictability metric is Yes (it needs PI objectives): run
   `python .github/skills/pf-helper-scripts/scripts/pf_rules.py --metric pi_predictability_pct`, or work
   it out by hand as the sum of Achieved Value over the sum of Business Value of the Committed
   objectives, as a percentage, and write it under Measures.
6. If ROAM risk handling is Yes: update each risk's ROAM status; close a Resolved risk in
   `risk-register.md` with a reason and date.
7. Move unfinished backlog items back to `product-backlog.md` (Status Not Started, Target PI blank or
   the next PI), set the PI's roadmap Status to Closed once the user confirms, and add the amendments
   rows this needs (today's date, a one-line change; ask only who approves).
8. Copy the finished `pi-plan.md` to `archives/<PI>/pi-plan.md` (for example `archives/PI-1/pi-plan.md`)
   so the PI's objectives, scores and review are kept; `/pf-plan-pi` replaces the live file for the
   next PI.
9. Suggest `/pf-session-archive-stage` to archive the PI's finished work (use the PI id as the stage
   label), and tell the user the next command is `/pf-plan-pi` to plan the next PI, or
   `/pf-close-project` at the end of the year.
