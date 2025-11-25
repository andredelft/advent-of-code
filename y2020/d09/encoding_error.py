from itertools import combinations, accumulate


def parse_input(input_string: str):
    return [int(n) for n in input_string.split("\n")]


def first_invalid(numbers: list[int], N=25):
    i = N

    while True:
        if not any(a + b == numbers[i] for a, b in combinations(numbers[i - N : i], 2)):
            return i

        i += 1


def solve_a(input_string: str, N=25):
    numbers = parse_input(input_string)

    index = first_invalid(numbers, N)
    return numbers[index]


def solve_b(input_string: str, N=25):
    numbers = parse_input(input_string)

    index = first_invalid(numbers, N)
    expected_sum = numbers[index]

    for i in range(index):
        for j, contiguous_sum in enumerate(accumulate(numbers[i : index - 1])):
            if contiguous_sum == expected_sum:
                contiguous_range = numbers[i : i + j + 1]
                return min(contiguous_range) + max(contiguous_range)
