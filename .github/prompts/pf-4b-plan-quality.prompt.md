---
description: Define quality standards, metrics, QA/QC approach, and the QA gate before "Done" — produce the Quality Management Plan.
---

# /pf-4b-plan-quality

Act as the `pf-quality-manager` agent (see `.github/agents/quality-manager.agent.md`). Read
`.pmo/wbs.md` and `.pmo/risk-register.md`; produce `.pmo/quality-management-plan.md`.

## Steps

1. Require an approved `wbs.md` — if missing, point the user to `/pf-2-plan-scope-wbs`.
2. Ask the user for the quality standards/policy relevant to this project's deliverables. Don't
   invent generic ones — if there are none beyond the WBS Dictionary's acceptance criteria, say
   so explicitly.
3. For each deliverable type, agree a measurable quality metric with a target and measurement
   method.
4. Define the Quality Assurance approach (process-level: audits, peer review cadence) separately
   from the Quality Control approach (product-level: inspection/testing method per deliverable
   type) — keep the two distinct.
5. Define QA Gate Criteria that supplement (not replace) each WBS leaf's acceptance criteria —
   this is the checklist a work package must pass before it can be marked "Done".
6. Present the Quality Management Plan to the user for review before treating it as baseline.
7. Tell the user the next command is `/pf-4c-plan-procurement`.
