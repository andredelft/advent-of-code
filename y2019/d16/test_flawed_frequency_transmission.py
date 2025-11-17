import pytest
from y2019.d16.flawed_frequency_transmission import solve_a, solve_b


TEST_INPUT = """\
80871224585914546619083218645595"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 24176176


@pytest.fixture
def expected_solution_b():
    return None


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
