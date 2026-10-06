"""!
@file constants.py
@brief Constants for the coffee machine: menu, coins, starting resources, texts.

Money is stored in whole cents so that sums and change are exact.
"""

from typing import TypedDict


class Drink(TypedDict):
    """!
    @brief A menu entry: the ingredients it needs and its price.
    """

    ingredients: dict[str, int]
    cost: int


MENU: dict[str, Drink] = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 150},
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 300,
    },
}

## Value of each US coin in cents, in the order the machine asks for them.
COIN_VALUES: dict[str, int] = {
    "quarters": 25,
    "dimes": 10,
    "nickels": 5,
    "pennies": 1,
}

INITIAL_RESOURCES: dict[str, int] = {"water": 300, "milk": 200, "coffee": 100}

## Unit printed after each resource in the report.
RESOURCE_UNITS: dict[str, str] = {"water": "ml", "milk": "ml", "coffee": "g"}

CENTS_PER_DOLLAR = 100

COMMAND_REPORT = "report"
COMMAND_OFF = "off"

PROMPT_ORDER = "What would you like? (espresso/latte/cappuccino): "
MESSAGE_INSERT_COINS = "Please insert coins."
MESSAGE_NOT_ENOUGH_MONEY = "Sorry that's not enough money. Money refunded."
MESSAGE_UNKNOWN_DRINK = "Sorry, we do not serve that."
MESSAGE_INVALID_NUMBER = "Please enter a whole number of coins, zero or more."
