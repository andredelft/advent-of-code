from itertools import count, pairwise
from math import asin, pi
from tqdm import tqdm

from lib.field import Field


PIPE_TRANS = str.maketrans("-|F7LJ", "─│┌┐└┘")

UP_CHARS = "│└┘S"
RIGHT_CHARS = "─┌└S"
DOWN_CHARS = "│┌┐S"
LEFT_CHARS = "─┐┘S"


def get_new_coords(coord, field: Field, visited):
    j, i = coord
    char = field[coord]
    new_coords = []

    if char in UP_CHARS and j > 0:
        coord = (j - 1, i)
        new_char = field[coord]
        if coord not in visited and new_char in DOWN_CHARS:
            new_coords.append(coord)

    if char in RIGHT_CHARS and i < field.width - 1:
        coord = (j, i + 1)
        new_char = field[coord]
        if coord not in visited and new_char in LEFT_CHARS:
            new_coords.append(coord)

    if char in DOWN_CHARS and j < field.height - 1:
        coord = (j + 1, i)
        new_char = field[coord]
        if coord not in visited and new_char in UP_CHARS:
            new_coords.append(coord)

    if char in LEFT_CHARS and i > 0:
        coord = (j, i - 1)
        new_char = field[coord]
        if coord not in visited and new_char in RIGHT_CHARS:
            new_coords.append(coord)

    return new_coords


def get_new_coord(*args):
    new_coords = get_new_coords(*args)

    return new_coords[0] if new_coords else None


def get_loop(field, start):
    coord = None
    visited = set()
    loop = [start]
    while coord != start:
        coord = get_new_coord(loop[-1], field, visited)

        if coord:
            visited.add(coord)
            loop.append(coord)

    return loop, visited


def get_domains(field, boundary):
    domains = []
    unvisited = set(coord for coord in field.coords() if coord not in boundary)

    while unvisited:
        current_domain = set()
        current_step = set([next(iter(unvisited))])  # Random element from unvisited

        while current_step:
            current_domain.update(current_step)
            next_step = set()

            for coord in current_step:
                neighbours = [
                    neighbour
                    for neighbour in field.coords_around(*coord)
                    if (neighbour not in boundary) and (neighbour not in current_domain)
                ]
                next_step.update(neighbours)

            current_step = next_step

        domains.append(current_domain)
        unvisited.difference_update(current_domain)

    return domains


def get_winding_number(coord, loop):
    total_angle = 0
    y, x = coord

    for (y_1, x_1), (y_2, x_2) in pairwise(loop):
        # We use the cross product `a x b = |a| |b| sin θ` to determine the angle between
        # the two vectors, because it preserves the sign of the angle.
        cross_product = (x_1 - x) * (y_2 - y) - (y_1 - y) * (x_2 - x)
        r_1 = ((y_1 - y) ** 2 + (x_1 - x) ** 2) ** 0.5
        r_2 = ((y_2 - y) ** 2 + (x_2 - x) ** 2) ** 0.5

        angle = asin(cross_product / (r_1 * r_2))

        total_angle += angle

    return round(total_angle / (2 * pi))


def parse_input(input_string: str):
    field = Field(input_string.translate(PIPE_TRANS))
    start = next(coord for coord, char in field.enumerate() if char == "S")

    return field, start


def solve_a(input_string: str):
    field, start = parse_input(input_string)

    coords = [start]
    visited = set()
    for num_steps in count():
        visited.update(coords)
        new_coords = set()
        for coord in coords:
            new_coords.update(get_new_coords(coord, field, visited))

        if not new_coords:
            break

        coords = new_coords

    for coord, char in field.enumerate():
        field[coord] = char if coord in visited else "."

    print(field)
    return num_steps


def solve_b(input_string: str):
    field, start = parse_input(input_string)
    loop, visited = get_loop(field, start)

    domains = get_domains(field, visited)
    num_trapped_tiles = 0

    for domain in tqdm(domains, "Calculate winding numbers"):
        if (0, 0) in domain or (field.height - 1, field.width - 1) in domain:
            winding_number = 0
        else:
            coord = next(iter(domain))  # Random element from the domain
            winding_number = get_winding_number(coord, loop)

        if winding_number != 0:
            num_trapped_tiles += len(domain)

        for coord in domain:
            field[coord] = "I" if winding_number else "O"

    print(field)
    return num_trapped_tiles
