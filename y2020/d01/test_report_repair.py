import pytest
from y2020.d01.report_repair import solve_a, solve_b


TEST_INPUT = """\
1721
979
366
299
675
1456"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 514579


@pytest.fixture
def expected_solution_b():
    return 241861950


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
