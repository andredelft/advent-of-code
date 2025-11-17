import pytest
from y2019.d14.space_stoichiometry import solve_a, solve_b


TEST_INPUT = """\
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

LARGE_TEST_INPUT = """\
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""


@pytest.fixture
def test_input():
    return TEST_INPUT


@pytest.fixture
def large_test_input():
    return LARGE_TEST_INPUT


@pytest.fixture
def expected_solution_a():
    return 31


@pytest.fixture
def expected_large_solution_a():
    return 13312


@pytest.fixture
def expected_solution_b():
    return 82892753


def test_solve_a(test_input, expected_solution_a):
    assert solve_a(test_input) == expected_solution_a


def test_solve_large_a(large_test_input, expected_large_solution_a):
    assert solve_a(large_test_input) == expected_large_solution_a


def test_solve_b(large_test_input, expected_solution_b):
    assert solve_b(large_test_input) == expected_solution_b
