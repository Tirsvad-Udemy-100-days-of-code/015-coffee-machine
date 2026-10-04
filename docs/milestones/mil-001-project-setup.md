# MIL-001 Project Setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-05 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project skeleton and tooling are ready for feature work.

## Deliverable

Repository skeleton: `src/`, `tests/`, `docs/`, `pyproject.toml`, `.gitignore`, `Doxyfile`, README with venv instructions.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` succeeds in a fresh `.venv` on Python 3.13+ | Succeeds | Fails |
| 2 | `python -m pytest` runs without configuration errors | Runs | Errors |
| 3 | README documents `.venv` creation and `python -m pip install --upgrade pip` | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 (documented setup) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-07 — within the short course-assignment timeline in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Declare the package with `requires-python >=3.13`, an empty runtime dependency list, a `dev` extra with pytest, and pytest config (`testpaths`, `pythonpath = ["src"]`). | No | Objective 4 |
| 2 | Verify Python .gitignore | Confirm the existing `.gitignore` ignores `.venv/`, `.env`, `__pycache__/`, `.pytest_cache/` and Doxygen output (`docs/doxygen/`); add what is missing. | No | Objective 4 |
| 3 | Add Doxyfile | Create a Doxyfile that scans `src/`, writes HTML to `docs/doxygen/`, and is configured for Python (`OPTIMIZE_OUTPUT_JAVA`, `EXTRACT_ALL`). Source comments use Doxygen style. | No | Objective 4 |
| 4 | Create src and tests skeleton | Create `src/coffee_machine/` with `__init__.py`, `constants.py` and `main.py` stubs, and `tests/` with a smoke test, following the `coding-conventions` skill. | No | Objective 1 |
| 5 | Write README with setup instructions | Write README.md: project description, how to create and use a local `.venv`, `python -m pip install --upgrade pip`, install, run, test and Doxygen. The README template from the request was not supplied; ask for it before writing. | No | Objective 4 |

---

[BC-001]: ../business-case.md
