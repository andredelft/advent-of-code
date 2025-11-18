import pytest
from y2020.d05.binary_boarding import solve_a, solve_b


TEST_INPUT = """\
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 820


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a
