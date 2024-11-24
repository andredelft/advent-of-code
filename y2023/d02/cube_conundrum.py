import re

RE_CUBES = r"(\d+) (red|green|blue)"


def parse_input(input_string: str):
    lines = input_string.split("\n")

    for line in lines:
        cube_sets = line.split(";")

        game = []

        for cube_set in cube_sets:
            cubes = {"red": 0, "green": 0, "blue": 0}
            for match in re.finditer(RE_CUBES, cube_set):
                num_cubes, color = match.groups()
                cubes[color] = int(num_cubes)

            game.append(cubes)

        yield game


def solve_a(input_string: str):
    valid_sum = 0

    for game_num, games in enumerate(parse_input(input_string), start=1):
        is_invalid = False

        for game in games:
            if (game["red"] > 12) or (game["green"] > 13) or (game["blue"] > 14):
                is_invalid = True
                break

        if not is_invalid:
            valid_sum += game_num

    return valid_sum


def solve_b(input_string: str):
    power_sum = 0

    for games in parse_input(input_string):
        max_red = 0
        max_green = 0
        max_blue = 0

        for game in games:
            max_red = max(game["red"], max_red)
            max_green = max(game["green"], max_green)
            max_blue = max(game["blue"], max_blue)

        power_sum += max_red * max_green * max_blue

    return power_sum
