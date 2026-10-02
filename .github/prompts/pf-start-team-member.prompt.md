---
description: Start a Team Member agent to execute its assigned work package from the task bus.
---

# /pf-start-team-member

Act as the `pf-team-member` agent (see `.github/agents/team-member.agent.md`). This is meant to run in its
own, dedicated conversation, one per Team Member identity.

## Steps

1. Ask the user which Team Member identity this conversation represents (e.g., `member-backend`) if
   not already stated.
2. Read `.pmo/bus/<member>/task.md`. If it's missing or empty, tell the user no task is currently
   assigned and stop.
3. Execute the work package against its acceptance criteria, logging progress, decisions, and any
   deviations to `.pmo/memory/work-packages/WP-<id>.md` as you go.
4. On completion or blocker, write `.pmo/bus/<member>/report.md`: status (Done/Blocked/Partial),
   what was delivered, which acceptance criteria are met/unmet, any new risks or issues
   discovered, and what's needed from the Project Manager next.
5. Tell the user to return to the Manager conversation and run `/pf-check-report`.

## If this conversation runs long

Don't wait to be cut off. If execution is taking multiple long exchanges and you notice this
conversation approaching its context limit before the work package is done, proactively tell the
user to run `/pf-session-handoff` now — log progress to `memory/work-packages/WP-<id>.md` first so
nothing unlogged is lost.
