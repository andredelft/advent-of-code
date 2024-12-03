import pytest
from y2024.d03.mull_it_over import solve_a, solve_b


@pytest.fixture
def test_input_a():
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


@pytest.fixture
def test_input_b():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


@pytest.fixture
def expected_solution_a():
    return 161


@pytest.fixture
def expected_solution_b():
    return 48


def test_solve_a(test_input_a, expected_solution_a):
    assert solve_a(test_input_a) == expected_solution_a


def test_solve_b(test_input_b, expected_solution_b):
    assert solve_b(test_input_b) == expected_solution_b
