from pathlib import Path
from itertools import islice
from more_itertools import peekable


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def yield_binary_from_hex(hex_string):
    for char in hex_string:
        for bit in HEX_TO_BIN[char]:
            yield bit


def bin_to_int(bin_string) -> int:
    return sum(2**i for i, n in enumerate(reversed(list(bin_string))) if int(n))


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def parse_packet(binary_generator):
    version = bin_to_int(islice(binary_generator, 3))
    type_ID = bin_to_int(islice(binary_generator, 3))
    header = {"type_ID": type_ID, "version": version}

    if type_ID == 4:
        binary_string = ""
        group_header = next(binary_generator)
        while group_header == "1":
            for bit in islice(binary_generator, 4):
                binary_string += bit

            group_header = next(binary_generator)

        # Add last number (with group_header == "1")
        for bit in islice(binary_generator, 4):
            binary_string += bit

        return {**header, "value": bin_to_int(binary_string)}
    else:
        subpackets = []
        if next(binary_generator) == "0":

            total_subpacket_length = bin_to_int(islice(binary_generator, 15))
            binary_generator = peekable(
                islice(binary_generator, total_subpacket_length)
            )
            while binary_generator:
                subpackets.append(parse_packet(binary_generator))
        else:
            num_subpackets = bin_to_int(islice(binary_generator, 11))
            for _ in range(num_subpackets):
                subpackets.append(parse_packet(binary_generator))

        return {**header, "subpackets": subpackets}


def sum_versions(packet):
    current_version = packet["version"]
    if packet["type_ID"] == 4:
        return current_version
    else:
        return current_version + sum(
            sum_versions(subpacket) for subpacket in packet["subpackets"]
        )


def calculate_value(packet):
    subvalues = [calculate_value(value) for value in packet.get("subpackets", [])]
    match packet["type_ID"]:
        case 0:
            # return f"({' + '.join(subvalues)})"
            return sum(subvalues)
        case 1:
            # return f"({' * '.join(subvalues)})"
            product = 1
            for value in subvalues:
                product *= value
            return product
        case 2:
            # return f"min([{', '.join(subvalues)}])"
            return min(subvalues)
        case 3:
            # return f"max([{', '.join(subvalues)}])"
            return max(subvalues)
        case 4:
            # return str(packet["value"])
            return packet["value"]
        case 5:
            # return f"bool({subvalues[0]} > {subvalues[1]})"
            return int(subvalues[0] > subvalues[1])
        case 6:
            # return f"bool({subvalues[0]} < {subvalues[1]})"
            return int(subvalues[0] < subvalues[1])
        case 7:
            # return f"bool({subvalues[0]} == {subvalues[1]})"
            return int(subvalues[0] == subvalues[1])


def solve_a(hex_string=INPUT_STRING):
    binary_generator = yield_binary_from_hex(hex_string)
    packet = parse_packet(binary_generator)
    version_sum = sum_versions(packet)
    print("Sum of all versions:", version_sum)
    return version_sum


def solve_b(hex_string=INPUT_STRING):
    binary_generator = yield_binary_from_hex(hex_string)
    packet = parse_packet(binary_generator)
    value = calculate_value(packet)
    print("Final value:", value)
    return value


# final_answer = (
#     (18519 * bool(43 == 78927470))
#     + 2
#     + (1634 * bool(52320 < 1923994496))
#     + max([10, 107, 210, 9, 48781326955])
#     + 13
#     + 226
#     + (bool(315663 > 15396305) * 100)
#     + 474569
#     + (68 + 15 + 404636)
#     + (bool(2819168 < 32479852) * 1953)
#     + (191 * 55 * 212)
#     + (1037)
#     + 2156
#     + max([1505])
#     + 2381514313
#     + (bool(344095 < 234578) * 3383)
#     + 11
#     + ((7 * 3 * 11) + (13 * 11 * 10) + (3 * 7 * 7))
#     + (765 * bool(7 > 4399446759194))
#     + 946
#     + min([252])
#     + (bool(37028 < 37028) * 1)
#     + (bool((11 + 6 + 4) < (15 + 2 + 11)) * 378529)
#     + max(
#         [
#             max(
#                 [
#                     (
#                         (
#                             (
#                                 (
#                                     min(
#                                         [
#                                             max(
#                                                 [
#                                                     max(
#                                                         [
#                                                             (
#                                                                 (
#                                                                     min(
#                                                                         [
#                                                                             (
#                                                                                 max(
#                                                                                     [
#                                                                                         (
#                                                                                             max(
#                                                                                                 [
#                                                                                                     min(
#                                                                                                         [
#                                                                                                             min(
#                                                                                                                 [
#                                                                                                                     max(
#                                                                                                                         [
#                                                                                                                             (
#                                                                                                                                 53272880723
#                                                                                                                             )
#                                                                                                                         ]
#                                                                                                                     )
#                                                                                                                 ]
#                                                                                                             )
#                                                                                                         ]
#                                                                                                     )
#                                                                                                 ]
#                                                                                             )
#                                                                                         )
#                                                                                     ]
#                                                                                 )
#                                                                             )
#                                                                         ]
#                                                                     )
#                                                                 )
#                                                             )
#                                                         ]
#                                                     )
#                                                 ]
#                                             )
#                                         ]
#                                     )
#                                 )
#                             )
#                         )
#                     )
#                 ]
#             )
#         ]
#     )
#     + max([206576, 2963, 115])
#     + (250 * bool(1119 > 142))
#     + max([113083, 9388306])
#     + max([55153, 26407, 5510634, 39223780866])
#     + 1059
#     + min([205411, 29452, 49630, 104])
#     + (219 * 207)
#     + (bool((2 + 13 + 9) > (8 + 5 + 11)) * 79)
#     + (725 * bool(483456898762 < 39179))
#     + (106 * 81 * 68 * 173)
#     + (551 + 8976099 + 1003389 + 61934 + 2572)
#     + (bool((4 + 10 + 13) > (7 + 14 + 14)) * 136)
#     + (15632 * bool(148 < 148))
#     + (bool(20 == 20) * 44451124674)
#     + min([134, 6, 57, 11554, 701977])
#     + ((4 + 2 + 15) * (7 + 6 + 2) * (7 + 14 + 8))
#     + min([56652, 3])
#     + 214
#     + (2355355762 * bool(6033620 > 6033620))
#     + (231 * bool((2 + 5 + 8) == (14 + 15 + 13)))
#     + (20 * 70 * 95 * 217 * 183)
#     + min([8, 5, 2128])
#     + (49 * bool((14 + 15 + 9) < (11 + 5 + 10)))
#     + (bool(517089 > 4) * 255384586)
#     + (5272 + 10353 + 14 + 652926481)
#     + (173)
#     + (4129201436 * bool(1099842 == 504558))
#     + (208 * bool(149059958 > 149059958))
#     + (3433 + 10915953)
# )

if __name__ == "__main__":
    solve_a()
    solve_b()
