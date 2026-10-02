---
description: Define the project's governance structure and role definitions, and start the team roster.
---

# /pf-setup-organization

Act as the `pf-project-manager` agent (see `.github/agents/project-manager.agent.md`). Read
`.pmo/charter.md` and `.pmo/constitution.md`; produce `.pmo/organization.md` from
`templates/organization.template.md`.

## Steps

1. Require an approved `charter.md` — if missing, point the user to `/pf-setup-charter`.
2. Read the Workflow Preset in `constitution.md`. This phase is Required under classic-waterfall
   and agile-hybrid and Optional under lean (see
   [docs/knowledge-areas.md](../../docs/knowledge-areas.md#workflow-presets)). For Optional, ask
   once whether a formal governance structure and roster are worth it for this project; if the
   user skips it, say so in one line and offer `/pf-plan-scope-wbs`.
3. If `.pmo/organization.md` does not exist, create it from the template.
4. Build the Governance Structure with the user, using the Sponsor and stakeholders named in the
   Charter as the starting point: who sponsors, who manages, who can approve a Change Request,
   what each body decides, how often it meets, and the escalation path. Never invent a name or a
   decision right — leave `TBD` and ask.
5. Define Role Definitions: the jobs the project needs done, each with its responsibilities and
   headcount. Leave Required Skills blank; `/pf-plan-skills` fills them in once the WBS exists.
6. Start the Team Roster with the people the user already knows about. For each member record a
   Member ID, Type, Role, and Status:
   - **Person**: a human on the team.
   - **AI**: an agent session that executes work packages; its Member ID becomes its
     `bus/<member>/` folder name.
   - **Vendor**: an outside company; note its contract in `vendor-contract-register.md` once the
     Procurement Manager has created it.
   Mark anyone not yet agreed as Proposed, and any role with nobody named as Open.
7. Present `organization.md` for review. On approval, the Governance Structure and Role
   Definitions are baseline (Ground Rule 5); the Team Roster stays a living register.
8. Tell the user the next command is `/pf-plan-scope-wbs`.
