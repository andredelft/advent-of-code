import pytest
from $module import part_a, part_b


TEST_INPUT = """\\
"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return None


@pytest.fixture
def expected_solution_b():
    return None


def test_part_a(test_input, expected_solution_a):
    assert part_a(test_input) == expected_solution_a


def test_part_b(test_input, expected_solution_b):
    assert part_b(test_input) == expected_solution_b
