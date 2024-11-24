import re
import math
from lib.regex import parse_numbers, parse_number
from lib.array import product
from .monkey import Monkey

TEST_INPUT = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def parse_input(input_string: str) -> list[Monkey]:
    monkeys = []
    for monkey_str in input_string.split("\n\n"):
        lines = monkey_str.split("\n")
        starting_items = parse_numbers(lines[1])
        m = re.search(r"(?:old|\d+) (?:\*|\+) (?:old|\d+)", lines[2])
        operation = m.group()
        divisible_by = parse_number(lines[3])
        throw_true = parse_number(lines[4])
        throw_false = parse_number(lines[5])
        monkeys.append(
            Monkey(starting_items, operation, divisible_by, throw_true, throw_false)
        )
    return monkeys


def part_a(input_string=TEST_INPUT):
    monkeys = parse_input(input_string)
    for _ in range(20):
        for monkey in monkeys:
            throw_dict = monkey.inspect()
            for i, items in throw_dict.items():
                monkeys[i].catch(items)

    return product(sorted([monkey.num_inspections for monkey in monkeys])[-2:])


def part_b(input_string=TEST_INPUT):
    monkeys = parse_input(input_string)
    least_common_multiple = math.lcm(*[monkey.divisible_by for monkey in monkeys])
    for _ in range(10_000):
        for monkey in monkeys:
            throw_dict = monkey.inspect(relief_factor=least_common_multiple)
            for i, items in throw_dict.items():
                monkeys[i].catch(items)

    return product(sorted([monkey.num_inspections for monkey in monkeys])[-2:])
