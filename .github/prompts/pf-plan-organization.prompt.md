---
description: Finalise roles and the team roster against the skill gaps, then build the RACI matrix with named team members.
---

# /pf-plan-organization

Act as the `pf-project-manager` agent (see `.github/agents/project-manager.agent.md`). Read
`.pmo/wbs.md`, `.pmo/organization.md`, and `.pmo/skill-matrix.md` (if they exist); update
`.pmo/organization.md` and produce `.pmo/raci.md`.

## Steps

1. Require an approved `wbs.md`. If `organization.md` is missing and the Workflow Preset in
   `project-constitution.md`'s Project Defaults requires it, point the user to `/pf-setup-organization`; under lean the RACI
   may use names directly and the roster checks below are skipped.
2. Read the Gap Analysis in `skill-matrix.md`, if present. For each open gap, work with the user
   on the roster: add a Proposed or Open member (or a Vendor) to fill it, change a member's role,
   or record that the user accepted the gap. Never invent a person, allocation, or contract.
3. Settle the Team Roster: every member has a Member ID, Type (Person, AI, or Vendor), Role(s),
   Allocation, and Status. Log each roster change in the Org Change Log. If a roster change
   alters skill coverage, tell the user to re-run `/pf-plan-skills` so the Resource Manager
   updates `skill-matrix.md`.
4. List every leaf work package from `wbs.md` as a RACI row (if `raci.md` already has rows, keep
   them and add only the leaves that have none, for example a new PI's branch), and use the Member IDs from the
   roster (plus Project Manager and Sponsor) as columns. Use the Role Definitions to propose who
   is Responsible; the user decides. See the `pf-raci-facilitation-reference` skill if the
   exercise gets stuck.
5. For each work package × column cell, assign Responsible, Accountable, Consulted, or Informed.
   Every work package must have exactly one Accountable.
6. Cross-check: every RACI column is a Member ID in the roster; every AI member has (or will
   have) a `bus/<member>/` folder of that name; a Vendor Responsible party has a contract in
   `vendor-contract-register.md` when one exists.
7. Run `pf_validate.py --pmo .pmo` (see the `pf-helper-scripts` skill) and fix any RACI or
   Organization FAIL — the one-Accountable rule is easy to miss by eye. If the script can't be
   run, re-read every row for exactly one Accountable.
8. Present `organization.md` and the RACI matrix for review.
9. Tell the user the next command is `/pf-plan-resources` (Optional under agile-hybrid and
   lean — offer `/pf-start-manager` if the user skips it).
