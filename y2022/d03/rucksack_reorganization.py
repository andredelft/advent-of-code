TEST_INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def get_priority(char):
    if ord(char) >= ord("a"):
        return 1 + ord(char) - ord("a")
    else:
        return 27 + ord(char) - ord("A")


def parse_input(input_string):
    return input_string.split("\n")


def part_a(input_string=TEST_INPUT):
    rucksacks = parse_input(input_string)
    priority_sum = 0

    for rucksack in rucksacks:
        compartments = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
        overlap = set(compartments[0]).intersection(compartments[1])
        priority_sum += get_priority("".join(overlap))  # Should be only one char

    return priority_sum


def part_b(input_string=TEST_INPUT):
    rucksacks = parse_input(input_string)
    priority_sum = 0

    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i : i + 3]
        overlap = set(group[0]).intersection(group[1]).intersection(group[2])
        priority_sum += get_priority("".join(overlap))  # Again, should be only one char

    return priority_sum
