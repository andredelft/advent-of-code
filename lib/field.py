from typing import Generator, Iterable
from itertools import chain

from .geometry import Coordinate


class Field(object):
    def __init__(self, field: list[list[str]] | list[str] | str):
        if isinstance(field, str):
            self.field = [list(line) for line in field.split("\n")]
        else:
            self.field = [list(line) for line in field]

        self.height = len(self.field)
        self.width = len(self.field[0])

    def __repr__(self):
        return f"<Field ({self.height}x{self.width})>"

    def __str__(self):
        return "\n".join("".join(line) for line in self.field)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.field == other.field

    def __len__(self):
        return self.height * self.width

    def __getitem__(self, coord: Coordinate):
        if (
            coord[0] < 0
            or coord[1] < 0
            or coord[0] >= self.height
            or coord[1] >= self.width
        ):
            raise IndexError("Field index out of range")

        return self.field[coord[0]][coord[1]]

    def __setitem__(self, key: Coordinate, value):
        self.field[key[0]][key[1]] = value

    def __iter__(self):
        for coord in self.coords():
            yield self[coord]

    @property
    def dimensions(self):
        return (self.height, self.width)

    def coords(self) -> Generator[Coordinate, None, None]:
        for j in range(self.height):
            for i in range(self.width):
                yield Coordinate(j, i)

    def enumerate(self):
        for coord in self.coords():
            yield coord, self[coord]

    def pairwise(self):
        for coord in self.coords():
            y, x = coord

            if y != self.height - 1:
                yield coord, Coordinate(y + 1, x)

            if x != self.width - 1:
                yield coord, Coordinate(y, x + 1)

    def find(self, value: str):
        return next(c for c, v in self.enumerate() if v == value)

    def row(self, index: int, joined=False):
        _row = self.field[index]
        return "".join(_row) if joined else _row

    def col(self, index: int, joined=False):
        _col = [self[j, index] for j in range(self.height)]
        return "".join(_col) if joined else _col

    def rows(self, joined=False):
        for j in range(self.height):
            _row = self.field[j]
            yield "".join(_row) if joined else _row

    def cols(self, joined=False):
        for i in range(self.width):
            _col = [self[j, i] for j in range(self.height)]
            yield "".join(_col) if joined else _col

    def coords_around(
        self,
        y: int | list[int, int] | tuple[int, int],
        x: int | list[int, int] | tuple[int, int],
        straight=True,
        diagonal=True,
    ):
        if isinstance(y, list) or isinstance(y, tuple):
            top = y[0] - 1
            btm = y[1]
        else:
            top = y - 1
            btm = y + 1

        if isinstance(x, list) or isinstance(x, tuple):
            lft = x[0] - 1
            rgt = x[1]
        else:
            lft = x - 1
            rgt = x + 1

        if diagonal and top >= 0 and lft >= 0:
            yield Coordinate(top, lft)

        if straight and top >= 0:
            for i in range(lft + 1, rgt):
                yield Coordinate(top, i)

        if diagonal and top >= 0 and rgt < self.width:
            yield Coordinate(top, rgt)

        if straight and rgt < self.width:
            for j in range(top + 1, btm):
                yield Coordinate(j, rgt)

        if diagonal and btm < self.height and rgt < self.width:
            yield Coordinate(btm, rgt)

        if straight and btm < self.height:
            for i in reversed(range(lft + 1, rgt)):
                yield Coordinate(btm, i)

        if diagonal and btm < self.height and lft >= 0:
            yield Coordinate(btm, lft)

        if straight and lft >= 0:
            for j in reversed(range(top + 1, btm)):
                yield Coordinate(j, lft)

    def contains(self, coord: Coordinate):
        return 0 <= coord[0] < self.height and 0 <= coord[1] < self.width

    def is_edge(self, coord: Coordinate):
        y, x = coord

        return y in [0, self.height - 1] or x in [0, self.width - 1]

    def is_corner(self, coord: Coordinate):
        return coord in [
            (0, 0),
            (0, self.width - 1),
            (self.height - 1, 0),
            (self.height - 1, self.width - 1),
        ]

    def copy(self):
        return Field([_row.copy() for _row in self.rows()])

    def draw(self, coords: Iterable[Coordinate], char="#"):
        for coord in coords:
            self[coord] = char

    @classmethod
    def blank(cls, height, width, char="."):
        return cls([[char for _ in range(width)] for _ in range(height)])

    @classmethod
    def from_coords(
        cls,
        *coord_groups: list[Iterable[Coordinate]],
        char: str | Iterable[str] = "#",
        blank_char=".",
    ):
        min_y = max_y = min_x = max_x = 0

        for coord in chain(*coord_groups):
            min_y = min(min_y, coord[0])
            max_y = max(max_y, coord[0])
            min_x = min(min_x, coord[1])
            max_x = max(max_x, coord[1])

        if min_x or min_y:
            max_x -= min_x
            max_y -= min_y

            translation = Coordinate(min_y, min_x)
            coord_groups = [
                (coord - translation for coord in coords) for coords in coord_groups
            ]

        field = cls.blank(max_y + 1, max_x + 1, char=blank_char)

        for coord_group, group_char in zip(coord_groups, char, strict=True):
            field.draw(coord_group, char=group_char)

        return field


def flood_fill(
    start: Coordinate,
    field: Field,
    boundary_char: str = "#",
    field_value="",
    straight=True,
    diagonal=True,
):
    coords_to_visit = {start}
    visited: set[Coordinate] = set()

    def is_inside(coord):
        value = field[coord]
        return value == field_value if field_value else value != boundary_char

    while coords_to_visit:
        new_coords_to_visit = set()
        for coord in coords_to_visit:
            visited.add(coord)
            for coord in field.coords_around(
                *coord, straight=straight, diagonal=diagonal
            ):
                if coord not in visited and is_inside(coord):
                    new_coords_to_visit.add(coord)

        coords_to_visit = new_coords_to_visit

    return visited
