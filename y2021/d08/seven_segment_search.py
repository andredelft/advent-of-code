from ast import Assert
from pathlib import Path
import re


# N: Number of digits that have N segments
NUM_SEGMENTS_COUNTER = {2: 1, 3: 1, 4: 1, 5: 3, 6: 3, 7: 1}


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_line(input_string):
    signal_patterns, coded_digits = (
        ["".join(sorted(set(n))) for n in re.findall(r"[a-g]+", digits)]
        for digits in input_string.split("|")
    )
    return signal_patterns, coded_digits


def solve_a(input_string=INPUT_STRING):
    unique_segment_numbers = []
    for line in input_string.split("\n"):
        _, coded_digits = parse_line(line)
        unique_segment_numbers += [d for d in coded_digits if len(d) in {2, 3, 4, 7}]

    num_unique_segment_numbers = len(unique_segment_numbers)
    print(f"{num_unique_segment_numbers} digits are a 1, 4, 7 or 8")
    return num_unique_segment_numbers


def solve_b(input_string=INPUT_STRING):
    sum_of_displays = 0
    for line in input_string.split("\n"):
        signal_patterns, coded_digits = parse_line(line)

        sp_by_length = {}
        for d in signal_patterns:
            num_segments = len(d)
            sp_by_length[num_segments] = sp_by_length.get(num_segments, []) + [d]

        # Check that the distribution of the number of segments matches what we expect
        assert {
            n: len(digits) for n, digits in sp_by_length.items()
        } == NUM_SEGMENTS_COUNTER

        # Start the algorithm to obtain the mapping of the signal patterns to their digit

        # We already know 1, 4, 7 and 8
        signal_patterns_map = {
            sp_by_length[2][0]: "1",
            sp_by_length[4][0]: "4",
            sp_by_length[3][0]: "7",
            sp_by_length[7][0]: "8",
        }

        # '3' is the 5-segment digit that has all the segments of '7'
        for i, digit in enumerate(sp_by_length[5]):
            if all((seg in digit) for seg in sp_by_length[3][0]):
                three = sp_by_length[5].pop(i)
                signal_patterns_map[three] = "3"
                break

        # '9' is the 6-segment digit that has all the segments of '4'
        for i, digit in enumerate(sp_by_length[6]):
            if all((seg in digit) for seg in sp_by_length[4][0]):
                nine = sp_by_length[6].pop(i)
                signal_patterns_map[nine] = "9"
                break

        # '0' is one of the unidentified 6-segment digits that has all the segments of '7'
        for i, digit in enumerate(sp_by_length[6]):
            if all((seg in digit) for seg in sp_by_length[3][0]):
                zero = sp_by_length[6].pop(i)
                signal_patterns_map[zero] = "0"
                break

        # The remaining 6-segment digit must be '6'
        signal_patterns_map[sp_by_length[6][0]] = "6"

        # '5' is one of the two unidentified 5-segment digits is contained in '9'
        for i, digit in enumerate(sp_by_length[5]):
            if all((seg in nine) for seg in digit):
                five = sp_by_length[5].pop(i)
                signal_patterns_map[five] = "5"
                break

        # The remaining 5-segment digit must be '2'
        signal_patterns_map[sp_by_length[5][0]] = "2"

        decoded_digits = "".join(signal_patterns_map[digit] for digit in coded_digits)

        sum_of_displays += int(decoded_digits)

    print(f"Sum of display numbers equals {sum_of_displays}")

    return sum_of_displays


if __name__ == "__main__":
    solve_a()
    solve_b()
