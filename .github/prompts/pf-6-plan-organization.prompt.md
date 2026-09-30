---
description: Build the RACI matrix mapping WBS work packages to roles/Workers.
---

# /pf-6-plan-organization

Act as the `pf-project-manager` agent (see `.github/agents/project-manager.agent.md`). Read
`.pmo/wbs.md`; produce `.pmo/raci.md`.

## Steps

1. List every leaf work package from `wbs.md` as a row.
2. With the user, define the roles/Workers involved (e.g., `worker-backend`, `worker-frontend`,
   `worker-docs`) as columns — these are the Worker identities used later in `bus/<worker>/`.
3. For each work package × role cell, assign Responsible, Accountable, Consulted, or Informed.
   Every work package must have exactly one Accountable owner.
4. Cross-check: every Worker identity used here must exist as a `bus/<worker>/` folder path when
   tasks are assigned later — flag any mismatch.
5. Run `pf_validate.py --pmo .pmo` (see the `pf-helper-scripts` skill) and fix any RACI FAIL —
   the one-Accountable rule is easy to miss by eye. If the script can't be run, re-read every row
   for exactly one Accountable.
6. Present the RACI matrix for review.
7. Tell the user the next command is `/pf-6b-plan-resources` (Optional under agile-hybrid and
   lean — offer `/pf-7-initiate-manager` if the user skips it).
