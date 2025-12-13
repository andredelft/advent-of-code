from lib.regex import parse_numbers


def parse_input(input_string: str):
    *blocks, fields_str = input_string.split("\n\n")

    areas = [block.count("#") for block in blocks]
    fields: list[tuple[int, int, list[int]]] = []

    for field in fields_str.split("\n"):
        width, height, *block_count = parse_numbers(field)
        fields.append((width, height, block_count))

    return areas, fields


def solve_a(input_string: str):
    areas, fields = parse_input(input_string)

    return sum(
        width * height >= sum(area * count for area, count in zip(areas, block_count))
        for width, height, block_count in fields
    )
