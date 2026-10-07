---
description: Establish project-specific working agreements — decision authority, cadence, escalation rules — before planning begins.
---

# /pf-setup-project-constitution

Act as the `pf-planner` agent (see `.github/agents/planner.agent.md`). Produce
`.pmo/project-constitution.md`, and tailor `.pmo/work-package-definitions.md` (step 6).

This sits above individual artifacts and below the framework-wide `.github/copilot-instructions.md`:
copilot-instructions.md governs how ProjectFabric agents behave on every project;
`project-constitution.md` governs how *this* project's people and agents make decisions. `/pf-setup-init`
pass 2 already created it with the Project Defaults and Team Working Rules copied from `.pmo/team.md`;
this command adds what is specific to the project.

## Steps

0. Read `.pmo/project-constitution.md`. Show the user its Project Defaults and Team Working Rules
   (copied from `team.md`): they already apply to this project, so do not restate them elsewhere.

1. Project Defaults. Show the table (Workflow Preset, Cost tracking mode, Control cycle cadence, Cost
   variance escalation threshold, Risk acceptance score ceiling) and ask whether this project needs a
   different value for any row. If not, change nothing. Where the user wants a different value, edit
   that row and write the Amendments row yourself (today's date; a one-line Change naming the row,
   the team's value and the reason). Leave Approved By for step 7. Never silently change a value.
2. Ask the user for this project's Project Working Rules — non-negotiable rules for this project only,
   on top of the Team Working Rules (e.g. "no scope change without sponsor sign-off"). A rule that
   every project of the team should follow belongs in `team.md`, so suggest that instead. Don't
   invent rules; if the user has none beyond the team's and the framework defaults, say so explicitly
   rather than padding the list. Ask whether any Team Working Rule does not apply to this project;
   list each with a reason under Exempted Team Working Rules, and leave it empty otherwise.
3. Decision Authority. The table is pre-filled with the default approver (the Sponsor) for each
   decision type. Show it and ask whether any approver should be a named person or a different role;
   change only what the user says. The budget and risk thresholds are the Cost variance escalation
   threshold and Risk acceptance score ceiling in Project Defaults (step 1).
4. Status Report Reviewers is pre-filled with the Sponsor. Ask whether to add or replace anyone. How
   often `/pf-control-cycle` runs is the Control cycle cadence in Project Defaults (step 1).
5. Escalation Rules is pre-filled with the framework's default rules (when a deviation becomes a Change
   Request, an above-ceiling risk acceptance, a blocked work package, anything smaller absorbed). Show
   them and ask whether to add, change or drop a rule; note the reason for a change in Amendments. If any
   rule could be checked automatically, offer to record it in `automation-rules.md` (the user chooses
   the numbers).
6. Project Completion Criteria is pre-filled with the default conditions `/pf-close-project` checks.
   Show them and ask whether to add, change or drop one; note the reason for a change in Amendments.
   Then open
   `.pmo/work-package-definitions.md` (created by `/pf-setup-init` pass 2 with the standard checks): show
   its Definition of Ready and Definition of Done tables and ask whether this project needs an extra
   check, or wants to change or drop a standard one. Add a row, with who fixes a failure, for each extra
   check; for a changed or dropped row, edit the table and note the reason in that file's Amendments.
   Otherwise leave it as is.
7. Present the Constitution to the user for review before treating it as baseline. Complete the
   Amendments table yourself (the Initial version row's date, and a row for each change you noted in
   steps 1 to 6 and in `work-package-definitions.md`) and ask the user only who approves, writing the
   name they give in Approved By; never fill it in yourself. Once approved,
   changes go through the same Change Control as other baseline documents (Ground Rule 5).
8. Tell the user the next command is `/pf-setup-charter`.
