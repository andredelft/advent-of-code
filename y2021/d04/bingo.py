import re


def bingo_indices():
    for i in range(5):
        for j in range(5):
            yield (i, j)


WINNING_ROWS = [
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
    [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
    [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
    [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
    [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
    [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
    [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
]


class BingoBoard:
    def __init__(self, board_string: str):
        numbers = [int(n) for n in re.findall(r"\d+", board_string)]

        if len(numbers) != 25:
            raise ValueError(f"{len(numbers)} input values found, 25 expected")

        self.numbers = [numbers[i : i + 5] for i in range(0, 25, 5)]
        self.checked = [[False for _ in range(5)] for _ in range(5)]

    def __str__(self):
        return self.print_board()

    def __repr__(self):
        no_checked = 0

        for (i, j) in bingo_indices():
            no_checked += int(self.checked[i][j])

        return f"<BingoBoard ({no_checked} checked)>"

    def __iter__(self):
        for (i, j) in bingo_indices():
            yield self.numbers[i][j]

    def __getitem__(self, item):
        return self.numbers[item]

    def print_board(self):
        return "\n".join(
            " ".join(
                f"{self.numbers[i][j]:>2}" if not self.checked[i][j] else " X"
                for j in range(5)
            )
            for i in range(5)
        )

    def has_bingo(self) -> bool:
        for winning_row in WINNING_ROWS:
            if all(self.checked[i][j] for (i, j) in winning_row):
                return True

        return False

    def check(self, n):
        for (i, j) in bingo_indices():
            if self[i][j] == n:
                self.checked[i][j] = True

    def unmarked_sum(self):
        return sum(self[i][j] for (i, j) in bingo_indices() if not self.checked[i][j])
