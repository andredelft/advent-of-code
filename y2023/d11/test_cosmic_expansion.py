from y2023.d11.cosmic_expansion import part_a, part_b

TEST_INPUT = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

EXPECTED_SOLUTION_A = 374
EXPECTED_SOLUTION_B = 8410


def test_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT, expansion_coefficient=100) == EXPECTED_SOLUTION_B
