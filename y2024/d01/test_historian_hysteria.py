import pytest
from y2024.d01.historian_hysteria import solve_a, solve_b


TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 11


@pytest.fixture
def expected_solution_b():
    return 31


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
