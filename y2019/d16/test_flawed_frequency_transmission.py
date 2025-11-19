import pytest
from y2019.d16.flawed_frequency_transmission import solve_a


TEST_INPUT = "80871224585914546619083218645595"


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution():
    return 24176176


def test_solve_a(test_input, expected_solution):
    assert solve_a(test_input) == expected_solution
