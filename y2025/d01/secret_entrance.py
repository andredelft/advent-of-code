def parse_input(input_string: str):
    for line in input_string.split("\n"):
        yield line[0], int(line[1:])


def solve_a(input_string: str):
    dial_position = 50
    num_zeroes = 0

    for direction, value in parse_input(input_string):
        dial_position += (-1 if direction == "L" else 1) * value
        dial_position %= 100
        if dial_position == 0:
            num_zeroes += 1

    return num_zeroes


def solve_b(input_string: str):
    dial_position = 50
    num_zeroes = 0

    for direction, value in parse_input(input_string):
        for _ in range(value):
            dial_position += 1 if direction == "R" else -1

            match dial_position:
                case 0:
                    num_zeroes += 1
                case -1:
                    dial_position = 99
                case 100:
                    num_zeroes += 1
                    dial_position = 0

    return num_zeroes
