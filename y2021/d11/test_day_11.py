from y2021.d11.dumbo_octopus import solve_a, solve_b

TEST_INPUT = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

PART_ONE_TEST_OUTPUT = 1656
PART_TWO_TEST_OUTPUT = 195


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
