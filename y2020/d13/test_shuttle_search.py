import pytest
from y2020.d13.shuttle_search import solve_a, solve_b


TEST_INPUT = """\
939
7,13,x,x,59,x,31,19"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 295


@pytest.fixture
def expected_solution_b():
    return 1068781


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
