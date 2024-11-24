from passage_pathing import solve_a, solve_b

TEST_INPUT = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

PART_ONE_TEST_OUTPUT = 10
PART_TWO_TEST_OUTPUT = 36


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    # test_a()
    test_b()
