from syntax_scoring import solve_a, solve_b

TEST_INPUT = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

PART_ONE_TEST_OUTPUT = 26397
PART_TWO_TEST_OUTPUT = 288957


def test_a():
    assert solve_a(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_b():
    assert solve_b(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_a()
    test_b()
