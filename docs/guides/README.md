# ProjectFabric Guides

Start with the guide that matches where you are.

| I want to... | Read |
|---|---|
| Try it on a small project, step by step | [Getting started](getting-started.md) |
| Understand the ideas: the three conversations, presets, baselines | [How a project runs](how-a-project-runs.md) |
| See what a real project looks like | [Example project](../example/README.md) |
| Know what to do in a specific situation | [Scenarios](scenarios.md) |
| Look up a command: when to run it, what to give it, what comes back | [Command reference](command-reference.md) |
| Know what a `.pmo/` file is and who owns it | [Artifact reference](artifact-reference.md) |

## By reader

**New to project management.** [How a project runs](how-a-project-runs.md) (it has a glossary), then
[Getting started](getting-started.md), then the [example project](../example/README.md).

**An experienced project manager.** The "Notes for experienced project managers" at the end of
[How a project runs](how-a-project-runs.md) map PMBOK terms to ProjectFabric. Then the fast path at the
top of [Getting started](getting-started.md), and the [command reference](command-reference.md).

**Setting this up for a team.** [Knowledge areas and presets](../knowledge-areas.md), the
[architecture](../architecture.md), and the plugin rules in [plugins/README.md](../../plugins/README.md).

## Keeping the command reference current

The tables in the command reference are generated. After changing a prompt or
[command-notes.md](command-notes.md), run this from the repository root:

```
python tools/gen_command_reference.py
```

`python tools/gen_command_reference.py --check` reports whether the file is out of date, and fails
when a prompt has no entry in `command-notes.md`.
