def parse_input(input_string: str):
    for line in input_string.split("\n"):
        command, value = line.split(" ")
        yield command, int(value)


def run_program(program: list[tuple[str, int]], exclude=set()):
    accumulator = 0
    pointer = 0
    instructions_ran = exclude.copy()

    while True:
        if pointer in instructions_ran:
            return 0, accumulator, instructions_ran

        command, value = program[pointer]
        instructions_ran.add(pointer)

        match command:
            case "nop":
                pointer += 1
            case "acc":
                accumulator += value
                pointer += 1
            case "jmp":
                pointer += value
            case _:
                raise ValueError(f"{command} does not exist")

        if pointer == len(program):
            return 1, accumulator, instructions_ran

        pointer %= len(program)


def solve_a(input_string: str):
    program = list(parse_input(input_string))

    return run_program(program)[1]


def solve_b(input_string: str):
    program = list(parse_input(input_string))

    *_, instructions_ran = run_program(program)

    for j in instructions_ran:
        command, value = program[j]

        if command == "acc":
            continue

        new_program = program.copy()

        new_program[j] = ("nop" if command == "jmp" else "jmp", value)

        exit_code, accumulator, _ = run_program(new_program)

        if exit_code == 1:
            return accumulator
