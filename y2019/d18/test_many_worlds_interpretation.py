import pytest
from y2019.d18.many_worlds_interpretation import solve_a, solve_b


TEST_INPUT = """\
#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 26


# @pytest.fixture
# def expected_solution_b():
#     return 8


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input, visualize=False) == expected_solution_a


# def test_solve_b(test_input, expected_solution_b):
#     assert solve_b(test_input, visualize=False) == expected_solution_b
