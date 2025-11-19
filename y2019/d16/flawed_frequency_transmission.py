from itertools import cycle, accumulate
from typing import Generator


def parse_input(input_string: str):
    return [int(n) for n in input_string]


def with_phase(func):
    def pattern_with_phase(period=1, phase=1) -> Generator[int]:
        generator = func(period)

        for _ in range(phase):
            next(generator)

        return generator

    return pattern_with_phase


@with_phase
def generate_pattern(period=1):
    for n in cycle([0, 1, 0, -1]):
        for _ in range(period):
            yield n


def flawed_frequency_transform(signal: list[int]):
    for i in range(len(signal)):
        N = sum(s * p for s, p in zip(signal, generate_pattern(i + 1)))

        yield ((-N) % 10) if N < 0 else N % 10


def solve_a(input_string: str):
    signal = parse_input(input_string)

    for _ in range(100):
        signal = list(flawed_frequency_transform(signal))

    return int("".join([str(n) for n in signal[:8]]))


def solve_b(input_string: str):
    input_string *= 10_000

    offset = int(input_string[:7])

    if not offset > len(input_string) // 2:
        raise ValueError("Can't be solved for this offset")

    signal_tail = reversed(parse_input((input_string)[offset:]))

    for _ in range(100):
        signal_tail = accumulate(signal_tail, lambda a, b: (a + b) % 10)

    return int("".join(str(n) for n in reversed(list(signal_tail)[-8:])))
