---
name: pf-critical-path-reference
description: 'Critical Path Method (CPM) forward/backward pass and float calculation for schedule.md. Use when the Planner is sequencing work packages during /pf-3-plan-schedule and needs to identify the actual critical path and float, not just an intuitive guess.'
---

# Critical Path Method (CPM) Reference

## When to Use

- Building `schedule.md`'s Critical Path Notes section during `/pf-3-plan-schedule`.
- The dependency graph has more than a handful of work packages, or has any parallel branches —
  past that size, "eyeballing" the critical path is unreliable.

Skip this for a simple linear chain (A→B→C→D) — the critical path is obviously the whole chain.

## Inputs

Each work package needs: a **Duration** (relative units are fine — days, weeks) and its
**Predecessor(s)** from `schedule.md`'s Work Package Sequencing table.

## Method

1. **Forward pass** (compute Early Start/Early Finish, left to right through the dependency
   graph):
   - ES (Early Start) = the latest EF among all predecessors (0 if no predecessor).
   - EF (Early Finish) = ES + Duration.
2. **Backward pass** (compute Late Start/Late Finish, right to left, starting from the project's
   overall EF):
   - LF (Late Finish) = the earliest LS among all successors (= project EF for end nodes).
   - LS (Late Start) = LF − Duration.
3. **Float** = LS − ES (equivalently LF − EF). A work package with **Float = 0 is on the critical
   path** — any delay to it delays the whole project. Float > 0 means it has slack.

## Worked Example

| WP | Duration | Predecessor(s) | ES | EF | LS | LF | Float | Critical? |
|---|---|---|---|---|---|---|---|---|
| A | 2 | — | 0 | 2 | 0 | 2 | 0 | Yes |
| B | 3 | A | 2 | 5 | 2 | 5 | 0 | Yes |
| C | 1 | A | 2 | 3 | 4 | 5 | 2 | No |
| D | 2 | B, C | 5 | 7 | 5 | 7 | 0 | Yes |

Critical path: **A → B → D** (total duration 7). C has 2 units of float — it could slip by up to
2 without delaying the project.

## Reporting in `schedule.md`

State the critical path in plain language ("A → B → D is critical; C has 2 weeks of slack") —
don't dump the full ES/EF/LS/LF table into the artifact unless the user asks for it; that table
is working material for you to derive the plain-language statement, not the deliverable itself.

## Common Mistakes to Avoid

- Don't compute float per-task in isolation — it depends on the whole downstream chain via the
  backward pass, not just the task's own duration.
- A dependency graph can have **more than one** critical path (multiple chains tied for the
  longest duration) — check for ties, don't stop at the first Float=0 chain found.
- If the user hasn't provided durations (only relative sequencing), you cannot compute numeric
  float — say so explicitly rather than inventing durations to force a calculation.
