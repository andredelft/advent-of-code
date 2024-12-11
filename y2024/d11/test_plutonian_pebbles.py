import pytest
from y2024.d11.plutonian_pebbles import solve_a, solve_b


TEST_INPUT = """125 17"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 55312


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a
