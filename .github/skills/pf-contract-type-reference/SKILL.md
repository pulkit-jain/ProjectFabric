---
name: pf-contract-type-reference
description: 'Contract type selection guide (Fixed-Price, Time & Materials, Cost-Reimbursable) with risk allocation trade-offs. Use when the Procurement Manager is choosing a contract type during /pf-4c-plan-procurement and the user is unsure which type fits their situation.'
---

# Contract Type Selection Reference

## When to Use

- A make-or-buy analysis concludes "Buy" and the user needs to pick a contract type.
- The user asks "who bears the risk if this costs more than expected?"

## The Three Core Types

| Contract Type | How payment works | Who bears cost-overrun risk | Best fit |
|---|---|---|---|
| **Fixed-Price** | One agreed price for the full defined scope | Vendor (they eat any overrun) | Scope and requirements are well-understood and unlikely to change |
| **Time & Materials (T&M)** | Pay per hour/unit of effort, no cap (or a not-to-exceed cap) | Buyer (you pay for however long it actually takes) | Scope is fuzzy, exploratory, or likely to change during the engagement |
| **Cost-Reimbursable** | Vendor is reimbursed actual costs plus a fee | Buyer, with the fee structure shaping vendor incentive | Long-term, high-uncertainty work where a fixed price would force the vendor to pad heavily |

## Fee Structure Variants (mostly relevant to Cost-Reimbursable)

| Variant | Vendor incentive |
|---|---|
| Cost Plus Fixed Fee (CPFF) | Fee is fixed regardless of final cost — vendor has no incentive to control cost, but also no reason to inflate it |
| Cost Plus Incentive Fee (CPIF) | Fee scales with hitting a cost/schedule target — aligns vendor incentive with buyer's |
| Cost Plus Award Fee (CPAF) | Fee is subjective, based on buyer satisfaction — most buyer-favorable, least predictable for vendor |

## Decision Guide

1. Is the deliverable spec (including QA gate criteria) fully knowable up front? → **Fixed-Price**.
2. Is the deliverable spec expected to change, or is this exploratory/R&D work? → **T&M**, ideally
   with a not-to-exceed cap so cost exposure has a ceiling.
3. Is this a long engagement where a fixed price would force the vendor into excessive padding,
   but you still want *some* cost control incentive? → **Cost-Reimbursable** (CPIF specifically).

## Common Mistakes to Avoid

- Don't default to Fixed-Price just because it feels "safer" — if the scope is genuinely
  uncertain, a fixed-price vendor will pad the quote heavily (you pay for the uncertainty anyway,
  just hidden inside the price) or under-deliver against ambiguous scope.
- T&M without a not-to-exceed cap has unbounded cost exposure — always ask the user whether they
  want a cap, don't assume.
- The contract type doesn't remove the need for QA gate criteria — even a Fixed-Price vendor's
  output still goes through the same gate as in-house work (see the Quality Manager's QA gate).
