import pytest
from y2019.intcode import Intcode


# Day 5, part a


@pytest.fixture()
def identity_program():
    """Outputs whatever it gets as input, then halts."""
    return Intcode([3, 0, 4, 0, 99])


program_inputs = [0, 1, 5, 10, 13, -25, 320]


@pytest.mark.parametrize("program_input", program_inputs)
def test_identity(identity_program, program_input):
    assert identity_program.run(program_input) == program_input


@pytest.fixture()
def multiply_program():
    return Intcode([1002, 4, 3, 4, 33])


def test_multiply_program(multiply_program):
    multiply_program.run()
    assert multiply_program.memory[4] == 99


# Day 5, part b

small_eight_comparison_programs = [
    # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 1),
    # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 0),
    # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], 1),
    # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], 0),
]


@pytest.mark.parametrize("program,expected_response", small_eight_comparison_programs)
def test_small_eight_comparison_programs(program, expected_response):
    intcode = Intcode(program)

    assert intcode.run(8, reset=True) == expected_response
    assert intcode.run(4) == 1 - expected_response


# Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
jump_tests = [
    [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],  # Position mode
    [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],  # Immediate mode
]


@pytest.mark.parametrize("program", jump_tests)
def test_jump_tests(program):
    intcode = Intcode(program)

    assert intcode.run(0, reset=True) == 0
    assert intcode.run(1, reset=True) == 1
    assert intcode.run(5) == 1


@pytest.fixture()
def compare_with_eight_program():
    """The program will then output 999 if the input value is below 8,
    output 1000 if the input value is equal to 8, or output 1001 if
    the input value is greater than 8."""

    return Intcode.parse_input(
        """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
    )


def test_compare_with_eight_program(compare_with_eight_program):
    intcode = compare_with_eight_program

    assert intcode.run(0, reset=True) == 999
    assert intcode.run(8, reset=True) == 1000
    assert intcode.run(23, reset=True) == 1001
    assert intcode.run(-5, reset=True) == 999


# Day 9
@pytest.fixture()
def quine_program():
    """Produces a copy of itself as output"""
    return [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]


def test_quine_program(quine_program):
    intcode = Intcode(quine_program, output_as_array=True)

    assert intcode.run() == quine_program


@pytest.fixture()
def sixteen_digit_program():
    """Should output a 16-digit number"""
    return [1102, 34915192, 34915192, 7, 4, 7, 99, 0]


def test_sixteen_digit_program(sixteen_digit_program):
    intcode = Intcode(sixteen_digit_program)

    assert intcode.run() == 1219070632396864


@pytest.fixture()
def large_number_program():
    """Should output the large number in the middle"""
    return [104, 1125899906842624, 99]


def test_large_number_program(large_number_program):
    intcode = Intcode(large_number_program)

    assert intcode.run() == large_number_program[1]
