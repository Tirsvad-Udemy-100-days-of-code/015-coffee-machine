"""!
@file test_smoke.py
@brief Smoke test that the package imports.
"""

import pytest

from coffee_machine import main as main_module


def test_main_is_callable(monkeypatch: pytest.MonkeyPatch) -> None:
    """!
    @brief The entry point starts and stops on "off".
    """
    monkeypatch.setattr("builtins.input", lambda _prompt: "off")
    main_module.main()
