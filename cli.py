import click
from datetime import datetime
from aocd import get_data, submit as aocd_submit
from pathlib import Path
import yaml
from importlib import import_module
import sys
from string import Template

sys.path.append(str(Path.cwd()))


TODAY = datetime.now().day
CURRENT_YEAR = datetime.now().year

ENTRYPOINTS_FILE = Path("entrypoints.yaml")
SOLUTION_TEMPLATE_FILE = Path("templates", "solution.template.py")
TEST_TEMPLATE_FILE = Path("templates", "test.template.py")

with open(ENTRYPOINTS_FILE) as f:
    ENTRYPOINTS = yaml.safe_load(f) or {}

with open(SOLUTION_TEMPLATE_FILE) as f:
    SOLUTION_TEMPLATE = f.read()

with open(TEST_TEMPLATE_FILE) as f:
    TEST_TEMPLATE = f.read()


def get_templates():
    return SOLUTION_TEMPLATE, Template(TEST_TEMPLATE)


def update_entrypoints():
    with open(ENTRYPOINTS_FILE, "w") as f:
        yaml.safe_dump(ENTRYPOINTS, f)


def get_day_path(year: int, day: int):
    return Path(f"y{year}", f"d{day:02d}")


def get_day_module(year: int, day: int, module_name: str, test=False):
    return f"y{year}.d{day:02d}.{'test_' if test else ''}{module_name}"


def get_module(year: int, day: int, test=False):
    module_name = ENTRYPOINTS.get(year, {}).get(day)

    if not module_name:
        click.BadParameter(f"Year {year} day {day} is not initialized yet")

    module = get_day_module(year, day, module_name, test)

    return import_module(module)


def get_solution(year: int, day: int, part: int):
    m = get_module(year, day)
    solve_fn = getattr(m, f"part_{part}")

    input_path = get_day_path(year, day) / "input.txt"

    if not input_path.is_file():
        input_string = get_data(year=year, day=day)

        with open(input_path, "w") as f:
            f.write(input_string)
    else:
        with open(input_path) as f:
            input_string = f.read()

    return solve_fn(input_string)


def find_puzzle(selector: list[str]):
    year = CURRENT_YEAR
    day = TODAY
    part = "a"

    match len(selector):
        case 3:
            year, day, part = selector
        case 2:
            if selector[1] in ["a", "b"]:
                day, part = selector
            else:
                year, day = selector
        case 1:
            day = selector[0]

    return int(year), int(day), part


def test_solution(year: int, day: int, part: int):
    m = get_module(year, day, test=True)

    test_input = m.TEST_INPUT
    solve_fn = getattr(m, f"part_{part}")

    click.echo(solve_fn(test_input))


arg_module_name = click.argument("module_name")
arg_selector = click.argument("selector", nargs=-1)


@click.command()
@arg_module_name
@arg_selector
def prepare(module_name, selector):
    year, day, _ = find_puzzle(selector)

    input_data = get_data(year=year, day=day)
    solution_template, test_template = get_templates()

    puzzle_path = get_day_path(year, day)
    puzzle_path.mkdir(parents=True, exist_ok=True)

    with open(puzzle_path / "input.txt", "w") as f:
        f.write(input_data)

    with open(puzzle_path / f"{module_name}.py", "w") as f:
        f.write(solution_template)

    with open(puzzle_path / f"test_{module_name}.py", "w") as f:
        f.write(test_template.substitute(module=get_day_module(year, day, module_name)))

    ENTRYPOINTS[year] = ENTRYPOINTS.get(year, {})
    ENTRYPOINTS[year][day] = module_name
    update_entrypoints()


@click.command()
@arg_selector
def test(selector):
    year, day, part = find_puzzle(selector)
    test_solution(year, day, part)


@click.command()
@arg_selector
def solve(selector):
    year, day, part = find_puzzle(selector)

    click.echo(get_solution(year, day, part))


@click.command()
@arg_selector
def submit(selector):
    year, day, part = find_puzzle(selector)

    solution = get_solution(year, day, part)

    if not solution:
        raise click.ClickException("Nothing to submit")

    aocd_submit(solution, year=year, day=day, part=part)
