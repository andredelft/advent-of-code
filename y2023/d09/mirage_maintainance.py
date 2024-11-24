from lib.regex import parse_numbers


def get_diff_lists(sequence: list[int]):
    diff_lists = [sequence]

    while not all(n == 0 for n in diff_lists[-1]):
        last_diff_list = diff_lists[-1]
        new_diff_list = []

        for i in range(len(last_diff_list) - 1):
            new_diff_list.append(last_diff_list[i + 1] - last_diff_list[i])

        diff_lists.append(new_diff_list)

    return diff_lists


def parse_input(input_string: str):
    return [
        parse_numbers(line, include_negative=True) for line in input_string.split("\n")
    ]


def part_a(input_string: str):
    new_number_sum = 0

    for sequence in parse_input(input_string):
        diff_lists = get_diff_lists(sequence)
        new_number = sum(diff_list[-1] for diff_list in diff_lists)
        new_number_sum += new_number

    return new_number_sum


def part_b(input_string: str):
    new_number_sum = 0

    for sequence in parse_input(input_string):
        diff_lists = get_diff_lists(sequence)
        new_number = sum(
            (-1) ** n * diff_list[0] for n, diff_list in enumerate((diff_lists))
        )
        new_number_sum += new_number

    return new_number_sum
