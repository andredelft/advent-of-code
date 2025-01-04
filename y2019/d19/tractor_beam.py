from y2019.intcode import Intcode
from lib.field import Coordinate
from itertools import product
from functools import cache


class TractorBeam:
    # We estimate the slope from some center points. See drawing below.
    center_points = [(20, 23), (30, 35), (50, 58), (70, 81)]
    slope = sum(y / x for y, x in center_points) / len(center_points)

    def __init__(self, intcode: Intcode):
        self.intcode = intcode

    def contains(self, coord: Coordinate):
        return bool(self.intcode.run(coord[1], coord[0], reset=True))

    def get_beam_center_estimate(self, y: int):
        return Coordinate(y, int(y / self.slope))

    @cache
    def get_edge(self, y: int):
        coord = self.get_beam_center_estimate(y)

        while self.contains(next_coord := coord + (0, -1)):
            coord = next_coord

        return coord


def solve_a(input_string: str):
    intcode = Intcode.parse_input(input_string)
    tractor_beam = TractorBeam(intcode)

    return sum(tractor_beam.contains(coord) for coord in product(range(50), repeat=2))


def solve_b(input_string: str):
    intcode = Intcode.parse_input(input_string)
    tractor_beam = TractorBeam(intcode)
    square_size = 100

    y_lower = 0
    y_upper = 5 * square_size

    edge_coords = []

    while True:
        edge_coord = tractor_beam.get_edge(y_upper)
        edge_coords.append(edge_coord)

        # Binary search
        delta_y = y_upper - y_lower
        if tractor_beam.contains(
            edge_coord + (-1 * (square_size - 1), (square_size - 1))
        ):
            if delta_y == 1:
                break
            else:
                y_upper -= delta_y // 2
        else:
            y_lower, y_upper = (y_upper, y_upper + delta_y)

    return edge_coord[0] - 99 + 10_000 * edge_coord[1]


"""
O...................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
.......#............................................................................................
........#...........................................................................................
.........#..........................................................................................
..........##........................................................................................
..(10,10).O##.......................................................................................
............##......................................................................................
.............##.....................................................................................
...............##...................................................................................
................##..................................................................................
.................##.................................................................................
..................##................................................................................
...................##...............................................................................
....................###.............................................................................
.....................###............................................................................
............(20,20).O.#X#.(20,23)...................................................................
.......................###..........................................................................
........................####........................................................................
.........................####.......................................................................
..........................####......................................................................
............................###.....................................................................
.............................####...................................................................
..............................####..................................................................
...............................####.................................................................
................................####................................................................
......................(30,30).O..##X##.(30,35)......................................................
..................................#####.............................................................
...................................#####............................................................
....................................#####...........................................................
.....................................#####..........................................................
......................................######........................................................
.......................................######.......................................................
........................................######......................................................
..........................................#####.....................................................
...........................................######...................................................
................................(40,40).O...######..................................................
.............................................######.................................................
..............................................######................................................
...............................................#######..............................................
................................................#######.............................................
.................................................#######............................................
..................................................#######...........................................
...................................................#######..........................................
....................................................########........................................
.....................................................########.......................................
..........................................(50,50).O....###X###.(50,58)..............................
........................................................#######.....................................
.........................................................########...................................
..........................................................########..................................
...........................................................########.................................
............................................................########................................
.............................................................#########..............................
..............................................................#########.............................
...............................................................#########............................
................................................................#########...........................
....................................................(60,60).O....##########.........................
..................................................................##########........................
....................................................................#########.......................
.....................................................................#########......................
......................................................................#########.....................
.......................................................................##########...................
........................................................................##########..................
.........................................................................##########.................
..........................................................................##########................
...........................................................................###########..............
..............................................................(70,70).O.....#####X#####.(70,81).....
.............................................................................###########............
..............................................................................###########...........
...............................................................................############.........
................................................................................############........
..................................................................................###########.......
...................................................................................###########......
....................................................................................############....
.....................................................................................############...
......................................................................................############..
........................................................................(80,80).O......############.
........................................................................................############
.........................................................................................###########
..........................................................................................##########
...........................................................................................#########
............................................................................................########
.............................................................................................#######
...............................................................................................#####
................................................................................................####
.................................................................................................###
..................................................................................(90,90).O.......##
...................................................................................................#
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
"""