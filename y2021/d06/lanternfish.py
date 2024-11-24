import re
from pathlib import Path
from collections import Counter

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT = f.read()


def parse_input(input_string):
    return Counter(int(n) for n in re.findall("\d+", input_string))


def perform_day(lanternfish: Counter):
    new_lanternfish = Counter()
    for age, num_lanternfish in lanternfish.items():
        if age > 0:
            new_lanternfish[age - 1] = num_lanternfish

    new_lanternfish[6] = new_lanternfish.get(6, 0) + lanternfish.get(0, 0)
    new_lanternfish[8] = lanternfish.get(0, 0)

    return new_lanternfish


def solve_a(input_string=INPUT, num_days=80):
    lanternfish = parse_input(input_string)
    for n in range(num_days):
        print(f"Calculating day {n + 1}")
        print(lanternfish)
        lanternfish = perform_day(lanternfish)

    num_counters = sum(lanternfish.values())
    print(f"There are {num_counters} lanternfish after {num_days} days")
    return num_counters


def solve_b(input_string=INPUT, num_days=256):
    return solve_a(input_string, num_days)  # This takes a LONG time


if __name__ == "__main__":
    solve_a()
    solve_b()
