---
description: Two passes. Pass 1 creates .pmo/team.md for you to fill in; pass 2 scaffolds the rest of .pmo/ once team.md is complete.
---

# /pf-setup-init

Scaffold the project's `.pmo/` directory so every ProjectFabric agent has somewhere to read and
write state. It runs in two passes, because the team defaults (including the Workflow Preset) must
exist before anything else is created. There is no separate preset question: the Workflow Preset
comes from `team.md`.

## Which pass is this?

Decide from the state of `.pmo/`:

| State | Pass |
|---|---|
| No `.pmo/team.md` | **Pass 1** |
| `.pmo/team.md` exists, no `.pmo/project-constitution.md` | **Pass 2**, which runs only if `team.md` is filled in (see its gate); otherwise it stops and tells the user to fill it in |
| `.pmo/project-constitution.md` exists | Already initialized: list `.pmo/` and ask the user whether to leave it alone (default) or which specific files to re-scaffold. Never overwrite existing project artifacts silently. |

## Pass 1: create team.md

1. Create `.pmo/team.md` from `templates/team.template.md` and create nothing else. Prefer the
   scaffold script (see the `pf-helper-scripts` skill):
   `python .github/skills/pf-helper-scripts/scripts/pf_scaffold.py --team-only`. If it can't be run,
   create `.pmo/` and copy the template by hand.
2. Tell the user `team.md` must be filled in before pass 2 will run: the Team name, a value in every
   row of Team Defaults (write N/A where the team has no default; the Workflow Preset must be one of
   the three below), and at least one Working Rule. Amendments is optional. If the team keeps a
   shared file of team working rules, the user pastes its content in.
   - **classic-waterfall** — full PMBOK coverage, every knowledge area planned up front.
   - **agile-hybrid** — Scope/Schedule/Risk/Stakeholder/Organization/RACI backbone required; Cost, Quality,
     Procurement, and Resource-depth planning are pulled in later only when actually needed.
   - **lean** — only the minimum needed to start assigning and tracking work is required;
     everything else is offered but skipped unless asked for.
   See [docs/knowledge-areas.md](../../docs/knowledge-areas.md#workflow-presets) for the full
   Required/Optional breakdown per preset — do not re-derive it here.
3. You may help the user decide, and may write values the user states, but never invent a value
   (Ground Rule 4).
4. Stop. Tell the user to fill in `.pmo/team.md` and then run `/pf-setup-init` again in this same
   conversation (Planner).

## Pass 2: scaffold the project

1. **Gate. Do this first, before creating anything.** Read `.pmo/team.md` yourself (the Planner
   cannot run the scaffold script, so do not rely on it for this check). Ignore HTML comments. It
   is filled in only if ALL of these hold:
   - The Team Name section has a name, not `TBD` or empty.
   - Every row of the Team Defaults table (Workflow Preset, Cost tracking mode, Control cycle
     cadence, Cost variance escalation threshold, Risk acceptance score ceiling) has a value that is
     not `TBD` or empty, and the Workflow Preset is exactly classic-waterfall, agile-hybrid, or lean.
   - Working Rules has at least one numbered rule with text (a bare `1.` does not count).
2. **If any check fails, pass 2 does not run.** Create no file or folder, ask no preset question, and
   do not offer to continue anyway or to fill the values in on your own. Reply with:
   - `## Planner - Blocked` and `Artifacts: none`;
   - the exact list of what is still missing, such as "Team Defaults: Cost tracking mode is TBD";
   - an instruction to fill in `.pmo/team.md` (pointing to the allowed values in its comments), then
     run `/pf-setup-init` again in this conversation.
   You may help the user choose values and write what they tell you, but never invent one
   (Ground Rule 4); then re-run the gate.
3. The project's Workflow Preset is the one in `team.md`. Do not ask the user for one: it is copied
   into the constitution's Project Defaults with the other defaults (step 5).
4. Create the structure below. Prefer the scaffold script if you can run it (it repeats the same
   check and also refuses on an incomplete `team.md`):
   `python .github/skills/pf-helper-scripts/scripts/pf_scaffold.py`, adding `--dry-run` first if
   `.pmo/` already holds other files. It never overwrites existing files. Otherwise copy
   each file from `templates/` by hand (strip the `.template` suffix), leaving placeholder fields
   intact for the owning agent to fill in later:
   ```
   .pmo/
     team.md            (filled in during pass 1; left as is)
     project-constitution.md
     work-package-definitions.md
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
5. Fill `project-constitution.md` from `team.md` (the script does this; otherwise by hand): copy the
   five Team Defaults values into its Project Defaults table, and copy the Working Rules list into
   Team Working Rules. Leave Project Working Rules and the rest empty. From now on agents read these
   values in the constitution, not in `team.md`; a project that needs a different value changes it
   later in `/pf-setup-project-constitution`.
6. Confirm the structure was created, tell the user which Workflow Preset applies (from `team.md`),
   and tell the user the next command is
   `/pf-setup-project-constitution` (or `/pf-setup-charter` directly if the user wants to skip the
   constitution step for a lightweight project).
