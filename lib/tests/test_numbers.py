import pytest
from lib.numbers import ceildiv

test_cases = [
    (-7, 3, -2),
    (-6, 3, -2),
    (-5, 3, -1),
    (-4, 3, -1),
    (-3, 3, -1),
    (-2, 3, 0),
    (-1, 3, 0),
    (0, 3, 0),
    (1, 3, 1),
    (2, 3, 1),
    (3, 3, 1),
    (4, 3, 2),
    (5, 3, 2),
    (6, 3, 2),
    (7, 3, 3),
]


@pytest.mark.parametrize("a, b, expected", test_cases)
def test_ceil_div(a, b, expected):
    assert ceildiv(a, b) == expected
