import pytest
from y2020.d08.handheld_halting import solve_a, solve_b


TEST_INPUT = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


@pytest.fixture
def test_input():
    return 5


@pytest.fixture
def expected_solution_a():
    return None


@pytest.fixture
def expected_solution_b():
    return None


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
