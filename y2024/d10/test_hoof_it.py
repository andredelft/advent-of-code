import pytest
from y2024.d10.hoof_it import solve_a, solve_b


TEST_INPUT = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 36


@pytest.fixture
def expected_solution_b():
    return 81


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
