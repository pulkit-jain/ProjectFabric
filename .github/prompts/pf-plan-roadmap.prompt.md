---
description: Build or re-plan the yearly roadmap (themes and planned Program Increments) for a pi-cadence product.
---

# /pf-plan-roadmap

Act as the `pf-planner` agent (see `.github/agents/planner.agent.md`). Read `.pmo/charter.md` and
`.pmo/project-constitution.md`; produce `.pmo/roadmap.md` from `templates/roadmap.template.md`.

## Steps

1. Check the Workflow Preset in `project-constitution.md`'s Project Defaults. This command is only for
   `pi-cadence`; under any other preset say so and stop. Require an approved `charter.md` — if it is
   missing or still in draft, point the user to `/pf-setup-charter`.
2. If `roadmap.md` is still the blank template, ask the user for the product name and the period it
   covers, the themes (the outcome wanted for each, not a feature list), and the PIs in the period:
   id, start and end (only if the user gives dates; otherwise relative weeks), a one-line focus, and
   Confidence (Committed / Planned / Tentative). Only the next PI should be Committed or Planned;
   later PIs stay Tentative and rough. Never invent dates, themes or confidence. If PI length is blank
   in the constitution's PI Practices, ask for it and note it there.
3. If a roadmap already exists, this is a re-plan: show it, apply the changes the user gives, and add a
   row to the Revision Log (today's date and a one-line change; ask the user only who approved it and
   never fill that in yourself). A re-plan is not a Change Request, except that moving the dates of a PI
   already In Progress is, so send the user to `/pf-change-request` for that.
4. Present the roadmap to the user for review.
5. Tell the user the next command is `/pf-plan-pi`, to plan the next PI in detail.
