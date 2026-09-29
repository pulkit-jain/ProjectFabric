---
name: pf-risk-identification-reference
description: 'Risk identification techniques and Probability/Impact scale anchor definitions for risk-register.md. Use when the Risk Manager is running risk elicitation during /pf-4-plan-risk and the user needs more than "ask by category", or when scoring a risk and the 1-5 scale meaning needs to be concrete rather than arbitrary.'
---

# Risk Identification & Scoring Reference

## When to Use

- The user is struggling to name risks beyond the obvious ones during `/pf-4-plan-risk`.
- Scoring Probability or Impact and the user asks "what does a 3 vs. a 4 actually mean here?"

## Identification Techniques (use whichever fits; don't run all of them every time)

| Technique | How it works | Best for |
|---|---|---|
| Category brainstorming | Walk each category (Technical, External, Organizational, PM) and ask "what could go wrong here?" | Default — already the agent's baseline approach |
| Checklist analysis | Compare against a checklist of risks from similar past projects | Repeatable project types (the same team has done this before) |
| Assumption analysis | Take every assumption in `charter.md`; ask "what if this assumption is wrong?" | Projects with many stated assumptions |
| SWOT | Weaknesses/Threats map to risks directly; Strengths/Opportunities can become positive risks | Early-stage projects with an unclear risk picture |
| Pre-mortem | Ask "imagine the project failed — what happened?" and work backward | Getting a team unstuck when brainstorming has gone quiet |

## Probability Scale Anchors (1–5)

| Score | Label | Concrete anchor |
|---|---|---|
| 1 | Rare | Would be surprising if this happened at all |
| 2 | Unlikely | Could happen, but no specific reason to expect it |
| 3 | Possible | Roughly even odds; has happened on comparable projects before |
| 4 | Likely | More likely than not; an early warning sign may already be present |
| 5 | Near-certain | Already happening or all but guaranteed given current conditions |

## Impact Scale Anchors (1–5)

| Score | Label | Concrete anchor |
|---|---|---|
| 1 | Negligible | Absorbed without anyone outside the team noticing |
| 2 | Minor | Small schedule/cost/quality impact, handled within existing reserve |
| 3 | Moderate | Consumes a meaningful chunk of contingency reserve or schedule slack |
| 4 | Major | Consumes the reserve/slack entirely; likely needs a Change Request |
| 5 | Severe | Threatens a Charter objective or the project's viability |

Anchors are starting points, not rigid rules — always confirm with the user rather than applying
them mechanically; a project's own risk appetite (see `constitution.md`) can shift what counts as
"major" for that specific project.

## Risk Statement Quality Check

A good risk statement is: **"If [condition], then [event] impacting [Scope/Schedule/Cost/Quality]
by [magnitude]."** If you can't fill in all four blanks, it's not ready to score yet — go back to
identification, not straight to scoring.
