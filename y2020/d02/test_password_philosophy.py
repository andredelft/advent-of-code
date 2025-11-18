import pytest
from y2020.d02.password_philosophy import solve_a, solve_b


TEST_INPUT = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 2


@pytest.fixture
def expected_solution_b():
    return 1


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
