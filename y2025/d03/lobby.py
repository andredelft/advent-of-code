def solve_a(input_string: str, num_digits=2):
    total_joltage = 0
    for numbers in input_string.split("\n"):
        num_dict: dict[int, list[int]] = {i: [] for i in range(10)}

        for i, n in enumerate(numbers):
            num_dict[int(n)].append(i)

        digits = []

        for nth_digit in range(num_digits):
            for n in reversed(range(10)):
                for i in num_dict[n]:
                    min_index = digits[-1] + 1 if len(digits) else 0
                    max_index = len(numbers) - num_digits + nth_digit

                    if min_index <= i <= max_index:
                        digits.append(i)
                        break

                if len(digits) == nth_digit + 1:
                    break

        total_joltage += int("".join(numbers[i] for i in digits))

    return total_joltage


def solve_b(input_string: str):
    return solve_a(input_string, 12)
