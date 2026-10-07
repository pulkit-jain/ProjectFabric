---
description: Choose a cost tracking mode, estimate costs per work package, and baseline the project budget.
---

# /pf-plan-cost

Act as the `pf-cost-manager` agent (see `.github/agents/cost-manager.agent.md`). Read
`.pmo/wbs.md` and `.pmo/schedule.md` (and `.pmo/risk-register.md` if it already exists); produce
`.pmo/cost-management-plan.md`.

## Steps

1. Require an approved `wbs.md` — if missing, point the user to `/pf-plan-scope-wbs`.
2. Ask the user to choose a tracking mode — **Lightweight** (budget vs. actual) or **Full EVM**
   (PV/EV/AC with CPI/SPI) — and record the choice and rationale.
3. For every leaf work package, ask the user for an estimating basis and a cost estimate. Never
   invent a number — if the user doesn't know yet, mark it `TBD` rather than guessing.
4. Roll estimates up into a budget baseline; add a contingency reserve (cross-reference
   `risk-register.md` if it exists yet) and a management reserve; compute the Total Project Budget.
5. Agree cost control thresholds with the user — the variance (% or absolute) that should trigger
   a Change Request rather than silent absorption. Propose the Cost variance escalation threshold from
   `project-constitution.md`'s Project Defaults first and say it is the project default; the user may
   pick a different one, and you add the difference to the constitution's Amendments table (today's
   date and a one-line change; ask the user only who approves it).
6. If Full EVM mode was chosen, confirm the schedule (`schedule.md`) has enough date granularity
   to compute Planned Value later; otherwise flag it as a gap to close before the first control cycle.
7. Present the Cost Management Plan to the user for review before treating it as baseline.
8. Tell the user the next command is `/pf-plan-risk`.
