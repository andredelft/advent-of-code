import pytest
from y2024.d09.disk_fragmenter import solve_a, solve_b


TEST_INPUT = """\
2333133121414131402"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 1928


@pytest.fixture
def expected_solution_b():
    return 2858


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
