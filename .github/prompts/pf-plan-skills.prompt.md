---
description: Build the skills catalog, map skill requirements to work packages, assess team coverage, and analyse gaps.
---

# /pf-plan-skills

Act as the `pf-resource-manager` agent (see `.github/agents/resource-manager.agent.md`). Read
`.pmo/wbs.md`, `.pmo/organization.md`, and `.pmo/constitution.md`; produce `.pmo/skill-matrix.md`
from `templates/skill-matrix.template.md`.

## Steps

1. Require an approved `wbs.md` — if missing, point the user to `/pf-plan-scope-wbs`.
2. Read the Workflow Preset in `constitution.md`. This phase is Required under classic-waterfall
   and agile-hybrid and Optional under lean (see
   [docs/knowledge-areas.md](../../docs/knowledge-areas.md#workflow-presets)). For Optional, ask
   once whether a skills assessment is worth it; if the user skips it, say so in one line and
   offer `/pf-plan-organization`.
3. If `organization.md` is missing, tell the user the roster is the source of Member IDs and
   point to `/pf-setup-organization` (or continue with an empty Team Coverage section).
4. Build the Skills Catalog with the user from the WBS Dictionary and the Role Definitions: the
   distinct skills the project needs, each with a Skill ID and category. For ideas, ask by
   deliverable type rather than inventing skills.
5. Fill Requirements: for each WBS leaf, the skill(s) it needs and the minimum level (1-4, see
   the Proficiency Scale in the template).
6. Fill Team Coverage for every roster member the user can assess. Ask for each level and its
   Source; never guess a rating — leave `TBD`. AI members are rated the same way, by what the
   user has seen them do.
7. Fill the Gap Analysis: for each skill whose best rostered member (Status Confirmed or
   Proposed) is below the highest minimum level required, record the gap and propose an Action —
   Train, Hire, Contract, Reassign, or Accept. The user chooses; do not decide.
8. Update the Required Skills column in `organization.md`'s Role Definitions by proposing the
   change to the Project Manager (Ground Rule 2) — do not edit that file yourself.
9. Run `pf_validate.py --pmo .pmo` (see the `pf-helper-scripts` skill) and fix any Skills FAIL.
10. Present the Skill Matrix for review, and tell the user the next command is
    `/pf-plan-organization`.
