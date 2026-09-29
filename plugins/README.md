# ProjectFabric Plugins

Plugins add agents, prompts, or templates to ProjectFabric **additively** — they never edit files
under `.github/agents/`, `.github/prompts/`, or `templates/` in core. Disabling a plugin means
deleting its folder; core is byte-identical to what it was before the plugin was installed.

## Structure

```
plugins/<plugin-name>/
  .pf-plugin/
    plugin.json          # manifest (see below)
  agents/                # optional: *.agent.md files, copied into .github/agents/ on install
  prompts/                # optional: *.prompt.md files, copied into .github/prompts/ on install
  templates/              # optional: *.template.md files, copied into templates/ on install
```

## Manifest (`plugin.json`)

```json
{
  "name": "scrum-team",
  "version": "0.1.0",
  "description": "Agile/Scrum ceremony track alongside the PMBOK waterfall track",
  "author": "your-name",
  "contributes": {
    "agents": ["scrum-master.agent.md"],
    "prompts": ["pf-scrum-standup.prompt.md", "pf-scrum-retro.prompt.md"],
    "templates": ["sprint-backlog.template.md"]
  }
}
```

## Install / Uninstall

There is no installer script yet (see `docs/test-plan.md`/`ROADMAP.md` for the Deterministic
helper scripts item that could add one later). For now:

1. **Install**: copy each file listed under `contributes` from `plugins/<name>/<kind>/` into the
   matching core directory (`.github/agents/`, `.github/prompts/`, or `templates/`).
2. **Uninstall**: delete the copied files by name; core reverts to exactly what it was before.

## Rules

- A plugin must never modify a core file — only add new ones.
- A plugin's contributed `/pf-N` prompts should use a **non-numeric, prefixed command name**
  (e.g. `/pf-scrum-standup`, not a `/pf-N` letter-suffix slot) so they never collide with core's
  numbering scheme (see `ROADMAP.md`'s Governance section on letter-suffix commands).
- A plugin's contributed agents must declare their own `tools:` allow-list in frontmatter (see
  `.github/agents/*.agent.md` for the pattern) — don't default to unrestricted tool access.
- Document what knowledge area or workflow the plugin covers in its `plugin.json` `description`,
  so `templates/catalog.json` (once built) can list it for discovery.
