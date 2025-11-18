import re
from functools import cache

RE_BAG_TYPE = re.compile(r"^[a-z]+ [a-z]+")
RE_CONTAINS = re.compile(r"(\d+) ([a-z]+ [a-z]+)")


def parse_input(input_string: str) -> dict[str, list[tuple[int, str]]]:
    return {
        RE_BAG_TYPE.search(line).group(): [
            (int(n), bag_type) for n, bag_type in RE_CONTAINS.findall(line)
        ]
        for line in input_string.split("\n")
    }


def solve_a(input_string: str):
    bag_dict = parse_input(input_string)

    @cache
    def contains_shiny_gold(bag_type: str):
        for _, contained_bag_type in bag_dict[bag_type]:
            if contained_bag_type == "shiny gold" or contains_shiny_gold(
                contained_bag_type
            ):
                return True

        return False

    return sum(contains_shiny_gold(bag_type) for bag_type in bag_dict.keys())


def solve_b(input_string: str):
    bag_dict = parse_input(input_string)

    @cache
    def num_contained_bags(bag_type: str):
        return sum(
            n + n * num_contained_bags(contained_bag_type)
            for (n, contained_bag_type) in bag_dict[bag_type]
        )

    return num_contained_bags("shiny gold")
