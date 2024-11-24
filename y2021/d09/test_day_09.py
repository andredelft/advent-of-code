from smoke_basin import solve_a, solve_b

TEST_INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678"""

PART_ONE_TEST_OUTPUT = 15
PART_TWO_TEST_OUTPUT = 1134


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
