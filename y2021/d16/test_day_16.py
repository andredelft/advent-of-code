from packet_decoder import solve_a, solve_b

PART_ONE_TEST_INPUTS = [
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]
PART_TWO_TEST_INPUTS = [
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]

PART_ONE_TEST_OUTPUTS = [16, 12, 23, 31]
PART_TWO_TEST_OUTPUTS = [3, 54, 7, 9, 1, 0, 0, 1]


def test_a():
    for test_input, test_output in zip(PART_ONE_TEST_INPUTS, PART_ONE_TEST_OUTPUTS):
        assert solve_a(test_input) == test_output


def test_b():
    for test_input, test_output in zip(PART_TWO_TEST_INPUTS, PART_TWO_TEST_OUTPUTS):
        assert solve_b(test_input) == test_output


if __name__ == "__main__":
    test_a()
    test_b()
