# MIL-003 Quality and Publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-05 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project is tested, documented and ready to share.

## Deliverable

pytest suite, Doxygen output, finished README, and repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes with all tests green | All pass | Any failure |
| 2 | `doxygen Doxyfile` runs without warnings on `src/` | No warnings | Warnings |
| 3 | Repository has a description and at least 3 topics | Set | Missing |
| 4 | `pyproject.toml` lists no runtime dependencies and `.env` is not imported or tested | Confirmed | Violated |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Behaviour must exist before it is tested and published |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3, 4, 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-12 — within the short course-assignment timeline in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write tests for resources and report | pytest tests for `report` output and `is_resource_sufficient` with sufficient and insufficient resources. | No | Objective 3 |
| 2 | Write tests for coins and transactions | pytest tests for `process_coins` (mocked input), refund, exact payment, change and profit updates. | No | Objective 3 |
| 3 | Write tests for make_coffee and main loop | pytest tests for resource deduction and for `off`, `report` and invalid input handling through mocked `input`. | No | Objective 3 |
| 4 | Generate and check Doxygen output | Run `doxygen Doxyfile`; fix undocumented or malformed comments. | No | Objective 4 |
| 5 | Set repository description and topics | Use the git host API with the token in `.env` (personal use only, never imported by the project) to set the description and topics, after the user confirms the exact text. | No | Objective 5 |

---

[BC-001]: ../business-case.md
