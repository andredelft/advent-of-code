from lib.field import Field, Coordinate
from itertools import combinations, chain
from lib.math import gcd
from fractions import Fraction


def solve_a(input_string: str, return_data=False):
    field = Field(input_string)

    asteroids = set(coord for (coord, value) in field.enumerate() if value == "#")

    visible_map: dict[Coordinate, set[Coordinate]] = {
        coord: set() for coord in asteroids
    }

    for coord1, coord2 in combinations(asteroids, 2):
        if coord2 in visible_map.get(coord1):
            continue

        delta = coord2 - coord1

        if delta[0] == 0:
            divisor = abs(delta[1])
        elif delta[1] == 0:
            divisor = abs(delta[0])
        else:
            divisor = gcd(*delta)

        has_asteroid_in_between = False

        if divisor > 1:
            step = delta // divisor

            for n in range(1, divisor):
                coord = coord1 + (step * n)

                if coord in asteroids:
                    visible_map[coord1].add(coord)
                    visible_map[coord].add(coord1)
                    has_asteroid_in_between = True
                    break

        if not has_asteroid_in_between:
            visible_map[coord1].add(coord2)
            visible_map[coord2].add(coord1)

    monitoring_station = None
    max_visible_asteroids = 0

    for asteroid, visible_asteroids in visible_map.items():
        num_visible_asteroids = len(visible_asteroids)

        if num_visible_asteroids > max_visible_asteroids:
            monitoring_station = asteroid
            max_visible_asteroids = num_visible_asteroids

    if return_data:
        return monitoring_station, visible_map[monitoring_station]

    return max_visible_asteroids


def solve_b(input_string: str):
    monitoring_station, visible_asteroids = solve_a(input_string, return_data=True)

    halves = [[] for _ in range(2)]
    axis = [[] for _ in range(2)]

    for visible_asteroid in visible_asteroids:
        relative_asteroid = visible_asteroid - monitoring_station

        if relative_asteroid[1] == 0:
            if relative_asteroid[0] > 0:
                axis[0].append(relative_asteroid)
            elif relative_asteroid[0] < 0:
                axis[1].append(relative_asteroid)
        elif relative_asteroid[1] > 0:
            halves[0].append(relative_asteroid)
        elif relative_asteroid[1] < 0:
            halves[1].append(relative_asteroid)

    for halve in halves:
        halve.sort(key=lambda coord: Fraction(*coord))

    vaporization_list = list(chain(axis[0], halves[0], axis[1], halves[1]))

    two_hundreth = vaporization_list[199] + monitoring_station
    return 100 * two_hundreth[1] + two_hundreth[0]
