from y2021.d17.trick_shot import solve_a, solve_b

TEST_INPUT = "target area: x=20..30, y=-10..-5"

PART_ONE_TEST_OUTPUT = 45
PART_TWO_TEST_OUTPUT = 112


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
