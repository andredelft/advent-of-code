from pathlib import Path
from brackets import check_syntax, IllegalCharacter, IncompleteLine, BRACKET_MAP

DAY_DIR = Path(__file__).parent

ILLEGAL_CHAR_VALUES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_CHAR_VALUES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    return input_string.split("\n")


def solve_a(input_string=INPUT_STRING):
    lines = parse_input(input_string)

    syntax_error_score = 0
    for line in lines:
        try:
            check_syntax(line)
        except IllegalCharacter as e:
            syntax_error_score += ILLEGAL_CHAR_VALUES[e.char]
        except IncompleteLine:
            pass
        else:
            raise SyntaxError("Syntax should be incorrect!")

    print(f"Syntax error score for illegal characters: {syntax_error_score}")

    return syntax_error_score


def solve_b(input_string=INPUT_STRING):
    lines = parse_input(input_string)

    syntax_error_scores = []
    for line in lines:
        try:
            check_syntax(line)
        except IllegalCharacter:
            pass
        except IncompleteLine as e:
            stack = list(e.stack)
            syntax_error_score = 0
            while stack:
                syntax_error_score *= 5
                syntax_error_score += INCOMPLETE_CHAR_VALUES[BRACKET_MAP[stack.pop()]]
            syntax_error_scores.append(syntax_error_score)
        else:
            raise SyntaxError("Syntax should be incorrect!")

    middle_syntax_error_score = sorted(syntax_error_scores)[
        len(syntax_error_scores) // 2
    ]

    print(f"Middle syntax error score: {middle_syntax_error_score}")

    return middle_syntax_error_score


if __name__ == "__main__":
    solve_a()
    solve_b()
