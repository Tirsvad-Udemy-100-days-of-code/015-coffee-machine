"""!
@file test_machine.py
@brief Tests for making drinks and the main loop.
"""

import pytest

from coffee_machine.constants import MENU
from coffee_machine.main import main, make_coffee
from tests.conftest import ScriptInput

COINS_FOR_LATTE = ["10", "0", "0", "0"]
NO_COINS = ["0", "0", "0", "0"]
FULL_REPORT = "Water: 300ml\nMilk: 200ml\nCoffee: 100g\nMoney: $0.00"


def test_make_coffee_uses_up_ingredients(capsys: pytest.CaptureFixture[str]) -> None:
    """!
    @brief The drink's ingredients are deducted and the drink is served.
    """
    resources = {"water": 300, "milk": 200, "coffee": 100}
    make_coffee("latte", MENU["latte"]["ingredients"], resources)
    assert resources == {"water": 100, "milk": 50, "coffee": 76}
    assert capsys.readouterr().out == "Here is your latte. Enjoy!\n"


def test_off_ends_the_machine(script_input: ScriptInput) -> None:
    """!
    @brief Typing off returns from the loop.
    """
    script_input(["off"])
    main()


def test_report_shows_starting_resources(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief A fresh machine reports full resources and no money.
    """
    script_input(["report", "off"])
    main()
    assert FULL_REPORT in capsys.readouterr().out


def test_unknown_input_is_rejected(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief Anything that is not a drink or command prints a message.
    """
    script_input(["tea", "off"])
    main()
    assert "Sorry, we do not serve that." in capsys.readouterr().out


def test_sale_updates_resources_and_profit(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief A paid drink is served, resources drop and profit rises by the price.
    """
    script_input(["latte", *COINS_FOR_LATTE, "report", "off"])
    main()
    out = capsys.readouterr().out
    assert "Here is your latte. Enjoy!" in out
    assert "Water: 100ml\nMilk: 50ml\nCoffee: 76g\nMoney: $2.50" in out


def test_refund_changes_nothing(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief An underpaid order is refunded: no drink, no profit.
    """
    script_input(["espresso", *NO_COINS, "report", "off"])
    main()
    out = capsys.readouterr().out
    assert "Money refunded." in out
    assert "Enjoy" not in out
    assert FULL_REPORT in out


def test_overpayment_adds_only_price_to_profit(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief Change is returned and only the price is counted as profit.
    """
    script_input(["espresso", "7", "0", "0", "0", "report", "off"])
    main()
    out = capsys.readouterr().out
    assert "Here is $0.25 in change." in out
    assert "Money: $1.50" in out


def test_order_refused_when_resources_run_out(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief After the water is used up, the next order is refused before payment.
    """
    script_input(["latte", *COINS_FOR_LATTE, "latte", "off"])
    main()
    out = capsys.readouterr().out
    assert out.count("Please insert coins.") == 1
    assert "Sorry there is not enough water." in out
