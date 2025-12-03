import pytest
from y2025.d03.lobby import solve_a, solve_b


TEST_INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 357


@pytest.fixture
def expected_solution_b():
    return 3121910778619


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
