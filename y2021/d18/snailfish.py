from pathlib import Path
from snailfish_numbers import SnailfishNumber
from itertools import permutations
from tqdm import tqdm
from math import factorial


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    return [SnailfishNumber(eval(line)) for line in input_string.split("\n") if line]


def sum_objs(obj_list):
    obj_sum = obj_list[0]
    for obj in obj_list[1:]:
        obj_sum += obj
    return obj_sum


def solve_a(input_string=INPUT_STRING):
    snailfishes = parse_input(input_string)
    snailfish_sum = sum_objs(snailfishes)
    print("Snailfish sum:", snailfish_sum)
    print("Quantity:", len(snailfish_sum))
    return len(snailfish_sum)


def solve_b(input_string=INPUT_STRING):
    snailfishes = parse_input(input_string)
    max_quantity = 0
    for snailfish_permuation in tqdm(
        permutations(snailfishes, 2), total=len(snailfishes) * (len(snailfishes) - 1)
    ):
        quantity = len(sum_objs(snailfish_permuation))
        max_quantity = max(max_quantity, quantity)
    print("Max quantity:", max_quantity)
    return max_quantity


if __name__ == "__main__":
    solve_a()
    solve_b()
