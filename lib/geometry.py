from lib.array import product
from itertools import pairwise
from typing import Self, Iterable
from enum import Enum


class Coordinate(tuple[int, int]):
    def __new__(cls, y: int, x: int):
        return super().__new__(cls, (y, x))

    def __add__(self: Self, other: Iterable[int]):
        return Coordinate(*(v1 + v2 for (v1, v2) in zip(self, other)))

    def __sub__(self: Self, other: Iterable[int]):
        return Coordinate(*(v1 - v2 for (v1, v2) in zip(self, other)))

    def __mul__(self, other: int):
        if not isinstance(other, int):
            raise ValueError("Only integer multiplication is allowed")

        return Coordinate(*(v * other for v in self))

    def __rmul__(self, other: int):
        return self * other

    def __floordiv__(self, other: int):
        if not isinstance(other, int):
            raise ValueError("Only integer division is allowed")

        return Coordinate(*(v // other for v in self))

    def __len__(self):
        # Manhattan distance from (0, 0)
        return sum(abs(n) for n in self)

    def rotate(self, num_rotations=1):
        match num_rotations % 4:
            case 0:
                return self
            case 1:
                return self.rotate_right()
            case 2:
                return -1 * self
            case 3:
                return self.rotate_left()

    def rotate_right(self):
        return Coordinate(self[1], -1 * self[0])

    def rotate_left(self):
        return Coordinate(-1 * self[1], self[0])


class Direction(Enum):
    UP = Coordinate(-1, 0)
    RIGHT = Coordinate(0, 1)
    DOWN = Coordinate(1, 0)
    LEFT = Coordinate(0, -1)

    @classmethod
    def values(self):
        for member in self:
            yield member.value


Segment = tuple[Coordinate, Coordinate]


def polygon_area(nodes: list[Coordinate]):
    """
    Find the area of the polygon enclosed by `coords` using the shoelace formula.
    NB: Since we only accept integer coordinates, we know that the result has to
    be an integer as well.
    """
    return (
        sum((y_1 + y_2) * (x_1 - x_2) for (y_1, x_1), (y_2, x_2) in pairwise(nodes))
        // 2
    )


def manhattan_distance(coord_1: Coordinate, coord_2: Coordinate = (0, 0)):
    return sum(abs(coord_1[i] - coord_2[i]) for i in range(len(coord_1)))


def euclidean_distance(coord_1: Coordinate, coord_2: Coordinate) -> float:
    return sum(abs(coord_1[i] - coord_2[i]) ** 2 for i in range(len(coord_1))) ** 0.5


def square_area(coord_1: Coordinate, coord_2: Coordinate):
    """Square area spanned by the two input coordinates as opposite corners"""
    return product(abs(coord_1[i] - coord_2[i]) + 1 for i in range(len(coord_1)))


def segment_intersection(segment_1: Segment, segment_2: Segment):
    """
    Calculate the intersection point between two line segments. Returns `None` if
    there isn't any.

    https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line_segment
    """
    (y1, x1), (y2, x2) = segment_1
    (y3, x3), (y4, x4) = segment_2

    det_1 = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
    det_2 = (x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)
    det_3 = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if det_3 == 0:  # Lines are parallel
        return

    t = det_1 / det_3
    u = det_2 / det_3

    if 0 <= t <= 1 and 0 <= u <= 1:
        return (y1 + t * (y2 - y1), x1 + t * (x2 - x1))
