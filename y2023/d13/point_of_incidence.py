from lib.field import Field


def parse_input(input_string: str):
    return [Field(block) for block in input_string.split("\n\n")]


def off_by_one(line_1, line_2):
    element_is_off = False

    for el_1, el_2 in zip(line_1, line_2):
        if el_1 != el_2:
            if not element_is_off:
                element_is_off = True
            else:
                return False

    return element_is_off


def check_mirror(lines: list[str], index: int):
    for i, j in zip(reversed(range(index + 1)), range(index + 1, len(lines))):
        if lines[i] != lines[j]:
            return False

    return True


def check_mirror_with_smudge(lines: list[str], index: int):
    smudge_found = False
    for i, j in zip(reversed(range(index + 1)), range(index + 1, len(lines))):
        if lines[i] != lines[j]:
            if not smudge_found and off_by_one(lines[i], lines[j]):
                smudge_found = True
            else:
                return False

    return smudge_found


def solve_a(input_string: str):
    fields = parse_input(input_string)

    mirror_number = 0

    for field in fields:
        mirror = None
        for j in range(field.height - 1):
            if field.row(j) == field.row(j + 1):
                if check_mirror(list(field.rows()), j):
                    mirror = ("row", j)
                    break

        if not mirror:
            for i in range(field.width - 1):
                if field.col(i) == field.col(i + 1):
                    if check_mirror(list(field.cols()), i):
                        mirror = ("col", i)
                        break

        match mirror[0]:
            case "row":
                mirror_number += 100 * (mirror[1] + 1)
            case "col":
                mirror_number += mirror[1] + 1

    return mirror_number


def solve_b(input_string: str):
    fields = parse_input(input_string)

    mirror_number = 0

    for field in fields:
        mirror = None
        for j in range(field.height - 1):
            if field.row(j) == field.row(j + 1) or off_by_one(
                field.row(j), field.row(j + 1)
            ):
                if check_mirror_with_smudge(list(field.rows()), j):
                    mirror = ("row", j)
                    break

        if not mirror:
            for i in range(field.width - 1):
                if field.col(i) == field.col(i + 1) or off_by_one(
                    field.col(i), field.col(i + 1)
                ):
                    if check_mirror_with_smudge(list(field.cols()), i):
                        mirror = ("col", i)
                        break

        match mirror[0]:
            case "row":
                mirror_number += 100 * (mirror[1] + 1)
            case "col":
                mirror_number += mirror[1] + 1

    return mirror_number
