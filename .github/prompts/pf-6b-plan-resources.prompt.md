---
description: Plan resource capacity, calendars, and allocation across work packages before execution begins.
---

# /pf-6b-plan-resources

Act as the `pf-resource-manager` agent (see `.github/agents/resource-manager.agent.md`). Read
`.pmo/wbs.md`, `.pmo/raci.md`, and `.pmo/schedule.md`; produce `.pmo/resource-management-plan.md`
from `templates/resource-management-plan.template.md`, and create `.pmo/resource-allocation.md`
from `templates/resource-allocation.template.md` if it doesn't exist yet.

## Steps

1. Require an approved `raci.md` — if missing, point the user to `/pf-6-plan-organization`.
2. For every leaf work package, identify the role/resource responsible (from `raci.md`) and ask
   the user for an effort estimate and acquisition approach (existing team / new hire /
   contractor), noting any lead time.
3. Build a resource calendar with the user for each resource: availability, planned time off,
   part-time %. Never invent availability — mark `TBD` if unknown.
4. Roll demand (from work packages) up against supply (from calendars) per resource per period;
   flag any resource over-allocated beyond 100% before treating the plan as baseline.
5. Agree a utilization threshold with the user that should trigger escalation or re-leveling.
6. Present the Resource Management Plan to the user for review before treating it as baseline.
7. Tell the user Planning is complete and the next command is `/pf-7-initiate-manager`.
