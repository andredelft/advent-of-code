from y2019.intcode import Intcode

from more_itertools import powerset
from tqdm import tqdm

COLLECT_ITEMS = """\
south
west
north
take fuel cell
south
east
north
north
east
take candy cane
south
take hypercube
north
west
north
take coin
east
take tambourine
west
west
take spool of cat6
north
take weather machine
west
take mutex
west
"""

ITEMS = [
    "fuel cell",
    "candy cane",
    "hypercube",
    "coin",
    "tambourine",
    "spool of cat6",
    "weather machine",
    "mutex",
]


def solve_a(input_string: str):
    intcode = Intcode.parse_input(
        input_string, input_as_ascii=True, output_as_ascii=True, pause_on_input=True
    )
    print("Collecting items")
    intcode.run(COLLECT_ITEMS)

    for item in ITEMS:
        intcode.run(f"drop {item}\n")

    for items in tqdm(powerset(ITEMS), total=2 ** len(ITEMS), desc="Trying items"):
        for item in items:
            intcode.run(f"take {item}\n")

        response = intcode.run("west\n")

        if not "Alert" in response:
            print("Passed with:", ", ".join(items))
            print(response)
            break

        for item in items:
            intcode.run(f"drop {item}\n")

    while not intcode.has_terminated:
        command = input() + "\n"
        print(intcode.run(command))


def solve_b(input_string: str):
    intcode = Intcode.parse_input(input_string)
