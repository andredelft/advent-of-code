from y2019.d02.program_alarm import part_a

TEST_INPUT = "1,9,10,3,2,3,11,0,99,30,40,50"

EXPECTED_SOLUTION_1 = 3500


def test_part_a():
    assert part_a(TEST_INPUT, restore_1202=False) == EXPECTED_SOLUTION_1


def test_part_b():
    print("No test is provided for part 2 in the exercise")
