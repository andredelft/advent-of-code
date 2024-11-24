from y2023.d16.lava_floor import part_a, part_b

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
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_B
