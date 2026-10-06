# Coffee Machine

A console game from Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*
(day 15). A virtual coffee machine serves espresso, latte and cappuccino. Pay with
US coins (quarters, dimes, nickels and pennies). The machine checks its water, milk
and coffee before it serves, refunds you if you pay too little and gives change if
you pay too much.

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is your latte. Enjoy!
```

- Python 3.13 or newer, no runtime dependencies.
- Type `report` to see the water, milk, coffee and money in the machine, and `off`
  to switch the machine off.
- The function names follow the assignment: `is_resource_sufficient`,
  `process_coins`, `is_transaction_successful`, `make_coffee`.
- Money is counted in whole cents inside the program, so change is never off by a
  rounding error.

## Requirements

- [Python](https://www.python.org/downloads/) 3.13 or newer
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation

## Set up

Create a local virtual environment in `.venv`, activate it, and upgrade `pip`.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Windows (Git Bash), Linux and macOS:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
```

The machine itself needs nothing more. To run the tests and the code checks, install
the development tools:

```bash
python -m pip install -e ".[dev]"
```

## Run the coffee machine

```bash
python -m coffee_machine
```

Type `espresso`, `latte` or `cappuccino` and press Enter, then enter the coins.
Type `report` for the machine's resources, or `off` to quit.

## Run the tests

```bash
python -m pytest
```

Check the code style and types:

```bash
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src tests
```

## Continuous integration

On every push and pull request, `.gitea/workflows/ci.yml` installs the project on
Python 3.13 and runs the same checks as above: `pytest`, `ruff check`,
`ruff format --check` and `mypy`. To run all of them locally:

```bash
python -m pytest && python -m ruff check src tests && python -m ruff format --check src tests && python -m mypy src tests
```

## Build the source documentation

The source uses Doxygen comments. The HTML output goes to `docs/doxygen/html`.

```bash
doxygen Doxyfile
```

## Project layout

| Path | Content |
| --- | --- |
| `src/coffee_machine/` | The machine: `main.py` (the loop), `constants.py` (menu, coins, starting resources) |
| `tests/` | pytest tests |
| `docs/` | Planning and review documents (business case, plan, milestones) |
| `pyproject.toml` | Project configuration |
| `Doxyfile` | Doxygen configuration |
| `.gitea/workflows/` | CI workflow |

## License

GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
