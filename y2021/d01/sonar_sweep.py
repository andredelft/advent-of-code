from pathlib import Path

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    DEPTHS = [int(n) for n in f.read().split("\n") if n]


def solve_a(depths=DEPTHS):
    print(f"{len(depths)} measurements found")

    number_of_increments = 0

    for i in range(1, len(depths)):
        if depths[i - 1] < depths[i]:
            number_of_increments += 1

    print(f"{number_of_increments} number of increments found in the measurements")


def solve_b(depths=DEPTHS):
    print(f"{len(depths)} measurements found")

    number_of_increments = 0

    # It is a three window sum like this:
    #
    # 199  A
    # 200  A B
    # 208  A B C
    # 210    B C D
    # 200  E   C D
    # 207  E F   D
    # 240  E F G
    # 269    F G H
    # 260      G H
    # 263        H
    #
    # Since the last two numbers of A equal the first two numbers of B, we only need to compare the fist of A with the last of B

    for i in range(3, len(depths)):
        if depths[i - 3] < depths[i]:
            number_of_increments += 1

    print(
        f"{number_of_increments} number of three-window increments found in the measurements"
    )


if __name__ == "__main__":
    solve_a()
    solve_b()
