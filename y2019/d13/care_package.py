from itertools import batched
from readchar import readkey, key
import time

from y2019.intcode import Intcode
from lib.field import Field, Coordinate


Tiles = dict[int, list[Coordinate]]


def parse_output(output: list[int]):
    score = None
    tiles: Tiles = {n: [] for n in range(5)}

    for x, y, n in batched(output, 3):
        if (x, y) == (-1, 0):
            score = n
            continue

        coord = Coordinate(y, x)

        tiles[n].append(coord)

    return tiles, score


TILE_MAP = {
    0: " ",
    1: "#",
    2: ".",
    3: "=",
    4: "o",
}


def draw_tiles(field: Field, tiles: Tiles):
    for tile_id, coords in tiles.items():
        field.draw(coords, TILE_MAP[tile_id])


def solve_a(input_string: str):
    intcode = Intcode.parse_input(input_string, output_as_array=True)

    output = intcode.run()
    tiles, _ = parse_output(output)

    return len(tiles[2])


def solve_b(input_string: str, manual=False, visual=True):
    intcode = Intcode.parse_input(
        input_string, output_as_array=True, pause_on_input=True
    )

    intcode.memory[0] = 2

    field = Field.blank(23, 43)
    score = 0

    intcode.run()

    while True:
        tiles, new_score = parse_output(intcode.value)

        draw_tiles(field, tiles)

        if new_score != None:
            score = new_score

        if manual or visual:
            print(field)
            print("Score:", score)
            time.sleep(0.01)

        if intcode.has_terminated:
            break

        if manual:
            match readkey():
                case key.LEFT:
                    intcode_input = -1
                case key.RIGHT:
                    intcode_input = 1
                case _:
                    intcode_input = 0

        else:
            # Algorithm for determining cursor position
            if tiles[4]:
                ball_coord = tiles[4][0]

            if tiles[3]:
                cursor_coord = tiles[3][0]

            if cursor_coord[1] > ball_coord[1]:
                intcode_input = -1
            elif cursor_coord[1] < ball_coord[1]:
                intcode_input = 1
            else:
                intcode_input = 0

        intcode.run(intcode_input)

    return score
