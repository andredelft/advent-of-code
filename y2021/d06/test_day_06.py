from lanternfish import solve_a, solve_b

TEST_INPUT = "3,4,3,1,2"

PART_ONE_TEST_OUTPUT = 5934
PART_TWO_TEST_OUTPUT = 26984457539


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
