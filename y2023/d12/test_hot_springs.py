from y2023.d12.hot_springs import solve_a, solve_b

TEST_INPUT = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

EXPECTED_SOLUTION_A = 21
EXPECTED_SOLUTION_B = 525152


def test_a():
    assert solve_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT) == EXPECTED_SOLUTION_B
