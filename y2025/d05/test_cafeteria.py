import pytest
from y2025.d05.cafeteria import solve_a, solve_b


TEST_INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 3


@pytest.fixture
def expected_solution_b():
    return 14


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
