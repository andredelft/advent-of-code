from pathlib import Path
import re
from collections import Counter

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    polymer, instructions_str = input_string.split("\n\n")
    instructions = {
        m[0]: m[1] for m in re.findall(r"([A-Za-z]{2}) -> ([A-Za-z])", instructions_str)
    }
    return polymer, instructions


def solve_a(input_string=INPUT_STRING, n=10):
    polymer, instructions = parse_input(input_string)

    for _ in range(n):
        new_polymer = polymer[0]
        for i in range(1, len(polymer)):
            new_polymer += instructions[polymer[i - 1 : i + 1]]
            new_polymer += polymer[i]
        polymer = new_polymer

    element_counter = Counter(polymer).most_common()

    print(element_counter[0][1] - element_counter[-1][1])
    return element_counter[0][1] - element_counter[-1][1]


def solve_b(input_string=INPUT_STRING):
    polymer, instructions = parse_input(input_string)
    last_element = polymer[-1]

    sequences = Counter(polymer[i - 1 : i + 1] for i in range(1, len(polymer)))
    for _ in range(40):
        new_sequences = Counter()
        for sequence, n in sequences.items():
            new_element = instructions[sequence]
            new_sequences.update(
                {
                    sequence[0] + new_element: n,
                    new_element + sequence[1]: n,
                }
            )
        sequences = new_sequences

    # To obtain the number of elements, we use the fact that each element is counted twice
    # in the sequence dict, except the first and the last element. We can overcome this by
    # only counting the first element of each sequence and adding the last element, which
    # we recorded in the beginning
    element_counter = Counter()
    for sequence, n in sequences.items():
        element_counter.update({sequence[0]: n})

    element_counter.update({last_element: 1})

    element_counter = element_counter.most_common()
    print(element_counter[0][1] - element_counter[-1][1])
    return element_counter[0][1] - element_counter[-1][1]


if __name__ == "__main__":
    solve_a()
    solve_b()
