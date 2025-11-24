import pytest
from y2020.d06.custom_customs import solve_a, solve_b


TEST_INPUT = """\
abc

a
b
c

ab
ac

a
a
a
a

b"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 11


@pytest.fixture
def expected_solution_b():
    return 6


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
