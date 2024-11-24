from typing import Literal
from tqdm import tqdm

from lib.field import Field, Coordinate

Direction = Literal["N", "E", "S", "W"]
Ray = tuple[Coordinate, Direction]
Rays = set[Ray]


def north(j: int, i: int) -> Ray:
    return ((j - 1, i), "N")


def east(j: int, i: int) -> Ray:
    return ((j, i + 1), "E")


def south(j: int, i: int) -> Ray:
    return ((j + 1, i), "S")


def west(j: int, i: int) -> Ray:
    return ((j, i - 1), "W")


def yield_new_rays(ray: Rays, field: Field):
    coord, direction = ray

    match (direction, field[coord]):
        case ("N", "\\") | ("S", "/"):
            yield west(*coord)
        case ("N", "/") | ("S", "\\"):
            yield east(*coord)
        case ("E", "\\") | ("W", "/"):
            yield south(*coord)
        case ("E", "/") | ("W", "\\"):
            yield north(*coord)
        case ("N", "-") | ("S", "-"):
            yield east(*coord)
            yield west(*coord)
        case ("E", "|") | ("W", "|"):
            yield north(*coord)
            yield south(*coord)
        case ("N", _):
            yield north(*coord)
        case ("E", _):
            yield east(*coord)
        case ("S", _):
            yield south(*coord)
        case ("W", _):
            yield west(*coord)
        case _:
            raise ValueError(f"Invalid ray: {(direction, field[coord])}")


def get_ray_path(ray: Ray, field: Field):
    rays = {ray}
    history: set[Ray] = set()
    visited: set[Coordinate] = {ray[0]}

    while not rays.issubset(history):
        history.update(rays)

        new_rays = set()
        for ray in rays:
            for new_ray in yield_new_rays(ray, field):
                if field.contains(new_ray[0]) and new_ray not in history:
                    new_rays.add(new_ray)
                    visited.add(new_ray[0])

        rays = new_rays

    return visited


def part_a(input_string: str):
    field = Field(input_string)
    ray = ((0, 0), "E")  # Entered (0, 0) eastward
    visited = get_ray_path(ray, field)

    for coord in visited:
        field[coord] = "#"

    print(field)
    return len(visited)


def part_b(input_string: str):
    field = Field(input_string)

    max_visited = set()
    print(field, end="\n\n")

    for i in tqdm(range(field.height)):
        for ray in [
            ((i, 0), "E"),
            ((i, field.width - 1), "W"),
            ((0, i), "S"),
            ((field.height - 1, i), "N"),
        ]:
            visited = get_ray_path(ray, field)

            if len(visited) > len(max_visited):
                max_visited = visited

    for coord in max_visited:
        field[coord] = "#"

    print(field)
    return len(max_visited)
