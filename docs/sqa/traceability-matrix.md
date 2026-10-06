# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-06 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-10-06 | Proposed | Jens Tirsvad Nielsen | S01 | Added MIL-004 | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability can be measured. A row is added or updated whenever an
artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- |
| [SA-001] | Stakeholder Analysis | - | [BC-001] | [RC-002] |
| [BC-001] | Business Case | [SA-001] | [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-001] |
| [PP-001] | Project Plan | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | - |
| [MIL-001] | Milestone | [BC-001], [PP-001] | - | [RC-003] |
| [MIL-002] | Milestone | [BC-001], [PP-001] | - | [RC-004] |
| [MIL-003] | Milestone | [BC-001], [PP-001] | - | [RC-005] |
| [MIL-004] | Milestone | [BC-001], [PP-001] | - | - |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream, nothing is built on it yet; in Last Reviewed, no `RC-*` exists yet.
- [PP-001] has no QC checklist in the framework, so it has no `RC-*`.
- No use case, domain model, design or data artifacts exist; the plan treats all tasks as plain technical tasks. The source code is covered by the tests, not by an `RC-*`.

---

[SA-001]: ../stakeholder-analysis.md
[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-coffee-machine-core.md
[MIL-003]: ../milestones/mil-003-quality-and-publication.md
[MIL-004]: ../milestones/mil-004-code-review-and-ci.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
