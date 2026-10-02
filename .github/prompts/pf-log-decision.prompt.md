---
description: Record a judgment call that doesn't rise to a scope/schedule/budget baseline change (Decision Log).
---

# /pf-log-decision

Any agent may propose a decision; the `pf-project-manager` agent owns the log. Write
`.pmo/decisions/DEC-<id>.md`.

## Steps

1. Confirm this decision does **not** change scope, schedule, budget, or resource baseline — if
   it does, stop and tell the user to run `/pf-change-request` instead.
2. Assign the next sequential `DEC-<id>` (check `.pmo/decisions/` for the highest existing ID).
3. Write the decision record using `templates/decision-record.template.md`: context, options
   considered, the decision itself and why, consequences, and a Decision Owner (whoever is
   accountable for this call — not necessarily the user).
4. Set Status to "Draft" until the user confirms it; then update Status to "Signed-off".
5. If this decision supersedes an earlier one, update the earlier `DEC-<id>.md`'s Status to
   "Superseded (by DEC-<new-id>)" and its Amendments section — never delete a superseded record.
6. Tell the user the decision is logged and continue with whatever command they were already
   running.
