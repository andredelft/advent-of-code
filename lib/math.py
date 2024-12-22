from collections import Counter
from functools import total_ordering
from itertools import pairwise

from .array import product
from .field import Coordinate

Number = int | float


def get_nth_digit(number: int, n: int, with_leading_zeros=True):
    number_str = str(number)
    number_size = len(number_str)

    if n >= number_size:
        if not with_leading_zeros:
            raise ValueError(f"Number {number} doesn't have digit {n}")

        return 0

    return int(number_str[number_size - (n + 1)])


def solve_quadratic(a: Number, b: Number, c: Number) -> list[float]:
    """Solve the quadratic equation `ax ** 2 + bx + c == 0` with `a != 0`"""

    determinant = b**2 - 4 * a * c

    if determinant > 0:
        numerator_1 = -1 * b - (determinant) ** 0.5
        numerator_2 = -1 * b + (determinant) ** 0.5
        denominator = 2 * a

        sol_1 = numerator_1 / denominator
        sol_2 = numerator_2 / denominator

        return [sol_1, sol_2] if a > 0 else [sol_2, sol_1]
    elif determinant == 0:
        return [-1 * b / (2 * a)]
    else:
        return []


def iter_prime_factors(num: int):
    """Very primitive prime factorization method, works fine for prime factors < 10^6"""
    if num < 0:
        num *= -1

    factor = 2
    while num != 1:
        while num % factor == 0:
            yield factor
            num //= factor
        factor += 1


def prime_factors(num: int):
    return list(iter_prime_factors(num))


def lcm(*nums: int):
    """The least common multiple of given numbers"""
    prime_union = Counter()
    for num in nums:
        new_primes = Counter(iter_prime_factors(num))

        for prime, num_factors in new_primes.items():
            prime_union[prime] = max(prime_union[prime], num_factors)

    return product(prime_union.elements())


def gcd(*nums: int):
    """The greatest common divider of given numbers"""
    if not nums:
        return 1

    common_primes = Counter(iter_prime_factors(nums[0]))
    for num in nums[1:]:
        new_primes = Counter(iter_prime_factors(num))

        for prime, num_factors in common_primes.items():
            common_primes[prime] = min(num_factors, new_primes[prime])

        if not common_primes:
            break

    return product(common_primes.elements())


HEX_VALUE_MAP = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def hex_value(hex_string: str) -> int:
    """Find the int value of a hexadecimal string (equivalent to `int(hex_string, 16)`)"""
    rest, char = hex_string[:-1], hex_string[-1]
    value = HEX_VALUE_MAP[char.lower()]
    if not rest:
        return value
    else:
        return 16 * hex_value(rest) + value


def polygon_area(nodes: list[Coordinate]):
    """Find the area of the polygon enclosed by `coords`. NB: Since we only accept integer coordinates, we know that the result has to be an integer as well."""
    return (
        sum((y_1 + y_2) * (x_1 - x_2) for (y_1, x_1), (y_2, x_2) in pairwise(nodes))
        // 2
    )


@total_ordering
class Infinity(object):
    def __eq__(self, other):
        return isinstance(other, Infinity)

    def __gt__(self, other):
        return not isinstance(other, Infinity)


infinity = Infinity()


def defined_min(*args):
    return min(*args, key=lambda n: n if n or n == 0 else infinity)
