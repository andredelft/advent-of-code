from functools import total_ordering
from typing import Self
from lib.array import is_sorted


@total_ordering
class Page:
    def __init__(self, value: int, page_ordering_rules: set[tuple[int, int]]):
        self.value = value
        self.page_ordering_rules = page_ordering_rules

    def __eq__(self, other: Self):
        return not self.page_ordering_rules.intersection(
            [(self.value, other.value), (other.value, self.value)]
        )

    def __lt__(self, other: Self):
        return (self.value, other.value) in self.page_ordering_rules

    def __repr__(self):
        return str(self.value)


def parse_input(input_string: str):
    page_ordering_rules, updates = input_string.split("\n\n")

    page_ordering_rules = set(
        tuple(int(n) for n in line.split("|"))
        for line in page_ordering_rules.split("\n")
    )

    updates = [
        [Page(int(n), page_ordering_rules) for n in line.split(",")]
        for line in updates.split("\n")
    ]

    return updates


def get_middle_page_value(pages: list[Page], sort_pages=False):
    if sort_pages:
        pages.sort()

    return pages[len(pages) // 2].value


def solve_a(input_string: str):
    updates = parse_input(input_string)

    return sum(get_middle_page_value(pages) for pages in updates if is_sorted(pages))


def solve_b(input_string: str):
    updates = parse_input(input_string)

    return sum(
        get_middle_page_value(pages, sort_pages=True)
        for pages in updates
        if (not is_sorted(pages))
    )
