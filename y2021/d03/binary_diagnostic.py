from pathlib import Path

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    BINARY_MATRIX = f.read().split("\n")

TEST_VALUE = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split(
    "\n"
)


def bin_to_dec(bin_num: str):
    """Converts an iterable of 1's and 0's (or truths and falsehoods) to its corresponding decimal number."""

    return sum(2**i for (i, n) in enumerate(reversed(list(bin_num))) if int(n))


def solve_a(binary_matrix=BINARY_MATRIX):
    column_length = len(binary_matrix)
    row_length = len(binary_matrix[0])

    column_sum = [
        sum(int(binary_matrix[i][j]) for i in range(column_length))
        for j in range(row_length)
    ]

    gamma_rate = bin_to_dec(n > (column_length / 2) for n in column_sum)
    # The gamma and epsilon rate are always each others opposite (bitwise flipped),
    # therefore gamma_rate + epsilon_rate = 111...1 = 2^(colum_length) - 1
    epsilon_rate = (2**row_length) - 1 - gamma_rate

    print(gamma_rate * epsilon_rate)


def solve_b(binary_matrix=BINARY_MATRIX):
    column_length = len(binary_matrix)
    row_length = len(binary_matrix[0])

    # Oxygen generator calculation
    binary_numbers = binary_matrix.copy()
    print(f"Starting with {len(binary_numbers)} binary numbers")

    bit_index = 0
    while len(binary_numbers) > 1:
        # We count the number of ones at index `bit_index` and return true (=1) if this is the majority or exactly half.
        # If it is false (=0) it thus means 0 is the majority.
        most_common_bit = int(
            sum(int(bin_num[bit_index]) for bin_num in binary_numbers)
            >= len(binary_numbers) / 2
        )

        print(f"Most common bit in position {bit_index}: {most_common_bit}")
        binary_numbers = [
            n for n in binary_numbers if int(n[bit_index]) == most_common_bit
        ]
        print(f"{len(binary_numbers)} remaining")

        bit_index += 1

    oxygen_generator_rating = bin_to_dec(binary_numbers[0])
    print(f"Oxygen generator rating found: {oxygen_generator_rating}")

    # CO2 generator calculation
    binary_numbers = binary_matrix.copy()
    print(f"Starting with {len(binary_numbers)} binary numbers")

    bit_index = 0
    while len(binary_numbers) > 1:
        # We count the number of ones at index `bit_index` and return true (=1) if this is the minority.
        # If it is false (=0) it thus means 0 is the minority or both are equal.
        least_common_bit = int(
            sum(int(bin_num[bit_index]) for bin_num in binary_numbers)
            < len(binary_numbers) / 2
        )

        print(f"Least common bit in position {bit_index}: {least_common_bit}")
        binary_numbers = [
            n for n in binary_numbers if int(n[bit_index]) == least_common_bit
        ]
        print(f"{len(binary_numbers)} remaining")

        bit_index += 1

    co2_generator_rating = bin_to_dec(binary_numbers[0])
    print(f"CO2 generator rating found: {co2_generator_rating}")

    print("Final answer", oxygen_generator_rating * co2_generator_rating)


if __name__ == "__main__":
    solve_b()
