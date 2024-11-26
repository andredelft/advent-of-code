import click
from datetime import datetime
from aocd import get_data, submit as aocd_submit
from pathlib import Path
from importlib import import_module
import sys

sys.path.append(str(Path.cwd()))

from templates import get_templates
from entrypoints import entrypoints


CURRENT_DAY = datetime.now().day
CURRENT_YEAR = datetime.now().year


def get_folder(year: int, day: int):
    return Path(f"y{year}", f"d{day:02d}")


def get_module_path(year: int, day: int, module_name: str, is_test=False):
    return f"y{year}.d{day:02d}.{'test_' if is_test else ''}{module_name}"


def get_module(year: int, day: int, is_test=False):
    module_name = entrypoints[year, day]

    module_path = get_module_path(year, day, module_name, is_test)

    return import_module(module_path)


def identify_puzzle(selector: list[str]):
    year = CURRENT_YEAR
    day = min(CURRENT_DAY, 25)
    part = "a"

    for el in selector:
        try:
            value = int(el)
        except ValueError:
            if el in ["a", "b"]:
                part = el
        else:
            if 1 <= value <= 25:
                day = value
            elif 2015 <= value <= CURRENT_YEAR:
                year = value

    return year, day, part


def get_solution(year: int, day: int, part: int):
    m = get_module(year, day)
    solve_fn = getattr(m, f"solve_{part}")

    input_path = get_folder(year, day) / "input.txt"

    if not input_path.is_file():
        input_string = get_data(year=year, day=day)

        with open(input_path, "w") as f:
            f.write(input_string)
    else:
        with open(input_path) as f:
            input_string = f.read()

    return solve_fn(input_string)


def test_solution(year: int, day: int, part: int):
    m = get_module(year, day, is_test=True)

    test_input = m.TEST_INPUT
    solve_fn = getattr(m, f"solve_{part}")

    click.echo(solve_fn(test_input))


arg_module_name = click.argument("module_name")
arg_selector = click.argument("selector", nargs=-1)


@click.command()
@arg_module_name
@arg_selector
def prepare(module_name, selector):
    year, day, _ = identify_puzzle(selector)

    input_data = get_data(year=year, day=day)
    solution_template, test_template = get_templates()

    puzzle_folder = get_folder(year, day)
    puzzle_folder.mkdir(parents=True, exist_ok=True)

    with open(puzzle_folder / "input.txt", "w") as f:
        f.write(input_data)

    with open(puzzle_folder / f"{module_name}.py", "w") as f:
        f.write(solution_template)

    with open(puzzle_folder / f"test_{module_name}.py", "w") as f:
        f.write(
            test_template.substitute(module=get_module_path(year, day, module_name))
        )

    entrypoints[year, day] = module_name


@click.command()
@arg_selector
def test(selector):
    year, day, part = identify_puzzle(selector)

    test_solution(year, day, part)


@click.command()
@arg_selector
def solve(selector):
    year, day, part = identify_puzzle(selector)

    click.echo(get_solution(year, day, part))


@click.command()
@arg_selector
def submit(selector):
    year, day, part = identify_puzzle(selector)

    solution = get_solution(year, day, part)

    if not solution:
        raise click.ClickException("Nothing to submit")

    aocd_submit(solution, year=year, day=day, part=part)
