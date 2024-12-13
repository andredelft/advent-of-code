from lib.field import Field, Coordinate, flood_fill


def parse_input(input_string: str):
    field = Field(input_string)

    coord_set = set(field.coords())

    groups: list[set[Coordinate]] = []

    while coord_set:
        start = coord_set.pop()
        group = flood_fill(start, field, field_value=field[start], diagonal=False)

        groups.append(group)
        coord_set.difference_update(group)

    return field, groups


def solve_a(input_string: str):
    field, groups = parse_input(input_string)
    border_pairs = {(c1, c2) for c1, c2 in field.pairwise() if field[c1] != field[c2]}
    total_price = 0

    for group in groups:
        area = len(group)

        # Edges between groups
        perimeter = sum(bool(group.intersection(pair)) for pair in border_pairs)

        # Edges (+1) and corners (+2) of the field
        for coord in group:
            if field.is_edge(coord):
                perimeter += 2 if field.is_corner(coord) else 1

        total_price += area * perimeter

    return total_price


def num_coord_corners(coord: Coordinate, group: set[Coordinate]):
    y, x = coord
    num_corners = 0

    # Sides
    t = (y - 1, x)
    r = (y, x + 1)
    b = (y + 1, x)
    l = (y, x - 1)

    # Corners
    tr = (y - 1, x + 1)
    br = (y + 1, x + 1)
    bl = (y + 1, x - 1)
    tl = (y - 1, x - 1)

    adjacent_sides = {tr: (t, r), br: (b, r), bl: (b, l), tl: (t, l)}

    for corner, (side_1, side_2) in adjacent_sides.items():
        if not side_1 in group and not side_2 in group:
            # Convex corner
            num_corners += 1
        elif not corner in group and side_1 in group and side_2 in group:
            # Concave corner
            num_corners += 1

    return num_corners


def solve_b(input_string: str):
    _, groups = parse_input(input_string)
    total_price = 0

    for group in groups:
        area = len(group)
        num_corners = sum(num_coord_corners(coord, group) for coord in group)

        total_price += area * num_corners

    return total_price
