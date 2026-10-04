# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-05 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Identify who is affected by the coffee machine project and what each needs,
using a power/interest grid (Manage Closely, Keep Satisfied, Keep Informed,
Monitor).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Self | High | High | Manage Closely | Finish the assignment correctly with clean structure |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | Low | High | Keep Informed | Readable, runnable code with the assignment's function names, and README run instructions |
| S03 | GitHub viewers | Repository browsers | Public | Low | Low | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews everything.
- **Keep Informed (S02):** cannot change the project but depend on its clarity.
- **Monitor (S03):** casual visitors; a good first impression is enough.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Correct behaviour per specification | Functionality |
| S01 | Tested and maintainable | Supportability |
| S02 | Easy to read and run | Usability |
| S02 | Same function names as the assignment | Functionality |
| S03 | Quick understanding of the repository | Usability |
| S03 | No dependencies to install | Implementation (+) |

## Communication Requirements

| Stakeholder | Channel | Frequency | Deliverable | Phase |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Working tree changes, PR | MIL-001 to MIL-003 |
| S02 | README | At publication | Run and test instructions | MIL-003 |
| S03 | Repository page | At publication | Description, topics, README | MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Mitigation |
| --- | --- |
| S02 want assignment-style function names; S01 wants testable structure | Keep the assignment's names (`is_resource_sufficient`, `process_coins`, `is_transaction_successful`, `make_coffee`) and make them pure/parameterised so they are testable |

## Traceability Analysis

| Stakeholder | Goal / use case | Business Case objective |
| --- | --- | --- |
| S01 | Operate the machine (order, report, off) | [BC-001] objectives 1, 3 |
| S02 | Read and run the code | [BC-001] objectives 2, 4 |
| S03 | Browse the repository | [BC-001] objective 5 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
