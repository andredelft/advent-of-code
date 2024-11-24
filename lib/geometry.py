from itertools import pairwise

Coordinate = tuple[int, int]
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
    return sum(abs(coord_1[i] - coord_2[i]) for i in range(2))


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
