from functools import cache


def parse_input(input_string: str):
    connections: dict[str, list[str]] = dict()

    for line in input_string.split("\n"):
        device, *outputs = line.split(" ")

        connections[device[:-1]] = outputs

    return connections


def solve_a(input_string: str):
    connections = parse_input(input_string)

    @cache
    def num_ways_out(device: str):
        if device == "out":
            return 1

        return sum(num_ways_out(d) for d in connections[device])

    return num_ways_out("you")


def solve_b(input_string: str):
    connections = parse_input(input_string)

    @cache
    def num_ways_out(device: str, has_fft=False, has_dac=False):
        match device:
            case "out":
                return 1 if (has_fft and has_dac) else 0
            case "fft":
                has_fft = True
            case "dac":
                has_dac = True

        return sum(num_ways_out(d, has_fft, has_dac) for d in connections[device])

    return num_ways_out("svr")
