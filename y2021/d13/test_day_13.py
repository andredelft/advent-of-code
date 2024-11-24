from transparent_origami import solve_a, solve_b

TEST_INPUT = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

PART_ONE_TEST_OUTPUT = 17
PART_TWO_TEST_OUTPUT = None


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
