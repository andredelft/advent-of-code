from y2023.d01.trebuchet import solve_a, solve_b

TEST_INPUT_A = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_INPUT_B = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

EXPECTED_SOLUTION_A = 142
EXPECTED_SOLUTION_B = 281


def test_a():
    assert solve_a(TEST_INPUT_A) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT_B) == EXPECTED_SOLUTION_B
