import re
from collections import Counter
from lib.numbers import ceildiv

RE_chemical = re.compile(r"^(\d+) ([A-Z]+)$")


chemical = tuple[int, str]


def parse_chemical(value: str) -> chemical:
    quantity, name = RE_chemical.search(value).groups()

    return (int(quantity), name)


def parse_input(input_string: str):
    equations: dict[str, tuple[int, list[chemical]]] = dict()

    for line in input_string.split("\n"):
        equation_in, equation_out = line.split(" => ")

        chemical_out = parse_chemical(equation_out)
        chemicals_in = [parse_chemical(v) for v in equation_in.split(", ")]

        equations[chemical_out[1]] = (chemical_out[0], chemicals_in)

    return equations


def solve_a(input_string: str, num_fuel=1):
    equations = parse_input(input_string)

    rank: dict[str, int] = {"ORE": 0}
    current_rank = 0

    while len(rank) <= len(equations):
        new_rank = rank.copy()
        current_rank += 1

        for name_out, (_, chemicals_in) in equations.items():
            if name_out in rank:
                continue

            if all((chemical[1] in rank) for chemical in chemicals_in):
                new_rank[name_out] = current_rank

        rank = new_rank

    chemicals = Counter({"FUEL": num_fuel})

    while current_rank > 0:
        new_chemicals = Counter()

        for name, n in chemicals.items():
            if rank[name] != current_rank:
                new_chemicals[name] += n
                continue

            num_out, chemicals_in = equations[name]

            num_reactions = ceildiv(n, num_out)
            remainder = num_out * num_reactions - n

            for n_in, name_in in chemicals_in:
                new_chemicals[name_in] += n_in * num_reactions

            new_chemicals[name] += remainder

        chemicals = new_chemicals
        current_rank -= 1

    return chemicals["ORE"]


def solve_b(input_string: str):
    ore_per_fuel = solve_a(input_string)
    cargo_hold = 1_000_000_000_000

    # Binary search
    lower_bound = cargo_hold // ore_per_fuel
    # lower_bound is too low because of residual chemicals, probably 1-10%
    upper_bound = lower_bound * 2

    while lower_bound < upper_bound - 1:
        fuel_estimate = (lower_bound + upper_bound) // 2
        min_num_ore = solve_a(input_string, fuel_estimate)

        if min_num_ore > cargo_hold:
            upper_bound = fuel_estimate
        elif min_num_ore < cargo_hold:
            lower_bound = fuel_estimate
        else:
            raise ValueError

    return lower_bound
