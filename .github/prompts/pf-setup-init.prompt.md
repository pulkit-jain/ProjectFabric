---
description: Scaffold the .pmo/ project management state directory from templates.
---

# /pf-setup-init

Scaffold the project's `.pmo/` directory so every ProjectFabric agent has somewhere to read and
write state.

## Steps

1. Check whether `.pmo/` already exists. If it does, list its contents and ask the user whether
   to leave it alone (default), or which specific files to re-scaffold — never overwrite existing
   project artifacts silently.
2. Ask the user whether their team keeps a shared team standards file (`team.md`). If yes, copy it
   into `.pmo/team.md` as-is; if no, scaffold a blank one from `templates/team.template.md` (safe
   to leave with `TBD` values — nothing depends on it being filled in). Read its Team Defaults
   for the next step.
3. Ask the user which Workflow Preset fits this project, briefly describing each — and if
   `team.md` sets a default Workflow Preset, propose that first and say it's the team default:
   - **classic-waterfall** (default) — full PMBOK coverage, every knowledge area planned up front.
   - **agile-hybrid** — Scope/Schedule/Risk/Stakeholder/Organization/RACI backbone required; Cost, Quality,
     Procurement, and Resource-depth planning are pulled in later only when actually needed.
   - **lean** — only the minimum needed to start assigning and tracking work is required;
     everything else is offered but skipped unless asked for.
   See [docs/knowledge-areas.md](../../docs/knowledge-areas.md#workflow-presets) for the full
   Required/Optional breakdown per preset — do not re-derive it here.
4. Create the structure below. Prefer the scaffold script (see the `pf-helper-scripts` skill):
   `python .github/skills/pf-helper-scripts/scripts/pf_scaffold.py --preset <choice from step 3>`,
   adding `--team <path>` if the user supplied a shared team file and `--dry-run` first if `.pmo/`
   already exists. It never overwrites existing files. If it can't be run, copy each file from
   `templates/` by hand (strip the `.template` suffix), leaving placeholder fields intact for the
   owning agent to fill in later:
   ```
   .pmo/
     team.md            (copied from the team's shared file, or blank from template)
     constitution.md
     charter.md
     scope-statement.md
     wbs.md
     schedule.md
     cost-management-plan.md
     cost-performance.md
     risk-register.md
     stakeholder-register.md
     raci.md
     communications-plan.md
     tracker.md
     automation-rules.md    (example rules, all disabled — checked at each /pf-control-cycle)
     sprint-backlog.md      (Agile ceremony layer — populated only if Scrum ceremonies are run)
     standup-log.md         (Agile ceremony layer)
     retro-log.md           (Agile ceremony layer)
     bus/               (empty — populated per team member by /pf-assign-task)
     memory/
       work-packages/   (empty — populated by Team Members)
     reports/           (empty — populated by /pf-control-cycle)
     changes/           (empty — populated by /pf-change-request)
     decisions/         (empty — populated by /pf-log-decision)
     archives/          (empty — populated by /pf-session-archive-stage)
     closing/           (empty — populated by /pf-close-project)
   ```
5. Make sure the freshly-copied `constitution.md`'s Workflow Preset field holds the user's choice
   from step 3 (the script does this when given `--preset`; otherwise fill it in by hand). Use
   `classic-waterfall` if the user has no preference yet — this is a scaffolding default, not a
   baseline approval, and can still be revisited in `/pf-setup-constitution`.
6. Confirm the structure was created and tell the user the next command is
   `/pf-setup-constitution` (or `/pf-setup-charter` directly if the user wants to skip the
   constitution step for a lightweight project).
