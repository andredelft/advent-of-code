from y2019.intcode import Intcode
import time

SPRINGSRIPT_A = """\
NOT C T
AND D T
OR T J
NOT B T
AND C T
OR T J
NOT A T
OR T J
WALK
"""


def solve_a(input_string: str):
    intcode = Intcode.parse_input(
        input_string, input_as_ascii=True, output_as_ascii=True
    )

    for block in intcode.run(SPRINGSRIPT_A).split("\n\n"):
        print(block)
        time.sleep(0.5)


SPRINGSRIPT_B = """\
NOT C T
AND D T
AND H T
OR T J
NOT B T
AND D T
OR T J
NOT A T
OR T J
RUN
"""


def solve_b(input_string: str):
    intcode = Intcode.parse_input(
        input_string, input_as_ascii=True, output_as_ascii=True
    )

    for block in intcode.run(SPRINGSRIPT_B).split("\n\n"):
        print(block)
        time.sleep(0.5)
