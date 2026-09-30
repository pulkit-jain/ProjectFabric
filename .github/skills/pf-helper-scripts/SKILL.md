---
name: pf-helper-scripts
description: 'Deterministic helper scripts for ProjectFabric: EVM math, .pmo/ consistency validation (WBS, RACI one-Accountable, risk scores, tracker, bus drift), automation-rule evaluation, and .pmo/ scaffolding. Use when computing Full EVM figures for cost-performance.md, running a control cycle, checking .pmo/ for drift or broken IDs, evaluating automation-rules.md, or running /pf-0-init.'
---

# ProjectFabric Helper Scripts

Small Python scripts for tasks that have exactly one right answer, so an agent runs them instead
of re-deriving the result by reading tables or doing arithmetic. They compute or check; they never
decide. Run them only when the user's workflow calls for it, never in a loop or unattended.

**Requirements:** Python 3.9 or newer, standard library only (nothing to install). Run from the
project root. If Python isn't available or the terminal is refused, do the task by hand as the
owning agent's instructions describe -- the scripts are an accelerator, not a dependency.

All four live in `.github/skills/pf-helper-scripts/scripts/`.

## pf_evm.py -- Earned Value figures (Cost Manager)

Use for **Full EVM** mode only. Computes EV, CV, SV, CPI, SPI, EAC, ETC, VAC per work package plus
the Project Rollup, and prints both tables in the exact shape `cost-performance.md` uses.

```
python .github/skills/pf-helper-scripts/scripts/pf_evm.py \
  --wp "1.1|Script approval|550|550|100|500" --wp "1.2|Video production|8250|8250|100|7500"
```

Each `--wp` is `id|name|BAC|PV|percent complete|AC` (name optional). Inputs come from
`cost-management-plan.md` (BAC), `schedule.md` (PV), `tracker.md` (% Complete), and reported actuals
(AC). Optional: `--currency ''` for no symbol, `--decimals 2` for cents.

- Read-only: paste the output into `cost-performance.md` yourself.
- Status is left `TBD`. Setting Green/Yellow/Red against the thresholds is the Cost Manager's call.
- `n/a` means a divisor was zero (no actual cost yet, no planned value, or no earned value).
- It does not round CPI before computing EAC, so EAC can differ slightly from a hand calculation
  that used a rounded CPI. The script's figure is the correct one.

## pf_validate.py -- .pmo/ consistency check (Project Manager)

Run at the start of each `/pf-11-control-cycle`, and whenever IDs or tables may have drifted.

```
python .github/skills/pf-helper-scripts/scripts/pf_validate.py --pmo .pmo
```

| Area | What it checks |
|---|---|
| WBS | Hierarchy leaves match the WBS Dictionary; IDs unique; every row has acceptance criteria |
| RACI | Exactly one Accountable per work package; IDs match the WBS Dictionary |
| Risks | IDs unique; Score = Probability x Impact; Probability/Impact within 1-5; sorted by Score descending |
| Tracker | IDs match the WBS; valid status; Done means 100%; linked `R-` and `CR-` IDs exist |
| Bus | Each `bus/<worker>/task.md` points at a tracker row that has been started, with a matching Owner |
| Sprint | Every `sprint-backlog.md` WBS ID exists in the WBS Dictionary |

Output is one line per finding: `FAIL` (a rule is broken), `WARN` (suspicious, may be intentional),
`PASS`, or `SKIP` (file missing or not yet filled in). Exit code 1 means at least one FAIL. Rows
whose name/description column is blank are unfilled template placeholders and are skipped.

- It only reads. Report FAIL/WARN findings to the user and to the artifact's owning agent; don't
  silently edit another agent's file to make the check pass (Ground Rule 2).
- A WARN for a register that isn't sorted is a real defect to fix, not noise.

## pf_rules.py -- automation rules (Project Manager)

Evaluates the user's rules in `.pmo/automation-rules.md` against the current `.pmo/` state. Run it
in `/pf-11-control-cycle` *after* the cycle has refreshed `cost-performance.md` and the other
logs (step 8) — run earlier, the cost rules read last cycle's figures.

```
python .github/skills/pf-helper-scripts/scripts/pf_rules.py --pmo .pmo
python .github/skills/pf-helper-scripts/scripts/pf_rules.py --list-metrics
```

Each rule is a table row: `Condition` (`<metric> <operator> <number>`, e.g.
`cost_overrun_pct_max > 15`), a `Flag Message`, a `Suggest`ed command, and `Enabled`. Metrics:
`blocked_wp_count`, `done_pct`, `open_risk_count`, `open_risk_max_score`, `cost_overrun_pct_max`
(Lightweight mode), `cpi_min` / `spi_min` (Full EVM mode), `draft_decision_count`.

Output per enabled rule: `TRIGGERED`, `ok`, `n/a` (metric can't be computed from the current
files), or `ERROR` (malformed rule; exit code 1). Disabled rules are skipped.

- A triggered rule only **flags**. Put it in the Status Report and show the user the suggested
  command; never run it, never edit a baseline because a rule fired (Ground Rules 5 and 6).
- The user writes the rules and chooses the numbers. The template's rows are examples, all
  disabled; don't enable one whose threshold nobody has set.
- Rules complement, not replace, judgment: a rule that doesn't fire is not proof nothing is wrong.

## pf_scaffold.py -- create .pmo/ (`/pf-0-init`)

Creates the standard artifact files from `templates/` (dropping `.template`) and the working
folders (`bus`, `memory/work-packages`, `reports`, `changes`, `decisions`, `archives`, `closing`).

```
python .github/skills/pf-helper-scripts/scripts/pf_scaffold.py --preset agile-hybrid [--team path/to/team.md] [--dry-run]
```

- Never overwrites: existing files and folders are kept and listed. Use `--dry-run` first when
  `.pmo/` already exists.
- `--preset` (classic-waterfall / agile-hybrid / lean) fills the constitution's `**Preset:**` line.
- `--team` copies the team's shared `team.md` in instead of the blank template.
- Its file list mirrors the one in `pf-0-init.prompt.md`; change both together.

## Common Mistakes to Avoid

- Running a script and treating its output as a decision. `PASS` means the tables are consistent,
  not that the plan is good; a `TBD` Status still needs a human judgment.
- Hand-computing EVM in Full EVM mode when the script is available.
- Editing another agent's artifact to clear a validator finding instead of routing it to the owner.
