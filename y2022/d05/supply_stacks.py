from lib.regex import parse_numbers
from lib.array import split_list

TEST_INPUT = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

Crates = list[list[str]]


def parse_crates(line: str, crates: Crates) -> Crates:
    for i in range(1, len(line), 4):
        char = line[i]
        if char != " ":
            crates[i // 4].append(char)


def parse_input(input_string):
    crates_str, moves_str = input_string.split("\n\n")
    *crates_str, stacks_str = crates_str.split("\n")

    # Each row is 3 chars long, with 1 char as gap, so we can divide by 4 and round up
    num_stacks = len(stacks_str) // 4 + 1

    crates: Crates = [[] for _ in range(num_stacks)]
    for line in reversed(crates_str):
        parse_crates(line, crates)

    moves = [parse_numbers(move) for move in moves_str.split("\n")]

    return crates, moves


def print_crates(crates: Crates):
    max_stack_height = max(len(crate) for crate in crates)

    for i in reversed(range(max_stack_height)):
        row: list[str | None] = []
        for stack in crates:
            if len(stack) < i + 1:
                row.append(None)
            else:
                row.append(stack[i])
        print(" ".join([f"[{crate}]" if crate else "   " for crate in row]))


def part_a(input_string=TEST_INPUT):
    crates, moves = parse_input(input_string)

    for num_crates, stack_from, stack_to in moves:
        for _ in range(num_crates):
            crate = crates[stack_from - 1].pop()
            crates[stack_to - 1].append(crate)

    print_crates(crates)

    return "".join(stack[-1] for stack in crates)


def part_b(input_string=TEST_INPUT):
    crates, moves = parse_input(input_string)

    for num_crates, stack_from, stack_to in moves:
        crates[stack_from - 1], moving_crates = split_list(
            crates[stack_from - 1], -1 * num_crates
        )
        crates[stack_to - 1].extend(moving_crates)

    print_crates(crates)

    return "".join(stack[-1] for stack in crates)
