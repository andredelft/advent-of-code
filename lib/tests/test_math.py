from lib.math import get_nth_digit, sieve
import pytest


test_cases = [
    (100, 2, 1),
    (25, 0, 5),
    (14001, 1, 0),
    (25, 4, 0),
]


@pytest.mark.parametrize("number, n, expected", test_cases)
def test_get_nth_digit(number, n, expected):
    assert get_nth_digit(number, n) == expected


test_cases_sieve = [
    (((1, 13), (2, 7), (3, 5)), 443),
    (((0, 3), (3, 4), (4, 5)), 39),
]


@pytest.mark.parametrize("args, expected", test_cases_sieve)
def test_sieve(args, expected):
    assert sieve(*args) == expected
