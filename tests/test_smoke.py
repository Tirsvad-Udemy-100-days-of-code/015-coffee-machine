"""!
@file test_smoke.py
@brief Smoke test that the package imports.
"""

from coffee_machine import main as main_module


def test_main_is_callable() -> None:
    """!
    @brief The entry point runs without error.
    """
    main_module.main()
