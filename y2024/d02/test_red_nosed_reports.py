import pytest
from y2024.d02.red_nosed_reports import solve_a, solve_b


TEST_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 2


@pytest.fixture
def expected_solution_b():
    return 4


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
