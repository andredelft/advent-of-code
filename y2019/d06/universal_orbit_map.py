from functools import cache

Orbits = dict[str, str]


def parse_input(input_string: str):
    orbits: Orbits = {}

    for line in input_string.split("\n"):
        node_1, node_2 = line.split(")")

        orbits[node_2] = node_1

    return orbits


def solve_a(input_string):
    orbits = parse_input(input_string)

    @cache
    def num_orbits(node_name):
        if node_name in orbits.keys():
            return 1 + num_orbits(orbits[node_name])

        return 0

    nodes = set().union(orbits.keys(), orbits.values())

    return sum(num_orbits(node) for node in nodes)


def get_orbit_set(node_name, orbits: Orbits):
    orbit_set: set[str] = set()
    current_node = node_name

    while current_node:
        current_node = orbits.get(current_node)

        if current_node:
            orbit_set.add(current_node)

    return orbit_set


def solve_b(input_string):
    orbits = parse_input(input_string)

    you_orbit_set = get_orbit_set("YOU", orbits)
    san_orbit_set = get_orbit_set("SAN", orbits)

    return len(you_orbit_set.symmetric_difference(san_orbit_set))
