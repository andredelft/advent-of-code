from typing import Tuple, List
from bingo import BingoBoard
from pathlib import Path

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    BINGO_INPUT = f.read()


def parse_input(input_string=BINGO_INPUT) -> Tuple[int, List[BingoBoard]]:
    blocks = input_string.split("\n\n")
    numbers = [int(n) for n in blocks.pop(0).split(",")]
    boards = [BingoBoard(block) for block in blocks]
    return numbers, boards


def solve_a():
    numbers, boards = parse_input()

    for _ in range(4):
        n = numbers.pop(0)
        # We do the first four without checking, since no bingo is yet possible
        for board in boards:
            board.check(n)

    while not any(board.has_bingo() for board in boards):
        n = numbers.pop(0)
        for board in boards:
            board.check(n)

    winning_board_index, winning_board = next(
        (i, board) for (i, board) in enumerate(boards) if board.has_bingo()
    )

    print(f"Board {winning_board_index} won with number {n}:\n\n{winning_board}\n")

    print(f"Answer: {winning_board.unmarked_sum() * n}")


def solve_b():
    numbers, boards = parse_input()

    bingos = [False for _ in range(len(boards))]
    last_bingo_index = None

    for _ in range(4):
        n = numbers.pop(0)
        # We do the first four without checking, since no bingo is yet possible
        for board in boards:
            board.check(n)

    while not all(bingos):
        n = numbers.pop(0)
        for i, (board, bingo) in enumerate(zip(boards, bingos)):
            if not bingo:
                board.check(n)
                if board.has_bingo():
                    bingos[i] = True
                    last_bingo_index = i

    last_winning_board = boards[last_bingo_index]

    print(
        f"Board {last_bingo_index} had the last bingo with number {n}:\n\n{last_winning_board}\n"
    )

    print(f"Answer: {last_winning_board.unmarked_sum() * n}")


if __name__ == "__main__":
    solve_a()
    solve_b()
