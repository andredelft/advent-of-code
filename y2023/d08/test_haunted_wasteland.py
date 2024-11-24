from y2023.d08.haunted_wasteland import solve_a, solve_b

TEST_INPUT_1 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT_2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT_3 = """\
LR

AAA = (AAB, XXX)
AAB = (XXX, AAZ)
AAZ = (AAB, XXX)
BBA = (BBB, XXX)
BBB = (BBC, BBC)
BBC = (BBZ, BBZ)
BBZ = (BBB, BBB)
XXX = (XXX, XXX)"""

EXPECTED_SOLUTION_A = 6
EXPECTED_SOLUTION_B = 6


def test_a():
    assert solve_a(TEST_INPUT_2) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT_3) == EXPECTED_SOLUTION_B
