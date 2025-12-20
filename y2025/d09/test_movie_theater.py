import pytest
from y2025.d09.movie_theater import solve_a, solve_b


TEST_INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 50


@pytest.fixture
def expected_solution_b():
    return None


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
