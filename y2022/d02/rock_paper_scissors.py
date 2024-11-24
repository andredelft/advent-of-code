TEST_INPUT = """\
A Y
B X
C Z"""


def parse_input(input_string):
    return input_string.split("\n")


WINS = {"A Y", "B Z", "C X"}
DRAWS = {"A X", "B Y", "C Z"}
VALUES = {"X": 1, "Y": 2, "Z": 3}


def part_a(input_string=TEST_INPUT):
    matches = parse_input(input_string)
    score = 0
    for match in matches:
        score += VALUES[match[-1]]
        if match in WINS:
            score += 6
        elif match in DRAWS:
            score += 3
    return score


WIN = {"A": 2, "B": 3, "C": 1}
DRAW = {"A": 1, "B": 2, "C": 3}
LOSS = {"A": 3, "B": 1, "C": 2}


def part_b(input_string=TEST_INPUT):
    matches = [match.split(" ") for match in parse_input(input_string)]
    score = 0
    for opponent, outcome in matches:
        match outcome:
            case "X":  # Loss
                score += 0 + LOSS[opponent]
            case "Y":  # Draw
                score += 3 + DRAW[opponent]
            case "Z":  # Win
                score += 6 + WIN[opponent]

    return score
