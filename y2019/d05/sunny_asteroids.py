from y2019.intcode import Intcode


def solve_a(input_string):
    intcode = Intcode.parse_input(input_string)

    return intcode.run(1)


def solve_b(input_string):
    intcode = Intcode.parse_input(input_string)

    return intcode.run(5)
