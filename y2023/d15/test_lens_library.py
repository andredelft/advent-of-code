from y2023.d15.lens_library import part_a, part_b

TEST_INPUT = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

EXPECTED_SOLUTION_A = 1320
EXPECTED_SOLUTION_B = 145


def test_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_B
