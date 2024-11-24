from y2022.d10.cathode_ray_tube import part_a, part_b

EXPECTED_SOLUTION_A = 13140
EXPECTED_SOLUTION_B = None


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == None
