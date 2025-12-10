import re


def _get_regex(include_negative):
    return r"-?\d+" if include_negative else r"\d+"


def parse_number(string: str, include_negative=False) -> int | None:
    """Searches for first occurence of a number in a given string, and returns it as an integer if found, and None otherwise."""
    re_num = _get_regex(include_negative)

    n = re.search(re_num, string)
    return int(n.group()) if n else None


def parse_numbers(string: str, include_negative=False, cast_as=list) -> list[int]:
    """Searches for all occurences of a number in a given string, and returns it as list of integers."""
    re_num = _get_regex(include_negative)

    return cast_as(int(n) for n in re.findall(re_num, string))


def is_num(string: str):
    return re.search(r"^\d+$", string)
