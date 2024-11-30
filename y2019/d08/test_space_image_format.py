import pytest
from y2019.d08.space_image_format import solve_a, solve_b


@pytest.fixture
def test_input_a():
    return "123456789012"


@pytest.fixture
def sizes_a():
    return (2, 3)


@pytest.fixture
def expected_solution_a():
    return 1


@pytest.fixture
def test_input_b():
    return "0222112222120000"


@pytest.fixture
def sizes_b():
    return (2, 2)


@pytest.fixture
def expected_solution_b():
    return " X\nX "


def test_solve_a(test_input_a, sizes_a, expected_solution_a):
    assert solve_a(test_input_a, sizes_a) == expected_solution_a


def test_solve_b(test_input_b, sizes_b, expected_solution_b):
    assert solve_b(test_input_b, sizes_b) == expected_solution_b
