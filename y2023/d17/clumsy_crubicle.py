from lib.field import Field
from lib.dijkstra import dijkstra


def get_neighbours(node, field: Field, num_straight_range: tuple[int, int]):
    (j, i), direction, num_straight = node

    match direction:
        case "N" | "S" if num_straight >= num_straight_range[0]:
            allowed_dirs = ["E", "W"]
        case "E" | "W" if num_straight >= num_straight_range[0]:
            allowed_dirs = ["N", "S"]
        case "":
            allowed_dirs = ["N", "E", "S", "W"]
        case _:
            allowed_dirs = []

    if num_straight < num_straight_range[1]:
        allowed_dirs.append(direction)

    for new_dir in allowed_dirs:
        match new_dir:
            case "N" if j > 0:
                new_coord = (j - 1, i)
            case "E" if i < field.width - 1:
                new_coord = (j, i + 1)
            case "S" if j < field.height - 1:
                new_coord = (j + 1, i)
            case "W" if i > 0:
                new_coord = (j, i - 1)
            case _:
                continue

        new_num_straight = num_straight + 1 if direction == new_dir else 1

        yield (new_coord, new_dir, new_num_straight), int(field[new_coord])


def part_a(input_string: str, num_straight=(0, 3)):
    field = Field(input_string)

    # Format: (j, i), direction, num_straight
    start_node = ((0, 0), "", 0)

    end_coord = (field.height - 1, field.width - 1)

    distance_map, end_node = dijkstra(
        start_node,
        end_node=lambda node: node[0] == end_coord,
        get_neighbours=lambda node: get_neighbours(node, field, num_straight),
        total_nodes=len(field) * 4 * num_straight[1],
    )

    path = set(node[0] for node in distance_map.backtrace_path(end_node))

    for coord in field.coords():
        field[coord] = "#" if coord in path else "."

    print(field)
    return distance_map.get_distance(end_node)


def part_b(input_string: str):
    return part_a(input_string, num_straight=(4, 10))
