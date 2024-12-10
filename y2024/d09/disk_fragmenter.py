Blocks = list[tuple[int | None, int]]


def parse_input(input_string: str):
    return [
        (None if i % 2 else i // 2, int(char)) for i, char in enumerate(input_string)
    ]


def find_next_empty_left(blocks: Blocks, current_value=0):
    while blocks[current_value][0] != None:
        current_value += 1

    return current_value


def find_next_available_left(blocks: Blocks, length: int):
    current_value = 0

    while (blocks[current_value][0] != None) or (blocks[current_value][1] < length):
        current_value += 1

    return current_value


def find_next_non_empty_right(blocks: Blocks, current_value=-1):
    while blocks[current_value][0] == None:
        current_value -= 1

    return current_value


def calculate_checksum(blocks: Blocks):
    checksum = 0
    pointer = 0
    for block_id, num_blocks in blocks:
        if block_id != None:
            checksum += block_id * sum(range(pointer, pointer + num_blocks))

        pointer += num_blocks

    return checksum


def move_block(blocks, left_pointer, right_pointer):
    num_empty = blocks[left_pointer][1]
    block_id, num_blocks = blocks[right_pointer]

    if num_empty == num_blocks:
        blocks[left_pointer] = (block_id, num_empty)
        blocks[right_pointer] = (None, num_blocks)
    elif num_empty > num_blocks:
        blocks[left_pointer] = (block_id, num_blocks)
        blocks[right_pointer] = (None, num_blocks)
        blocks.insert(left_pointer + 1, (None, num_empty - num_blocks))
    else:  # num_empty < num_blocks
        blocks[left_pointer] = (block_id, num_empty)
        blocks[right_pointer] = (block_id, num_blocks - num_empty)


def solve_a(input_string: str):
    blocks = parse_input(input_string)

    left_pointer = find_next_empty_left(blocks)
    right_pointer = find_next_non_empty_right(blocks)

    while left_pointer < (right_pointer % len(blocks)):
        move_block(blocks, left_pointer, right_pointer)

        left_pointer = find_next_empty_left(blocks, left_pointer)
        right_pointer = find_next_non_empty_right(blocks, right_pointer)

    return calculate_checksum(blocks)


def solve_b(input_string: str):
    blocks = parse_input(input_string)

    right_pointer = find_next_non_empty_right(blocks)

    while right_pointer > -1 * len(blocks):
        try:
            left_pointer = find_next_available_left(
                blocks, length=blocks[right_pointer][1]
            )

            if left_pointer >= (right_pointer % len(blocks)):
                raise IndexError
        except IndexError:
            right_pointer -= 1
        else:
            move_block(blocks, left_pointer, right_pointer)

        right_pointer = find_next_non_empty_right(blocks, right_pointer)

    return calculate_checksum(blocks)
