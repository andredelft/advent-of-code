import pytest
from y2024.d07.bridge_repair import solve_a, solve_b


TEST_INPUT = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 3749


@pytest.fixture
def expected_solution_b():
    return 11387


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
