import pytest
from y2019.d06.universal_orbit_map import solve_a, solve_b


TEST_INPUT_A = """\
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


@pytest.fixture
def test_input_a():
    return TEST_INPUT_A


TEST_INPUT_B = """\
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


@pytest.fixture
def test_input_b():
    return TEST_INPUT_B


@pytest.fixture
def expected_solution_a():
    return 42


@pytest.fixture
def expected_solution_b():
    return 4


def test_solve_a(test_input_a, expected_solution_a):
    assert solve_a(test_input_a) == expected_solution_a


def test_solve_b(test_input_b, expected_solution_b):
    assert solve_b(test_input_b) == expected_solution_b
