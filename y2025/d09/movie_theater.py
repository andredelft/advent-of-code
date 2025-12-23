from lib.regex import parse_numbers
from lib.geometry import Coordinate, iter_edge, square_area
from lib.field import Field, flood_fill
from itertools import combinations, pairwise, product, chain


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        yield parse_numbers(line, cast_as=tuple)


def solve_a(input_string: str):
    coords = parse_input(input_string)
    return max(square_area(*pair) for pair in combinations(coords, 2))


def compress_coords(coords: list[Coordinate]):
    y_coords: list[int] = []
    x_coords: list[int] = []

    for coord in coords:
        y_coords.append(coord[0])
        x_coords.append(coord[1])

    decompressed_y = sorted(set(y_coords))
    decompressed_x = sorted(set(x_coords))

    y_rank = {y: i for i, y in enumerate(decompressed_y)}
    x_rank = {x: i for i, x in enumerate(decompressed_x)}

    def decompress(c: Coordinate):
        return Coordinate(decompressed_y[c[0]], decompressed_x[c[1]])

    return [(y_rank[y], x_rank[x]) for y, x in coords], decompress


def solve_b(input_string: str):
    coords = list(parse_input(input_string))
    coords, decompress = compress_coords(coords)

    field = Field.from_coords(coords)

    borders = pairwise(coords + [coords[0]])
    field.draw(chain.from_iterable(iter_edge(*border) for border in borders))

    start = Coordinate(field.height // 2, field.width // 4)
    visited = flood_fill(start, field)
    field.draw(visited)

    def decompressed_area(pair: tuple[Coordinate, Coordinate]):
        return square_area(*map(decompress, pair))

    coord_pairs = sorted(combinations(coords, 2), key=decompressed_area, reverse=True)

    for pair in coord_pairs:
        remaining_corners = [(pair[0][0], pair[1][1]), (pair[1][0], pair[0][1])]

        if any(field[c] != "#" for c in remaining_corners):
            continue

        edges = product(pair, remaining_corners)
        is_inside = not any(
            field[c] != "#"
            for c in chain.from_iterable(iter_edge(*edge) for edge in edges)
        )

        if is_inside:
            return decompressed_area(pair)
