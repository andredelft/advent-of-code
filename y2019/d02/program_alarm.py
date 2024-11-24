from collections import Counter
from itertools import product


def parse_input(input_string: str):
    program = [int(n) for n in input_string.split(",")]

    return program


def intcode(program: list[int]):
    pointer = 0

    while True:
        match program[pointer]:
            case 1 | 2 as opcode:
                # Parameters
                p_1, p_2, p_3 = program[pointer + 1 : pointer + 4]

                n_1 = program[p_1]
                n_2 = program[p_2]

                program[p_3] = n_1 + n_2 if opcode == 1 else n_1 * n_2
                pointer += 4
            case 99:
                break
            case _ as opcode:
                raise ValueError(f"Unknown opcode: {opcode}")

    return program[0]


def part_a(input_string, restore_1202=True):
    program = parse_input(input_string)

    if restore_1202:
        program[1] = 12
        program[2] = 2

    return intcode(program)


def part_b(input_string, desired_output=19690720):
    program = parse_input(input_string)

    for noun, verb in product(range(len(program)), repeat=2):
        memory = program.copy()

        memory[1] = noun
        memory[2] = verb

        if intcode(memory) == desired_output:
            return 100 * noun + verb
