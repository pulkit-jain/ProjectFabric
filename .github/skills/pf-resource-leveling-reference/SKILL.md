---
name: pf-resource-leveling-reference
description: 'Resource leveling and schedule compression techniques (leveling vs. smoothing, fast-tracking, crashing). Use when the Resource Manager or Project Manager finds a resource conflict or schedule pressure during /pf-plan-resources, /pf-control-cycle, or a Change Request, and needs options beyond "just ask the user".'
---

# Resource Leveling & Schedule Compression Reference

Sources: REF-M01 ([docs/Reference.md](../../../docs/Reference.md)).

## When to Use

- `resource-management-plan.md`'s Capacity Plan shows a genuine over-allocation (demand > 100%
  supply in some period) that can't be waved away.
- A Change Request needs to propose options for resolving a schedule/resource conflict.

## Resource Leveling vs. Resource Smoothing

| Technique | What it does | Schedule impact |
|---|---|---|
| **Resource Leveling** | Resequence work so no resource is ever over-allocated | May extend the schedule / push out the critical path |
| **Resource Smoothing** | Adjust only within existing float (slack) — never touches the critical path | Schedule end date is protected, but only works if enough float exists |

Use Smoothing first (it's free — no schedule impact) if there's enough float; fall back to
Leveling (which does cost schedule) only if Smoothing isn't enough.

## Options When a Conflict Is Found (in rough order of preference, cheapest first)

1. **Resequence within existing float** (Smoothing) — no cost, no schedule impact, only works if
   slack exists.
2. **Resequence past available float** (Leveling) — small schedule slip, no added cost.
3. **Add a resource** (existing team member part-time, or a new hire/contractor) — no schedule
   slip, but adds cost and needs lead time for a new hire/contractor.
4. **Fast-track** — run normally-sequential activities in parallel, accepting rework risk if an
   upstream activity changes after a downstream one has already started based on it.
5. **Crash** — add resources specifically to shorten a critical-path activity's duration; only
   effective on the critical path (crashing a non-critical activity doesn't change the finish
   date) and usually has cost/quality trade-offs (see the law of diminishing returns — crashing
   too hard produces coordination overhead that eats the time saved).

## Common Mistakes to Avoid

- Don't crash a work package that isn't on the critical path — see the
  `pf-critical-path-reference` skill to confirm which work packages are actually critical first.
- Fast-tracking increases rework risk — flag it to the Risk Manager as a new or elevated risk,
  don't just apply it silently.
- Leveling that pushes the schedule needs the same Change Request/baseline-update treatment as
  any other schedule change (Ground Rule 5) — it's not a free action just because it avoids
  adding cost.
