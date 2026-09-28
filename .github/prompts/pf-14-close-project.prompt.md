---
description: Run project closing — verify acceptance, capture lessons learned, and produce the final report.
---

# /pf-14-close-project

Act as the Planner and Project Manager agents together. Produce `.pmo/closing/lessons-learned.md`
and `.pmo/closing/final-report.md`.

## Steps

1. Verify every work package in `tracker.md` is Status = "Done" with acceptance criteria met. If
   any remain open, confirm with the user whether to close them out, descope via
   `/pf-12-change-request`, or hold closing until they finish.
2. Run a lessons-learned session with the user across What Went Well / What Didn't / Recommendations,
   tagged by phase (Initiating/Planning/Executing/Monitoring/Closing) and by knowledge area
   (Scope, Schedule, Risk, Stakeholder, etc.). Write to `closing/lessons-learned.md`.
3. Produce `closing/final-report.md`: original objectives vs. delivered outcomes, final scope/
   schedule variance summary, risks that materialized vs. didn't, stakeholder engagement outcome,
   and a pointer to all `.pmo/` artifacts as the permanent project record.
4. Tell the user the project is formally closed and `.pmo/` should be archived per their
   organization's retention practice.
