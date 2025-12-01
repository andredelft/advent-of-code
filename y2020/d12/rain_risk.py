from lib.geometry import Coordinate

NORTH = Coordinate(-1, 0)
EAST = Coordinate(0, 1)
SOUTH = Coordinate(1, 0)
WEST = Coordinate(0, -1)


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        yield line[0], int(line[1:])


def solve_a(input_string: str):
    instructions = parse_input(input_string)
    coord = Coordinate(0, 0)
    direction = Coordinate(0, 1)

    for action, value in instructions:
        match action:
            case "N":
                coord += value * NORTH
            case "S":
                coord += value * SOUTH
            case "E":
                coord += value * EAST
            case "W":
                coord += value * WEST
            case "L":
                direction = direction.rotate(-1 * value // 90)
            case "R":
                direction = direction.rotate(value // 90)
            case "F":
                coord += value * direction

    return len(coord)


def solve_b(input_string: str):
    instructions = parse_input(input_string)
    coord = Coordinate(0, 0)
    waypoint = Coordinate(-1, 10)

    for action, value in instructions:
        match action:
            case "N":
                waypoint += value * NORTH
            case "S":
                waypoint += value * SOUTH
            case "E":
                waypoint += value * EAST
            case "W":
                waypoint += value * WEST
            case "L":
                waypoint = waypoint.rotate(-1 * value // 90)
            case "R":
                waypoint = waypoint.rotate(value // 90)
            case "F":
                coord += value * waypoint

    return len(coord)
