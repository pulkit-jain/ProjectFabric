---
name: pf-quality-audit-reference
description: 'Generic quality assurance (process) and quality control (product) checklists, plus a catalog of common quality metrics. Use when the Quality Manager is building quality-management-plan.md during /pf-4b-plan-quality and the user does not already know what metrics or checklist items fit their deliverable type.'
---

# Quality Audit & Metrics Reference

Sources: REF-M01 ([docs/Reference.md](../../../docs/Reference.md)).

## When to Use

- The user says "I don't know what quality metrics make sense for this" during
  `/pf-4b-plan-quality`.
- Building the QA (process) checklist vs. the QC (product) checklist and the distinction isn't
  landing yet.

## Quality Assurance Checklist (process-level — is the *process* being followed?)

- Is there a defined review/approval step before a deliverable is considered complete?
- Is there a second reviewer, distinct from the person who produced the work?
- Are standards/policies documented somewhere the team can actually reference (not just tribal
  knowledge)?
- Is there a cadence for auditing the process itself (not just individual deliverables)?

## Quality Control Checklist (product-level — is *this specific deliverable* good?)

- Does it meet every acceptance criterion in the WBS Dictionary?
- Does it meet every applicable quality standard from `quality-management-plan.md`?
- Has it been inspected/tested by the method stated in the Quality Control Approach table?
- Are all defects found during inspection logged (not silently fixed and forgotten)?

## Common Quality Metrics Catalog (pick what fits the deliverable type; don't force all of these)

| Deliverable Type | Candidate Metric | Typical Target Shape |
|---|---|---|
| Any reviewed artifact | Review coverage | 100% of deliverables reviewed before Done |
| Software/code | Defect density | Defects per unit (KLOC, per feature, etc.) |
| Software/code | Escape rate | % of defects found after "Done" vs. before |
| Data migration | Validation pass rate | % of records passing an integrity check |
| Content/documentation | Accuracy rate | % matching source-of-truth on spot-check |
| Any process | Audit pass rate | % of process audits with zero findings |
| Vendor deliverables | On-spec delivery rate | % of vendor deliverables passing QA gate first try |

## Common Mistakes to Avoid

- Don't set a metric target without a measurement method — "high quality" isn't measurable;
  "≥98% caption accuracy per automated diff tool" is.
- Don't conflate QA and QC in the same checklist item — "code review happened" is QA (process);
  "this specific PR has zero linter errors" is QC (product).
- A metric with no one accountable for measuring it will quietly stop being tracked — assign an
  owner in the Quality Control Approach table, not just a target.
