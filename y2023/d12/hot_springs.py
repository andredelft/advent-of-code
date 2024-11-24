import re
from tqdm import tqdm
from functools import cache

from lib.regex import parse_numbers


def parse_input(input_string: str) -> tuple[str, tuple[int]]:
    lines = input_string.split("\n")
    records = []

    for line in lines:
        lines, hash_lengths = line.split(" ")

        records.append((lines, tuple(parse_numbers(hash_lengths))))
    return records


def parse_folded_input(input_string: str) -> tuple[str, tuple[int]]:
    records = parse_input(input_string)
    records_folded_out = []

    for line, hash_lengths in records:
        line_folded_out = "?".join(line for _ in range(5))
        hash_lengths_folded_out = 5 * hash_lengths
        records_folded_out.append((line_folded_out, hash_lengths_folded_out))

    return records_folded_out


@cache
def solve_line(line: str, hash_lengths: tuple[int], num_hashes: int, num_dots: int):
    if not line:
        solved = not hash_lengths and not num_hashes and not num_dots
        return int(solved)

    first_char = line[0]

    match first_char:
        case ".":
            return solve_line(line[1:], hash_lengths, num_hashes, num_dots)
        case "#":
            if not hash_lengths:
                return 0

            current_hash_length = hash_lengths[0]

            new_line, matches = re.subn(
                rf"^[\#\?]{{{current_hash_length}}}(?:[\.\?]|$)", "", line, 1
            )

            if not matches:
                return 0

            num_hashes -= line[:current_hash_length].count("?")

            if len(line) > current_hash_length and line[current_hash_length] == "?":
                num_dots -= 1

            if num_hashes < 0 or num_dots < 0:
                return 0

            return solve_line(new_line, hash_lengths[1:], num_hashes, num_dots)
        case "?":
            num_sols = 0
            if num_dots:
                num_sols += solve_line(
                    "." + line[1:], hash_lengths, num_hashes, num_dots - 1
                )

            if num_hashes:
                num_sols += solve_line(
                    "#" + line[1:], hash_lengths, num_hashes - 1, num_dots
                )

            return num_sols


def get_num_solutions(records):
    num_solutions = []

    for line, hash_lengths in tqdm(records):
        num_unknowns = line.count("?")
        num_known_hash = line.count("#")

        num_unknown_hash = sum(hash_lengths) - num_known_hash
        num_unknown_dot = num_unknowns - num_unknown_hash

        num_solutions.append(
            solve_line(line, hash_lengths, num_unknown_hash, num_unknown_dot)
        )

    return num_solutions


def solve_a(input_string: str):
    records = parse_input(input_string)

    return sum(get_num_solutions(records))


def solve_b(input_string: str):
    records = parse_folded_input(input_string)

    return sum(get_num_solutions(records))
