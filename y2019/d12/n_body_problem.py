import numpy as np
from itertools import combinations
from itertools import count

from lib.regex import parse_numbers
from lib.math import lcm


class Moon:
    def __init__(self, position: list[int]):
        self.initial_position = np.array(position)
        self.position = np.array(position, dtype=int)
        self.velocity = np.zeros(3, dtype=int)

    @property
    def potential_energy(self):
        return sum(abs(self.position))

    @property
    def kinetic_energy(self):
        return sum(abs(self.velocity))

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy


def parse_input(input_string: str):
    return [
        Moon(parse_numbers(line, include_negative=True))
        for line in input_string.split("\n")
    ]


def move(moons: list[Moon]):
    for m1, m2 in combinations(moons, 2):
        for i in range(3):
            if m1.position[i] > m2.position[i]:
                m1.velocity[i] -= 1
                m2.velocity[i] += 1
            elif m1.position[i] < m2.position[i]:
                m1.velocity[i] += 1
                m2.velocity[i] -= 1

    for moon in moons:
        moon.position += moon.velocity


def solve_a(input_string: str, num_steps=1000):
    moons = parse_input(input_string)

    for _ in range(num_steps):
        move(moons)

    return sum(moon.energy for moon in moons)


def solve_b(input_string: str):
    moons = parse_input(input_string)

    periods = [None for _ in range(3)]

    for n in count(1):
        move(moons)

        # The movement along the different coordinates is independent, so we search for a period
        # along each axis. The period of the total constellation is then the least common multiple
        # of all these periods
        for i in range(3):
            if not periods[i] and all(
                moon.position[i] == moon.initial_position[i] and moon.velocity[i] == 0
                for moon in moons
            ):
                periods[i] = n

        if all(periods):
            break

    return lcm(*periods)
