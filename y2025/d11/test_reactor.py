import pytest
from y2025.d11.reactor import solve_a, solve_b


TEST_INPUT_A = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

TEST_INPUT_B = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


@pytest.fixture
def test_input_a():
    return TEST_INPUT_A


@pytest.fixture
def test_input_b():
    return TEST_INPUT_B


@pytest.fixture
def expected_solution_a():
    return 5


@pytest.fixture
def expected_solution_b():
    return 2


def test_solve_a(test_input_a, expected_solution_a):
    assert solve_a(test_input_a) == expected_solution_a


def test_solve_b(test_input_b, expected_solution_b):
    assert solve_b(test_input_b) == expected_solution_b
