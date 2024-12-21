from lib.field import Field
from lib.geometry import Coordinate, Direction
from lib.dijkstra import dijkstra


def get_neighbour_nodes(coord: Coordinate, direction: Coordinate, field: Field):
    if field[coord + direction] != "#":
        yield (coord + direction, direction), 1

    for n in [1, -1]:
        yield (coord, direction.rotate(n)), 1000


def solve_a(input_string: str):
    field = Field(input_string)

    start = field.find("S")
    direction = Coordinate(0, 1)
    end = field.find("E")

    is_end_node = lambda n: n[0] == end
    get_neighbours = lambda n: get_neighbour_nodes(*n, field)

    distance_map, end_node = dijkstra((start, direction), is_end_node, get_neighbours)

    return distance_map.get_distance(end_node)


def solve_b(input_string: str):
    field = Field(input_string)

    start = field.find("S")
    direction = Coordinate(0, 1)
    end = field.find("E")

    is_end_node = lambda n: n[0] == end
    get_neighbours = lambda n: get_neighbour_nodes(*n, field)

    distance_map, end_node = dijkstra((start, direction), is_end_node, get_neighbours)
    reverse_distance_map = dijkstra(
        start_node=(end, -1 * end_node[1]),
        end_node=(start, -1 * direction),
        get_neighbours=get_neighbours,
    )

    optimal_distance = distance_map.get_distance(end_node)
    posible_seats: list[Coordinate] = []

    for coord, value in field.enumerate():
        if value == "#":
            continue

        for direction in Direction.values():
            try:
                distance_to_start = distance_map.get_distance((coord, direction))
                distance_to_end = reverse_distance_map.get_distance(
                    (coord, direction * -1)
                )
            except KeyError:
                continue

            if distance_to_start + distance_to_end == optimal_distance:
                posible_seats.append(coord)
                break

    return len(posible_seats)
