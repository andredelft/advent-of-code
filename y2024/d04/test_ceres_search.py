import pytest
from y2024.d04.ceres_search import solve_a, solve_b


TEST_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 18


@pytest.fixture
def expected_solution_b():
    return 9


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_b(test_input, expected_solution_b):
    assert solve_b(test_input) == expected_solution_b
