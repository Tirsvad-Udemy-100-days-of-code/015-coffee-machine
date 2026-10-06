"""!
@file main.py
@brief Entry point and logic of the coffee machine.
"""

from coffee_machine.constants import (
    CENTS_PER_DOLLAR,
    COIN_VALUES,
    COMMAND_OFF,
    COMMAND_REPORT,
    INITIAL_RESOURCES,
    MENU,
    MESSAGE_INSERT_COINS,
    MESSAGE_INVALID_NUMBER,
    MESSAGE_NOT_ENOUGH_MONEY,
    MESSAGE_UNKNOWN_DRINK,
    PROMPT_ORDER,
    RESOURCE_UNITS,
)


def format_money(cents: int) -> str:
    """!
    @brief Format an amount in cents as dollars.
    @param cents Amount in whole cents.
    @return The amount such as "$2.50".
    """
    return f"${cents / CENTS_PER_DOLLAR:.2f}"


def report(resources: dict[str, int], profit: int) -> None:
    """!
    @brief Print the resources left in the machine and the money earned.
    @param resources Remaining amount of each resource.
    @param profit Money earned so far, in cents.
    """
    for name, amount in resources.items():
        print(f"{name.capitalize()}: {amount}{RESOURCE_UNITS[name]}")
    print(f"Money: {format_money(profit)}")


def is_resource_sufficient(
    order_ingredients: dict[str, int], resources: dict[str, int]
) -> bool:
    """!
    @brief Check that the machine has enough of every ingredient for an order.
    @param order_ingredients Amount of each ingredient the drink needs.
    @param resources Remaining amount of each resource.
    @return True if every ingredient is available, otherwise False after
            printing the first missing one.
    """
    for name, needed in order_ingredients.items():
        if needed > resources[name]:
            print(f"Sorry there is not enough {name}.")
            return False
    return True


def _ask_coin_count(coin_name: str) -> int:
    """!
    @brief Ask how many coins of one kind are inserted, until the answer is valid.
    @param coin_name Plural coin name, such as "quarters".
    @return The number of coins, zero or more.
    """
    while True:
        answer = input(f"How many {coin_name}?: ")
        try:
            count = int(answer)
        except ValueError:
            count = -1
        if count >= 0:
            return count
        print(MESSAGE_INVALID_NUMBER)


def process_coins() -> int:
    """!
    @brief Ask for the coins and total their value.
    @return The total inserted, in cents.
    """
    print(MESSAGE_INSERT_COINS)
    return sum(
        _ask_coin_count(coin_name) * value for coin_name, value in COIN_VALUES.items()
    )


def is_transaction_successful(money_received: int, drink_cost: int) -> bool:
    """!
    @brief Check the payment, refund it if too small, otherwise give change.
    @param money_received Money inserted, in cents.
    @param drink_cost Price of the drink, in cents.
    @return True if the payment covers the price, otherwise False.
    """
    if money_received < drink_cost:
        print(MESSAGE_NOT_ENOUGH_MONEY)
        return False
    change = money_received - drink_cost
    if change > 0:
        print(f"Here is {format_money(change)} in change.")
    return True


def make_coffee(
    drink_name: str, order_ingredients: dict[str, int], resources: dict[str, int]
) -> None:
    """!
    @brief Use up the drink's ingredients and serve it.
    @param drink_name Name of the drink.
    @param order_ingredients Amount of each ingredient the drink needs.
    @param resources Remaining amount of each resource; updated in place.
    """
    for name, needed in order_ingredients.items():
        resources[name] -= needed
    print(f"Here is your {drink_name}. Enjoy!")


def main() -> None:
    """!
    @brief Run the coffee machine until the user types "off".
    """
    resources = dict(INITIAL_RESOURCES)
    profit = 0
    while True:
        choice = input(PROMPT_ORDER).strip().lower()
        if choice == COMMAND_OFF:
            return
        if choice == COMMAND_REPORT:
            report(resources, profit)
        elif choice in MENU:
            drink = MENU[choice]
            if not is_resource_sufficient(drink["ingredients"], resources):
                continue
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                profit += drink["cost"]
                make_coffee(choice, drink["ingredients"], resources)
        else:
            print(MESSAGE_UNKNOWN_DRINK)
