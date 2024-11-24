from more_itertools import chunked

from lib.regex import parse_numbers


def is_in_range(value: int, range_start: int, range_length: int):
    return range_start <= value < range_start + range_length


def parse_input(input_string: str):
    blocks = input_string.split("\n\n")

    seeds = parse_numbers(blocks[0])

    maps = []
    for block in blocks[1:]:
        map_parts = []
        for line in block.split("\n"):
            numbers = parse_numbers(line)
            if len(numbers) == 3:
                map_parts.append(numbers)

        maps.append(map_parts)
    return seeds, maps


def solve_a(input_string: str):
    seeds, maps = parse_input(input_string)
    min_location = -1

    for seed in seeds:
        source_value = seed

        for map_parts in maps:
            destination_value = source_value

            for map_part in map_parts:
                (destination_range_start, source_range_start, range_length) = map_part

                if is_in_range(source_value, source_range_start, range_length):
                    destination_value = (
                        source_value - source_range_start + destination_range_start
                    )
                    break

            source_value = destination_value

        location = source_value

        if min_location < 0:
            min_location = source_value
        else:
            min_location = min(min_location, location)

    return min_location


def solve_b(input_string: str):
    seeds, maps = parse_input(input_string)
    location = 0

    seed_in_range = False
    while not seed_in_range:
        source_value = location

        for map_parts in reversed(maps):
            destination_value = source_value

            # We reverse the mapping, hence we switch source & destination
            for map_part in map_parts:
                (source_range_start, destination_range_start, range_length) = map_part

                if is_in_range(source_value, source_range_start, range_length):
                    destination_value = (
                        source_value - source_range_start + destination_range_start
                    )
                    break

            source_value = destination_value

        seed = destination_value

        for seed_range_start, range_length in chunked(seeds, 2):
            if is_in_range(seed, seed_range_start, range_length):
                seed_in_range = True
                break

        if not seed_in_range:
            location += 1

    return location
