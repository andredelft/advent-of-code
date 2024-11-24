from pathlib import Path
import re
from collections import Counter


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input):
    return Counter(int(n) for n in re.findall("\d+", input))


def linear_fuel(crab_positions, destination):
    fuel = 0
    for crab_position, num_crabs in crab_positions.items():
        fuel += num_crabs * abs(crab_position - destination)
    return fuel


def cumulative_fuel(crab_positions, destination):
    fuel = 0
    for crab_position, num_crabs in crab_positions.items():
        num_steps = abs(crab_position - destination)
        # We use Gauss' relation: 1 + 2 + 3 + ... + n = n(n + 1)/2
        fuel += int(num_crabs * num_steps * (num_steps + 1) / 2)
    return fuel


def solve_a(input_string=INPUT_STRING, fuel_function=linear_fuel):
    crab_positions = parse_input(input_string)
    max_position = max(crab_positions.keys())
    min_position = min(crab_positions.keys())

    min_fuel_required = fuel_function(crab_positions, min_position)
    min_destination = min_position
    for position in range(min_position + 1, max_position + 1):
        fuel_required = fuel_function(crab_positions, position)
        if fuel_required < min_fuel_required:
            min_fuel_required = fuel_required
            min_destination = position

    print(
        f"Destination {min_destination} requires the least amount of fuel ({min_fuel_required} units) with function"
    )

    return min_fuel_required


def solve_b(input_string=INPUT_STRING):
    return solve_a(input_string, fuel_function=cumulative_fuel)


if __name__ == "__main__":
    solve_a()
    solve_b()
