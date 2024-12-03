import re


RE_MUL = r"mul\((\d+),(\d+)\)"
RE_MUL_DO_DONT = rf"{RE_MUL}|do\(\)|don't\(\)"


def parse_input(input_string: str, include_do_dont=False):
    matches = re.finditer(RE_MUL_DO_DONT if include_do_dont else RE_MUL, input_string)

    do = True

    for m in matches:
        match m.group(0):
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if do:
                    yield (int(m.group(1)), int(m.group(2)))


def solve_a(input_string: str, include_do_dont=False):
    number_pairs = parse_input(input_string, include_do_dont)

    return sum(number[0] * number[1] for number in number_pairs)


def solve_b(input_string: str):
    return solve_a(input_string, include_do_dont=True)
