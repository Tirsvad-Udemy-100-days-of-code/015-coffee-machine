# MIL-004 Code Review and CI

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-06 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [8ef00aa] |

---

## Purpose

Decide whether the source code has been reviewed against the Python quality checklist and is checked automatically on every push.

## Deliverable

`RC-006` review record for the source code, fixes for its findings, a CI workflow running the tests and code checks, and a README section describing it.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/sqa/reviews/` has an RC record for the source against `QC-PY-001` | Present with a verdict | Missing |
| 2 | Every Fail in that record has a closed action item or a recorded deviation | All handled | Open Fail |
| 3 | The CI workflow runs pytest, ruff check, ruff format --check and mypy on push and pull request | All four run | Any missing |
| 4 | The latest CI run on `main` is green | Green | Red or none |
| 5 | README describes the CI and the matching local commands | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Tests and metadata must exist before they are reviewed and automated |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6 (review and CI), Objective 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-12 — inside the duration constraint in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Review source code against QC-PY-001 | Create RC-006 with `new-artifact.sh RC` for `src/` and `tests/` against `framework/qc/qc-programming-python.md`. Criterion 10 (Design Class Diagram) is N-A because no DCD exists. Every Fail becomes an action item. | No | Objective 6 |
| 2 | Fix code review findings | Fix each Fail from RC-006 under `src/` and `tests/`, or record a justified deviation in the record. If the review has no Fail, close this task without a code change. | No | Objective 6 |
| 3 | Add CI workflow | Add `.gitea/workflows/ci.yml` that sets up Python 3.13, installs `.[dev]`, and runs `pytest`, `ruff check`, `ruff format --check` and `mypy` on push and pull request. Check first that the git host has an Actions runner. | No | Objective 6 |
| 4 | Document CI in README | Add a short section to README.md saying what the CI runs and how to run the same checks locally. | No | Objective 4 |
| 5 | Update traceability matrix | Add the RC-006 review to `docs/sqa/traceability-matrix.md` and close the milestone's row there. | No | Objective 6 |

---

[BC-001]: ../business-case.md
[8ef00aa]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/015-coffee_machine/commit/8ef00aafaaa193ea565f1a45238d31e963a5e05d
