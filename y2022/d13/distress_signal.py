TEST_INPUT = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, list):
        for item_a, item_b in zip(a, b):
            comparison = compare(item_a, item_b)
            if comparison:
                return comparison
        return compare(len(a), len(b))


def parse_input(input_string: str):
    for pair in input_string.split("\n\n"):
        yield [eval(line) for line in pair.split("\n")]


def part_a(input_string=TEST_INPUT):
    indices_sum = 0

    for i, pair in enumerate(parse_input(input_string), start=1):
        if compare(*pair) < 1:
            indices_sum += i

    return indices_sum


def part_b(input_string=TEST_INPUT):
    index_1 = 1
    index_2 = 2
    for pair in parse_input(input_string):
        for item in pair:
            if compare(item, [[2]]) == -1:
                index_1 += 1
                index_2 += 1
            elif compare(item, [[6]]) == -1:
                index_2 += 1

    return index_1 * index_2
