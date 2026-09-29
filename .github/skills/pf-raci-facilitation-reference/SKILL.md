---
name: pf-raci-facilitation-reference
description: 'RACI workshop facilitation technique, common anti-patterns, and RACI variants (RASCI, DACI). Use when the Project Manager is building raci.md during /pf-6-plan-organization and the user is unsure how to run the exercise or gets stuck on who should be Accountable.'
---

# RACI Facilitation Reference

## When to Use

- Building `raci.md` during `/pf-6-plan-organization` and the user isn't sure how to run the
  exercise, or the matrix keeps coming out wrong (multiple As, no As, everyone Consulted).

## Facilitation Steps

1. List every WBS leaf work package as a row (already done, from `wbs.md`).
2. List every Worker identity + the Project Manager + the Sponsor as columns.
3. For each row, ask **"who is Accountable?"** first, before assigning any Responsible — 
   Accountable is the one person whose neck is on the line for this work package being done
   correctly. Exactly one per row, no exceptions.
4. Then ask **"who is Responsible?"** — who actually does the work. Often the same person as
   Accountable for a small team; can differ when someone delegates but retains accountability.
5. Only then consider Consulted/Informed — and be stingy. Every C and I adds communication
   overhead; don't add someone "just in case."

## Anti-Patterns to Catch

| Anti-pattern | Why it's a problem | Fix |
|---|---|---|
| Two or more A's on one row | No one is actually accountable — diffused responsibility means no one acts when something goes wrong | Force a single choice; if truly shared, split the work package into two |
| Zero A's on a row | Same problem, inverted — work package has no owner | Assign one, even if it feels arbitrary; ambiguity is worse |
| R with no A | Responsible person has no one to escalate to or be accountable to | Every R needs an A, even if it's the same person |
| Everyone marked C | Decision paralysis — too many people need to weigh in before anything moves | Downgrade most Cs to I; reserve C for people whose input would actually change the outcome |
| A role that's Accountable for everything | Bottleneck — one person can't meaningfully oversee 20 work packages in detail | Consider whether Accountable should be distributed by work stream instead of concentrated |

## RACI Variants (use only if plain RACI doesn't fit)

| Variant | Adds | When it helps |
|---|---|---|
| **RASCI** | Support (S) — helps Responsible but isn't R themselves | Work packages where one person leads but regularly needs hands-on help, distinct from a C (who's just consulted, not doing hands-on work) |
| **DACI** | Driver / Approver / Contributor / Informed — reframes around decision-making rather than task execution | Decision-heavy work packages (e.g. "choose the vendor") rather than execution-heavy ones |

Default to plain RACI — only reach for a variant if the user explicitly says RACI doesn't capture
their situation.

## Common Mistakes to Avoid

- Don't let the RACI matrix become a task list in disguise — it maps WBS work packages (already
  decomposed) to roles, it doesn't re-decompose the work.
- A Worker identity used in `raci.md` must exist as a `bus/<worker>/` folder later — flag any
  mismatch when work packages are eventually assigned via `/pf-8-assign-task`.
