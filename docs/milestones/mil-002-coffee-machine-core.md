# MIL-002 Coffee Machine Core

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-05 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the machine behaves as the assignment specification requires.

## Deliverable

Working console program in `src/coffee_machine/` implementing report, off, drink selection, resource check, coin processing, change and profit.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Typing `report` prints water, milk, coffee and money | Matches spec format | Differs |
| 2 | A drink is refused when a resource is insufficient, naming the resource | Refused with message | Served or no message |
| 3 | Insufficient coins refund everything with the spec's refund message | Refunded | Drink served |
| 4 | Excess coins return correct change and add only the price to profit | Correct | Wrong amount |
| 5 | Typing `off` ends the program | Exits | Keeps running |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Skeleton and tooling must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-10 — within the short course-assignment timeline in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define constants | Put `MENU`, `COIN_VALUES` and `INITIAL_RESOURCES` in `constants.py`, from the assignment's starting data. | No | Objective 1 |
| 2 | Implement report | Print water (ml), milk (ml), coffee (g) and money ($) in the assignment's format. | No | Objective 1 |
| 3 | Implement is_resource_sufficient | Check an order against current resources; print the not-enough-resource message and return False when short. Keep the assignment's function name. | No | Objective 2 |
| 4 | Implement process_coins | Ask for quarters, dimes, nickels and pennies and return the total, using integer cents internally to avoid float errors. | No | Objective 1 |
| 5 | Implement is_transaction_successful | Compare payment with cost; refund if short, otherwise return change rounded to 2 decimals and add the cost to profit. | No | Objective 1 |
| 6 | Implement make_coffee | Deduct the drink's ingredients from resources and print the enjoy message. | No | Objective 1 |
| 7 | Implement main loop | Prompt for espresso/latte/cappuccino, handle `report`, `off` and invalid input, and wire the functions together. | No | Objective 1 |

---

[BC-001]: ../business-case.md
