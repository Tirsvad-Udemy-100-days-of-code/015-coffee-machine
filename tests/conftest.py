"""!
@file conftest.py
@brief Shared pytest helpers.
"""

from collections.abc import Callable, Iterable

import pytest

ScriptInput = Callable[[Iterable[str]], None]


@pytest.fixture
def script_input(monkeypatch: pytest.MonkeyPatch) -> ScriptInput:
    """!
    @brief Provide a function that feeds the given answers to `input`.
    @param monkeypatch pytest's monkeypatch fixture.
    @return A function taking the answers in the order they are asked.
    """

    def feed(answers: Iterable[str]) -> None:
        remaining = iter(answers)
        monkeypatch.setattr("builtins.input", lambda _prompt: next(remaining))

    return feed
