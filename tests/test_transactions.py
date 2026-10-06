"""!
@file test_transactions.py
@brief Tests for coin processing and payment.
"""

import pytest

from coffee_machine.main import is_transaction_successful, process_coins
from tests.conftest import ScriptInput


def test_process_coins_totals_in_cents(script_input: ScriptInput) -> None:
    """!
    @brief Quarters, dimes, nickels and pennies add up to the right total.
    """
    script_input(["4", "3", "2", "1"])
    assert process_coins() == 4 * 25 + 3 * 10 + 2 * 5 + 1


def test_process_coins_asks_again_on_invalid_count(
    script_input: ScriptInput, capsys: pytest.CaptureFixture[str]
) -> None:
    """!
    @brief Text and negative counts are rejected and asked again.
    """
    script_input(["abc", "-1", "2", "0", "0", "0"])
    assert process_coins() == 50
    assert capsys.readouterr().out.count("Please enter a whole number") == 2


def test_transaction_refused_when_too_little(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """!
    @brief Too little money is refunded with the refund message.
    """
    assert not is_transaction_successful(100, 150)
    assert "Sorry that's not enough money. Money refunded." in capsys.readouterr().out


def test_transaction_accepted_with_exact_payment(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """!
    @brief Exact payment succeeds and gives no change.
    """
    assert is_transaction_successful(150, 150)
    assert "change" not in capsys.readouterr().out


def test_transaction_gives_change(capsys: pytest.CaptureFixture[str]) -> None:
    """!
    @brief Overpaying succeeds and returns the difference.
    """
    assert is_transaction_successful(175, 150)
    assert capsys.readouterr().out == "Here is $0.25 in change.\n"
