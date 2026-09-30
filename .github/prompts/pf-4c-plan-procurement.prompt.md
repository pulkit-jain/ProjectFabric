---
description: Run make-or-buy analysis, choose contract types, and set procurement risk thresholds — produce the Procurement Management Plan.
---

# /pf-4c-plan-procurement

Act as the `pf-procurement-manager` agent (see `.github/agents/procurement-manager.agent.md`).
Read `.pmo/wbs.md`, `.pmo/cost-management-plan.md`, and `.pmo/risk-register.md` (if it exists);
produce `.pmo/procurement-management-plan.md` from
`templates/procurement-management-plan.template.md`, and create `.pmo/vendor-contract-register.md`
from `templates/vendor-contract-register.template.md` if it doesn't exist yet.

## Steps

1. Require an approved `wbs.md` — if missing, point the user to `/pf-2-plan-scope-wbs`.
2. For every deliverable or work package where outsourcing is plausible, run a make-or-buy
   analysis with the user — cost, capability, timeline, and control trade-offs. If nothing is
   plausibly outsourced, say so explicitly and keep this section short rather than padding it.
3. For each "Buy" item, agree vendor selection criteria and a contract type (fixed-price, time &
   materials, cost-reimbursable) that fits the risk allocation the user wants.
4. Identify candidate procurement risks (vendor delay, vendor failure, contract dispute) and tell
   the user to route them to the Risk Manager (`/pf-4-plan-risk` re-run, or added directly to
   `risk-register.md`) rather than tracking them separately.
5. Agree procurement control thresholds with the user — the delivery delay or contract variance
   that should trigger a Change Request rather than silent absorption.
6. Present the Procurement Management Plan to the user for review before treating it as baseline.
7. Tell the user the next command is `/pf-5-plan-stakeholders`.
