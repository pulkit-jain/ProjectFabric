---
description: Run risk identification, qualitative analysis, and response planning; produce the Risk Register.
---

# /pf-plan-risk

Act as the `pf-risk-manager` agent (see `.github/agents/risk-manager.agent.md`). Read
`.pmo/charter.md` and `.pmo/wbs.md`; produce `.pmo/risk-register.md`.

## Steps

1. Run a risk identification pass against each major WBS branch and against each risk category
   (Technical, External, Organizational, Project Management). Ask the user for input rather than
   inventing risks wholesale — you may propose candidates but must have the user confirm them.
2. For each identified risk, capture: description (as a specific conditional statement), category,
   related WBS element(s).
3. Score Probability (1–5) and Impact (1–5) with the user — never fabricate a score. Compute
   Score = Probability × Impact and sort the register by Score, descending.
4. For each risk, agree a response strategy (Avoid/Transfer/Mitigate/Accept for threats;
   Exploit/Share/Enhance/Accept for opportunities), an owner, and — where applicable — a trigger
   condition the Project Manager should watch for. Read `.pmo/team.md` (and the Risk acceptance
   row of `constitution.md`'s Decision Authority) for a Risk acceptance score ceiling: if a risk
   with Score above the ceiling is given the Accept strategy, flag it and name the approver
   before it is recorded. The ceiling is a trigger for approval, not a ban.
5. Present the Risk Register to the user for review.
6. Tell the user the next command is `/pf-plan-quality`.
