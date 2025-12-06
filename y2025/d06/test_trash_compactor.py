import pytest
from y2025.d06.trash_compactor import solve_a, solve_b


TEST_INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 4277556


@pytest.fixture
def expected_solution_b():
    return 3263827


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
