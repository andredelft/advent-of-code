from itertools import product
from y2019.intcode import Intcode
from lib.regex import parse_numbers


def parse_input(input_string: str):
    return parse_numbers(input_string)


def solve_a(input_string, restore_1202=True):
    program = parse_input(input_string)

    if restore_1202:
        program[1] = 12
        program[2] = 2

    intcode = Intcode(program)
    intcode.run()
    return intcode.program[0]


def solve_b(input_string, desired_output=19690720):
    program = parse_input(input_string)

    for noun, verb in product(range(len(program)), repeat=2):
        memory = program.copy()

        memory[1] = noun
        memory[2] = verb

        intcode = Intcode(memory)
        intcode.run()
        if intcode.program[0] == desired_output:
            return 100 * noun + verb
