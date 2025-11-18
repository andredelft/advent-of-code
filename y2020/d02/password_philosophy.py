import re

RE_PASSWORD = re.compile("^(\d+)-(\d+) ([a-z]): ([a-z]+)$")


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        n1, n2, char, password = RE_PASSWORD.search(line).groups()

        yield int(n1), int(n2), char, password


def is_valid(n_min: int, n_max: int, char: str, password: str):
    return n_min <= len(re.findall(char, password)) <= n_max


def is_actually_valid(n1: int, n2: int, char: str, password: str):
    return sum([password[n1 - 1] == char, password[n2 - 1] == char]) == 1


def solve_a(input_string: str):
    return sum(is_valid(*args) for args in parse_input(input_string))


def solve_b(input_string: str):
    return sum(is_actually_valid(*args) for args in parse_input(input_string))
