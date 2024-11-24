import re

Lens = tuple[str, int]
Box = list[Lens]

RE_INSTRUCTION = re.compile(
    r"^(?P<label>.+)(?P<instruction_type>=|-)(?P<focal_length>\d?)$"
)


def parse_input(input_string: str):
    return input_string.split(",")


def holiday_ascii_string_helper(instruction: str):
    current_value = 0
    for ascii_value in instruction.encode("ascii"):
        current_value += ascii_value
        current_value *= 17
        current_value %= 256

    return current_value


def manual_arrangement_procedure(instructions: list[str]):
    boxes: list[Box] = [[] for _ in range(256)]

    for instruction in instructions:
        m = RE_INSTRUCTION.match(instruction).groupdict()
        label = m["label"]
        box_index = holiday_ascii_string_helper(label)
        current_box = boxes[box_index]

        lens_index = next(
            (i for i, lens in enumerate(current_box) if lens[0] == label), -1
        )

        match m["instruction_type"]:
            case "-":
                if lens_index >= 0:
                    current_box.pop(lens_index)
            case "=":
                focal_length = int(m["focal_length"])
                if lens_index == -1:
                    current_box.append((label, focal_length))
                else:
                    current_box[lens_index] = (label, focal_length)

    return boxes


def part_a(input_string: str):
    instructions = parse_input(input_string)

    return sum(holiday_ascii_string_helper(instruction) for instruction in instructions)


def part_b(input_string: str):
    instructions = parse_input(input_string)
    boxes = manual_arrangement_procedure(instructions)

    focusing_power = 0
    for box_num, box in enumerate(boxes, 1):
        for lens_num, (_, focal_length) in enumerate(box, 1):
            focusing_power += box_num * lens_num * focal_length

    return focusing_power
