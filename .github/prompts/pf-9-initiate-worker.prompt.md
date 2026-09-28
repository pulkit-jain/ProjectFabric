---
description: Start a Worker agent to execute its assigned work package from the task bus.
---

# /pf-9-initiate-worker

Act as the `pf-worker` agent (see `.github/agents/worker.agent.md`). This is meant to run in its
own, dedicated conversation, one per Worker identity.

## Steps

1. Ask the user which Worker identity this conversation represents (e.g., `worker-backend`) if
   not already stated.
2. Read `.pmo/bus/<worker>/task.md`. If it's missing or empty, tell the user no task is currently
   assigned and stop.
3. Execute the work package against its acceptance criteria, logging progress, decisions, and any
   deviations to `.pmo/memory/work-packages/WP-<id>.md` as you go.
4. On completion or blocker, write `.pmo/bus/<worker>/report.md`: status (Done/Blocked/Partial),
   what was delivered, which acceptance criteria are met/unmet, any new risks or issues
   discovered, and what's needed from the Project Manager next.
5. Tell the user to return to the Manager conversation and run `/pf-10-check-report`.

## If this conversation runs long

Don't wait to be cut off. If execution is taking multiple long exchanges and you notice this
conversation approaching its context limit before the work package is done, proactively tell the
user to run `/pf-13-handoff` now — log progress to `memory/work-packages/WP-<id>.md` first so
nothing unlogged is lost.
