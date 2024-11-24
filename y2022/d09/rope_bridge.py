from y2022.d09.rope import Rope

TEST_INPUT_A = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

TEST_INPUT_B = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


PRINT_STEPS = False  # Set to True for animation in terminal


def parse_input(input_string: str):

    for line in input_string.split("\n"):
        direction, num_moves = line.split(" ")
        yield direction, int(num_moves)


def part_a(input_string=TEST_INPUT_A):
    rope = Rope(2)
    moves = parse_input(input_string)

    for move in moves:
        rope.move_n(*move, print_steps=PRINT_STEPS)

    rope.print_visited()
    return len(rope.tail_history)


def part_b(input_string=TEST_INPUT_B):
    rope = Rope(10)
    moves = parse_input(input_string)

    for move in moves:
        rope.move_n(*move, print_steps=PRINT_STEPS)

    rope.print_visited()
    return len(rope.tail_history)
