import pytest
from y2019.d12.n_body_problem import solve_a, solve_b


TEST_INPUT = """\
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def num_steps():
    return 100


@pytest.fixture
def expected_solution_a():
    return 1940


@pytest.fixture
def expected_solution_b():
    return None


def test_solve_a(test_input, num_steps, expected_solution_a):
    assert solve_a(test_input, num_steps) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
