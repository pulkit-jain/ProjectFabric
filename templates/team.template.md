# Team Working Agreement

<!-- Team-level defaults shared across every ProjectFabric project this team runs. Sits between the
framework-wide .github/copilot-instructions.md (all teams) and each project's project-constitution.md
(one project). /pf-setup-init creates this file in .pmo/ (pass 1); fill it in before running
/pf-setup-init again (pass 2), which refuses to continue while it is incomplete. If your team keeps
a shared copy, paste its content in. Once filled in, treat as baseline — changes go through the same
Change Control as project-constitution.md. Pass 2 copies the Team Defaults and Working Rules into the
project's project-constitution.md (Project Defaults and Team Working Rules); from then on agents read
them there, and editing this file does not change them. A project that needs a different value changes
it in its constitution. Neither this file nor a constitution may contradict the framework-wide Ground
Rules. -->

## Team Name

<!-- The name of the team these defaults and standards belong to, e.g. "Brand and Packaging Team".
Required before /pf-setup-init pass 2 will run. -->

TBD

## Team Defaults

<!-- Starting values proposed at /pf-setup-init and in the relevant planning commands. The user can
still pick differently for a given project, but should be told this is a deviation from the team default.
Every row must be filled (not TBD) before /pf-setup-init pass 2 will run; write N/A if the team has
no default for a row (Workflow Preset must be one of the four presets).

Allowed values:
- Workflow Preset: classic-waterfall / agile-hybrid / lean / pi-cadence
- Cost tracking mode: Lightweight / Full EVM
- Control cycle cadence: weekly / bi-weekly / monthly / per sprint / per milestone (how often
  /pf-control-cycle is intended to run)
- Cost variance escalation threshold: a percentage, e.g. 10% (overrun beyond which a Change Request
  is raised)
- Risk acceptance score ceiling: 1-25 (Probability x Impact); accepting a risk above it needs sign-off -->

| Setting | Team Default |
|---|---|
| Workflow Preset | TBD |
| Cost tracking mode | TBD |
| Control cycle cadence | TBD |
| Cost variance escalation threshold | TBD |
| Risk acceptance score ceiling | TBD |

## Working Rules

<!-- Working rules every project of THIS TEAM follows, e.g. "all vendor contracts need Legal
review", "status reports go to the PMO lead". They apply to all of the team's projects; a rule for
one project only goes in that project's project-constitution.md under Working Rules instead.
Only real rules; don't pad. At least one rule is required before /pf-setup-init pass 2 will run. -->

1.

## Amendments

<!-- One row per change to this file after it is baselined. The agent writes Date (YYYY-MM-DD) and
Change (one line, with the CR ID if there is one); the user names who approved it (Approved By), and
the agent never fills that in itself. Keep the Initial version row and add new rows below it; never
edit or delete earlier rows. -->

| Date | Change | Approved By |
|---|---|---|
| | Initial version | |
