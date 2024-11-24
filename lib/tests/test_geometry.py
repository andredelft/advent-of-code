from lib.geometry import segment_intersection


def test_segment_intersection():
    assert segment_intersection(((0, -1), (0, 1)), ((-1, 0), (1, 0))) == (0, 0)
    assert segment_intersection(((1, 1), (1, -1)), ((-1, 1), (-1, -1))) == None
