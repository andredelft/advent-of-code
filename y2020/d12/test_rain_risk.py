import pytest
from y2020.d12.rain_risk import solve_a, solve_b


TEST_INPUT = """\
F10
N3
F7
R90
F11"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 25


@pytest.fixture
def expected_solution_b():
    return 286


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
