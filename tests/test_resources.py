"""!
@file test_resources.py
@brief Tests for the report and the resource check.
"""

import pytest

from coffee_machine.constants import INITIAL_RESOURCES, MENU
from coffee_machine.main import format_money, is_resource_sufficient, report


def test_format_money_shows_two_decimals() -> None:
    """!
    @brief Cents are shown as dollars with two decimals.
    """
    assert format_money(250) == "$2.50"
    assert format_money(0) == "$0.00"


def test_report_prints_resources_and_money(capsys: pytest.CaptureFixture[str]) -> None:
    """!
    @brief The report lists each resource with its unit, then the money.
    """
    report({"water": 300, "milk": 200, "coffee": 100}, 250)
    assert capsys.readouterr().out == (
        "Water: 300ml\nMilk: 200ml\nCoffee: 100g\nMoney: $2.50\n"
    )


def test_is_resource_sufficient_when_enough() -> None:
    """!
    @brief An order is accepted when every ingredient is available.
    """
    assert is_resource_sufficient(MENU["latte"]["ingredients"], INITIAL_RESOURCES)


def test_is_resource_sufficient_when_exactly_enough() -> None:
    """!
    @brief Using up an ingredient completely is allowed.
    """
    assert is_resource_sufficient({"water": 300}, {"water": 300})


def test_is_resource_sufficient_names_missing_resource(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """!
    @brief A short ingredient is refused and named.
    """
    resources = {"water": 300, "milk": 100, "coffee": 100}
    assert not is_resource_sufficient(MENU["latte"]["ingredients"], resources)
    assert capsys.readouterr().out == "Sorry there is not enough milk.\n"
