# RC-006 Source Code Review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-006 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [00d47e2] |

---

## Artifact Under Review

- Instance reviewed: `src/coffee_machine/` and `tests/` at the state of MIL-003 (`main` after PR 22)
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Independence: S01 is the only stakeholder and is also the recorded author, so the reviewer-is-not-author rule cannot be met. The code and documents were written by Claude on S01's behalf; S01 reviews and signs. This is a known limit of a one-person project, not a clean independent review.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions and variables are `snake_case`, constants `UPPER_SNAKE`, `Drink` is `PascalCase`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`is_resource_sufficient`, `process_coins`); the only short names are loop variables. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; no suppression comments. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, including tests and the nested `feed`, is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`. `_ask_coin_count` catches only `ValueError` and answers it by asking again, so nothing is swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | The program opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | All modules, public functions and tests have Doxygen docstrings that say what the code does. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging exists. `print` is the program's own console output, not diagnostics. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; the plan treats the work as plain technical tasks. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 19 tests named for behaviour, independent of order, no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` runs clean and `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Runtime dependencies: none. The dev tools had no lower bounds for ruff and mypy; fixed by action item 1, which sets `pytest>=9`, `ruff>=0.16`, `mypy>=2.4` (the tested versions). |

## Overall Verdict

Go — every mandatory criterion passes or is N-A. The one Fail (13) is optional and is fixed in the same change by issue #25.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Set lower bounds for the dev dependencies in pyproject.toml (done) | S01 | 2026-10-06 |

---

[MIL-004]: ../../milestones/mil-004-code-review-and-ci.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[00d47e2]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/015-coffee_machine/commit/00d47e244c82007bbc55e18312649189b175ec10
