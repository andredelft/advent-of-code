from y2022.d10.cathode_ray_tube import solve_a, solve_b

EXPECTED_SOLUTION_A = 13140
EXPECTED_SOLUTION_B = None


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == None
