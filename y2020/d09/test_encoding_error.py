import pytest
from y2020.d09.encoding_error import solve_a, solve_b


TEST_INPUT = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 127


@pytest.fixture
def expected_solution_b():
    return 62


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input, 5) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input, 5) == expected_solution_b
