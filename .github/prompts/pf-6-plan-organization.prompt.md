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
5. Present the RACI matrix for review.
6. Tell the user the next command is `/pf-6b-plan-resources`.
