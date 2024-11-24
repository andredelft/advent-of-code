import pytest
from y2019.d03.crossed_wires import part_a, part_b


TEST_INPUT = """\
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 159


@pytest.fixture
def expected_solution_b():
    return 610


def test_part_a(test_input, expected_solution_a):
    assert part_a(test_input) == expected_solution_a


def test_part_b(test_input, expected_solution_b):
    assert part_b(test_input) == expected_solution_b
