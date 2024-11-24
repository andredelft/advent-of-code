def parse_input(input_string: str):
    for n in input_string.split("\n"):
        yield int(n)


def get_fuel(mass, recursive=False):
    fuel = (mass // 3) - 2

    if fuel <= 0:
        return 0

    if recursive:
        fuel += get_fuel(fuel, recursive)

    return fuel


def solve_a(input_string):
    return sum(get_fuel(mass) for mass in parse_input(input_string))


def solve_b(input_string):
    return sum(get_fuel(mass, recursive=True) for mass in parse_input(input_string))
