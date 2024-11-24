from tqdm import tqdm
import time

TEST_INPUT = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def parse_input(input_string: str):
    start = None
    end = None
    field = []
    for i, line in enumerate(input_string.split("\n")):
        field_stroke = []
        for j, char in enumerate(line):
            match char:
                case "S":
                    start = (i, j)
                    field_stroke.append(0)
                case "E":
                    end = (i, j)
                    field_stroke.append(25)
                case _:
                    field_stroke.append(ord(char) - ord("a"))
        field.append(field_stroke)

    if not start or not end:
        raise ValueError("Start or end not found")

    return field, start, end


Coordinate = tuple[int, int]
Field = list[list[int]]


def neighbours(position: Coordinate, height: int, width: int):
    y, x = position
    if x < width - 1:
        yield (y, x + 1)
    if y > 0:
        yield (y - 1, x)
    if y < height - 1:
        yield (y + 1, x)
    if x > 0:
        yield (y, x - 1)


def iter_indices(height, width):
    for i in range(height):
        for j in range(width):
            yield i, j


def dijkstra(field: Field, start: Coordinate, reversed=False):
    height = len(field)
    width = len(field[0])
    unvisited = set((i, j) for i, j in iter_indices(height, width))

    current_node = start
    current_distance = 0
    shortest_distances: dict[Coordinate, int] = {start: current_distance}
    distance_sources: dict[Coordinate, Coordinate] = {}
    while current_node:
        y, x = current_node
        accessible_neighbours = [
            (i, j)
            for i, j in neighbours(current_node, height, width)
            if (i, j) in unvisited
            and (
                (not reversed and field[i][j] <= field[y][x] + 1)
                or (reversed and field[i][j] >= field[y][x] - 1)
            )
        ]

        for i, j in accessible_neighbours:
            current_distance += 1
            current_shortest_distance = shortest_distances.get((i, j))
            if (
                not current_shortest_distance
                or current_distance < current_shortest_distance
            ):
                shortest_distances[i, j] = current_distance
                distance_sources[i, j] = current_node

        unvisited.remove(current_node)
        # draw_trail(field, unvisited.intersection(shortest_distances.keys()))
        current_node = min(
            unvisited.intersection(shortest_distances.keys()),
            key=lambda coord: shortest_distances[coord],
            default=None,
        )

    return distance_sources


def draw_trail(field: Field, trail: list[Coordinate]):
    visited = set(trail)
    lines = []
    for i in range(len(field)):
        line = ""
        for j in range(len(field[0])):
            if (i, j) in visited:
                line += "."
            else:
                char = chr(field[i][j] + ord("a"))
                line += char

        lines.append(line)
    print("\n".join(lines), end="\n\n")
    time.sleep(0.01)


def find_trail(
    distance_sources: dict[Coordinate, Coordinate], start: Coordinate, end: Coordinate
):
    trail = [end]

    while trail[0] != start:
        trail.insert(0, distance_sources[trail[0]])

    return trail


def part_a(input_string=TEST_INPUT):
    field, start, end = parse_input(input_string)
    distance_sources = dijkstra(field, start)

    trail = find_trail(distance_sources, start, end)

    draw_trail(field, trail)
    return len(trail) - 1


def part_b(input_string=TEST_INPUT):
    field, _, end = parse_input(input_string)
    height = len(field)
    width = len(field[0])

    distance_sources = dijkstra(field, end, reversed=True)  # Dijkstra starting from end

    # We only need to check a's that are directly next to some b
    possible_starts = [
        (i, j)
        for i, j in iter_indices(height, width)
        if field[i][j] == 0
        and any(field[k][l] == 1 for k, l in neighbours((i, j), height, width))
    ]

    shortest_trail = None
    for start in tqdm(possible_starts):
        trail = find_trail(distance_sources, end, start)
        if not shortest_trail or len(trail) < len(shortest_trail):
            shortest_trail = trail

    draw_trail(field, shortest_trail)
    return len(shortest_trail) - 1
