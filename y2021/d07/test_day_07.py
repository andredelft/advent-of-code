from whale_treachery import solve_a, solve_b

TEST_INPUT = "16,1,2,0,4,2,7,1,2,14"

PART_ONE_TEST_OUTPUT = 37
PART_TWO_TEST_OUTPUT = 168


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
