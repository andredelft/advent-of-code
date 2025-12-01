import pytest
from y2025.d01.secret_entrance import solve_a, solve_b


TEST_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 3


@pytest.fixture
def expected_solution_b():
    return 6


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
