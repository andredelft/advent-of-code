from pathlib import Path

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    CONTROLS = [line for line in f.read().split("\n") if line]


def process_control(line: str, x: int, y: int):
    control, n = line.split()

    match control:
        case "up":
            return x, y - int(n)
        case "down":
            return x, y + int(n)
        case "forward":
            return x + int(n), y
        case _:
            raise ValueError(f"Control '{control}' not recognized")


def solve_a(controls=CONTROLS):
    x, y = (0, 0)

    for line in controls:
        x, y = process_control(line, x, y)

    print(x * y)


def process_control_with_aim(line: str, aim: int, x: int, y: int):
    control, n = line.split()

    match control:
        case "up":
            return aim - int(n), x, y
        case "down":
            return aim + int(n), x, y
        case "forward":
            return aim, x + int(n), y + int(n) * aim
        case _:
            raise ValueError(f"Control '{control}' not recognized")


def solve_b(controls=CONTROLS):
    aim, x, y = (0, 0, 0)

    for line in controls:
        aim, x, y = process_control_with_aim(line, aim, x, y)

    print(x * y)


if __name__ == "__main__":
    solve_a()
    solve_b()
