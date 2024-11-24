from y2023.d16.lava_floor import solve_a, solve_b

TEST_INPUT = """\
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

EXPECTED_SOLUTION_A = 46
EXPECTED_SOLUTION_B = 51


def test_a():
    assert solve_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT) == EXPECTED_SOLUTION_B
