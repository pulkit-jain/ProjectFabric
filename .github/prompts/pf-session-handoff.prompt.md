---
description: Produce a handoff prompt to transfer working context to a fresh Manager or Team Member instance.
---

# /pf-session-handoff

Use this when the current Manager or Team Member conversation is approaching its context limit.

## Steps

1. Determine which role is handing off (Manager or Team Member) and, for a Team Member, which Team Member
   identity.
2. Summarize the working knowledge that isn't already captured in `.pmo/` files: recent
   conversational context, unlogged decisions, anything the user said that hasn't been written
   down yet.
3. Write that summary into the relevant durable file:
   - Manager: append to a `## Handoff Notes` section at the bottom of `tracker.md`.
   - Team Member: append to `memory/work-packages/WP-<id>.md`.
4. Produce a short handoff prompt for the user to paste into a brand-new conversation, telling the
   fresh instance to act as the same agent (`/pf-start-manager` or `/pf-start-team-member`)
   and to read the file(s) above before doing anything else.
5. Tell the user to start the new conversation and paste the handoff prompt.
