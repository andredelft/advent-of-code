class SyntaxException(Exception):
    pass


class IllegalCharacter(SyntaxException):
    def __init__(self, char, value=""):
        self.char = char
        super().__init__(value)


class IncompleteLine(SyntaxException):
    def __init__(self, stack, value=""):
        self.stack = stack
        super().__init__(value)


class UnknownCharacter(SyntaxException):
    def __init__(self, char, value=""):
        self.char = char
        super().__init__(value)


OPENING_BRACKETS = set("({[<")
CLOSING_BRACKETS = set(")}]>")

BRACKET_MAP = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


def check_syntax(line: str):
    stack = []
    for char in line:
        if char in OPENING_BRACKETS:
            stack.append(char)
        elif char in CLOSING_BRACKETS:
            expected_char = BRACKET_MAP[stack.pop()]
            if char != expected_char:
                raise IllegalCharacter(
                    char,
                    f"Expected '{expected_char}', but found '{char}' instead",
                )
        else:
            raise UnknownCharacter(char, f"Character {char} not part of the syntax")

    if stack:
        raise IncompleteLine(
            "".join(stack), "Line ended while some brackets are still open"
        )
