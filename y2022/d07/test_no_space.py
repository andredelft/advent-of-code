from y2022.d07.no_space import part_a, part_b

EXPECTED_SOLUTION_A = 95437
EXPECTED_SOLUTION_B = 24933642


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == EXPECTED_SOLUTION_B
