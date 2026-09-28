---
description: Scaffold the .pmo/ project management state directory from templates.
---

# /pf-0-init

Scaffold the project's `.pmo/` directory so every ProjectFabric agent has somewhere to read and
write state.

## Steps

1. Check whether `.pmo/` already exists. If it does, list its contents and ask the user whether
   to leave it alone (default), or which specific files to re-scaffold — never overwrite existing
   project artifacts silently.
2. Create the following structure, copying each file from `templates/` (strip the `.template`
   suffix) and leaving placeholder fields intact for the owning agent to fill in later:
   ```
   .pmo/
     constitution.md
     charter.md
     scope-statement.md
     wbs.md
     schedule.md
     cost-management-plan.md
     cost-performance.md
     risk-register.md
     stakeholder-register.md
     raci.md
     communications-plan.md
     tracker.md
     bus/               (empty — populated per-Worker by /pf-8-assign-task)
     memory/
       work-packages/   (empty — populated by Workers)
     reports/           (empty — populated by /pf-11-control-cycle)
     changes/           (empty — populated by /pf-12-change-request)
     closing/           (empty — populated by /pf-14-close-project)
   ```
3. Confirm the structure was created and tell the user the next command is
   `/pf-0b-constitution` (or `/pf-1-initiate-planner` directly if the user wants to skip the
   constitution step for a lightweight project).
