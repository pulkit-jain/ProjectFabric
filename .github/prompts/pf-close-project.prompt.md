---
description: Run project closing — verify acceptance, capture lessons learned, and produce the final report.
---

# /pf-close-project

Act as the Planner and Project Manager agents together. Produce `.pmo/closing/lessons-learned.md`
(from `templates/lessons-learned.template.md`) and `.pmo/closing/final-report.md`.

## Steps

1. Verify every work package in `tracker.md` is Status = "Done" with acceptance criteria met. If
   any remain open, confirm with the user whether to close them out, descope via
   `/pf-change-request`, or hold closing until they finish.
2. If `.pmo/archives/` exists, read each `stage-summary.md` (not the archived files) as input to
   the lessons-learned session and final report.
3. Run a lessons-learned session with the user across What Went Well / What Didn't / Recommendations,
   tagged by phase (Initiating/Planning/Executing/Monitoring/Closing) and by knowledge area
   (Scope, Schedule, Risk, Stakeholder, etc.). Write to `closing/lessons-learned.md`.
4. Produce `closing/final-report.md`: original objectives vs. delivered outcomes, final scope/
   schedule variance summary, risks that materialized vs. didn't, stakeholder engagement outcome,
   and a pointer to all `.pmo/` artifacts as the permanent project record.
5. Tell the user the project is formally closed and `.pmo/` should be archived per their
   organization's retention practice.
