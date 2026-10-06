# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-06 | Accepted | Jens Tirsvad Nielsen | S01 | Added duration constraint (RC-001 action) | [8ef00aa] |
| 2026-10-06 | Proposed | Jens Tirsvad Nielsen | S01 | Added objective 6 and scope for code review and CI | [8ef00aa] |

---

## Executive Summary

Build a console coffee machine in Python as the Day 15 assignment of Udemy's
"100 Days of Code: The Complete Python Pro Bootcamp". The program serves
espresso, latte and cappuccino, accepts US coins, tracks water, milk and coffee
and prints a report on request. It is published as a readable, runnable
reference for other course participants and as a portfolio piece.

## Methodological and Standards Foundation

Planning follows the SQA/QC framework mounted at `framework/` (plan first, then
code). Quality is described with ISO/IEC 25010:2023 characteristics. Code uses
the `coding-conventions` skill and Doxygen comments.

## Problem Statement

The assignment specification is long and detail-heavy (resources, coins,
refunds, change). Solutions shared by participants vary widely in structure and
readability, and a single `main.py` script is hard to test.

## Business Opportunity

A small, well-structured and tested solution is a clear example for other
participants and for viewers browsing the repository.

## Objectives

1. Implement the full assignment behaviour: `report`, `off`, drink selection, resource check, coin processing, change, profit.
2. Keep the assignment's function names so participants can compare solutions.
3. Cover the behaviour with automated pytest tests.
4. Document how to set up a local `.venv` and run the program and tests.
5. Publish the repository with a description, topics and README.
6. Review the source code against the Python quality checklist and run the tests and code checks automatically on every push.

## Scope

### In Scope

- Console program under `src/` with a `constants.py` for menu, coins and starting resources.
- pytest tests under `tests/`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md`.
- Project documents under `docs/`.
- Repository description and topics on the git host.
- A review record for the source code and a CI workflow (MIL-004).

### Out of Scope

- Graphical or web interface.
- Payment other than the four US coins.
- Persistence of resources or profit between runs.
- Runtime dependencies.

## Expected Benefits

### Tangible Benefits

- Completed Day 15 assignment.
- Runnable code with tests and setup instructions.

### Intangible Benefits

- Practice with planning, testing and Python project layout.
- A reusable template for later course projects.

## Strategic Alignment

Supports the learner's goal of finishing the 100 Days of Code course with
professional project hygiene, and the goal of sharing readable solutions.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Assignment behaviours implemented | 100% of listed behaviours | Manual run against the specification |
| 2 | Tests pass | All pytest tests green | `python -m pytest` |
| 3 | Runtime dependencies | 0 | `pyproject.toml` `dependencies` is empty |
| 4 | Setup documented | A new reader can run program and tests from README | README walkthrough |
| 5 | Repository metadata | Description and at least 3 topics set | Repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Floating-point rounding in coin totals | Wrong change or refund | Compute money in cents (integers) internally |
| Token in `.env` leaks | Account compromise | `.env` is gitignored, never imported or tested by the project |
| Scope creep beyond the assignment | Delay | Out of Scope list above |

## Assumptions

- Python 3.13 or newer is installed.
- The git host repository already exists and is reachable.

## Constraints

- Python greater than 3.13 as requested, `venv` for environments, pytest for tests.
- Constants live in `constants.py`.
- Source files use Doxygen comments.
- Nothing is committed or pushed unless the user asks.
- Duration: one week, 2026-10-05 to 2026-10-12.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few hours of the learner's time | Finished, tested, shareable assignment (qualitative; no money involved) |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment and owns the plan, code and review |
| S02 | Reads and runs the code, compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, well specified and delivers a reusable example.

---

[SA-001]: ./stakeholder-analysis.md
[8ef00aa]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/015-coffee_machine/commit/8ef00aafaaa193ea565f1a45238d31e963a5e05d
