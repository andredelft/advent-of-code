import re
from collections import Counter
from lib.numbers import ceildiv

from tqdm import tqdm


def parse_input(input_string: str):
    reactions = dict()
    for line in input_string.split("\n"):
        substances = [
            (int(m.group(1)), m.group(2)) for m in re.finditer(r"(\d+) ([A-Z]+)", line)
        ]

        reactions[substances[-1][1]] = (substances[-1][0], substances[:-1])

    return reactions


def solve_a(input_string: str):
    reactions = parse_input(input_string)

    chemicals = Counter(["FUEL"])

    while list(chemicals) != ["ORE"]:
        new_chemicals = Counter()

        for chemical, count in chemicals.items():
            if chemical == "ORE":
                new_chemicals[chemical] = count
                continue

            num_produced, elements = reactions[chemical]

            num_reactions = count // num_produced
            leftover = count % num_produced

            if num_reactions > 0:
                new_chemicals.update(
                    {element: n * num_reactions for n, element in elements}
                )

            if leftover:
                new_chemicals[chemical] += leftover

        # print(new_chemicals)
        # input()

        if chemicals == new_chemicals:
            break

        chemicals = new_chemicals

    return chemicals


def solve_b(input_string: str):
    parse_input(input_string)
