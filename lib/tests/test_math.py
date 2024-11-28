from lib.math import get_nth_digit
import pytest


test_cases = [
    (100, 2, 1),
    (25, 0, 5),
    (14001, 1, 0),
    (25, 4, 0),
]


@pytest.mark.parametrize("test_case", test_cases)
def test_get_nth_digit(test_case):
    number, n, expected = test_case

    assert get_nth_digit(number, n) == expected
