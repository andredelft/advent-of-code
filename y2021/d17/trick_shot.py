from pathlib import Path
import re
from tqdm import tqdm


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    x_min, x_max = [
        int(n) for n in re.search(r"x=(-?\d+)\.+(-?\d+)", input_string).groups()
    ]
    y_min, y_max = [
        int(n) for n in re.search(r"y=(-?\d+)\.+(-?\d+)", input_string).groups()
    ]

    return [x_min, x_max], [y_min, y_max]


def yield_path(v, y_min, start=[0, 0]):
    x, y = start.copy()
    yield (x, y)
    while y >= y_min:
        x += v[0]
        y += v[1]

        if v[0] > 0:
            v[0] -= 1
        elif v[0] < 0:
            v[0] += 1

        v[1] -= 1

        yield (x, y)


def draw_path(trajectory, target):
    delta_x_target, delta_y_target = target

    dimensions = [
        (0, 1 + max(delta_x_target[1], *[x for x, _ in trajectory])),
        (delta_y_target[0], 1 + max(delta_y_target[1], *[y for _, y in trajectory])),
    ]

    for y in reversed(range(*dimensions[1])):
        line = ""
        for x in range(*dimensions[0]):
            if (x, y) in trajectory:
                line += "#"
            elif (
                x >= delta_x_target[0]
                and x <= delta_x_target[1]
                and y >= delta_y_target[0]
                and y <= delta_y_target[1]
            ):
                line += "T"
            else:
                line += "."
        print(line)


def solve_a(input_string=INPUT_STRING):
    delta_x_target, delta_y_target = parse_input(input_string)
    v = [0, 0]
    v[1] = -delta_y_target[0] - 1
    v[0] = 1
    while sum(range(v[0] + 1)) < delta_x_target[1]:
        v[0] += 1
    v[0] -= 1
    initial_velocity = v.copy()
    trajectory = set(yield_path(v, delta_y_target[0]))
    draw_path(trajectory, (delta_x_target, delta_y_target))
    max_height = max(y for _, y in trajectory)
    print("Initial velocity:", initial_velocity)
    print("Max height:", max_height)
    return max_height


def solve_b(input_string=INPUT_STRING):
    delta_x_target, delta_y_target = parse_input(input_string)
    within_target = 0
    x_range = [0, delta_x_target[1] + 2]
    y_range = [delta_y_target[0], -delta_y_target[0]]
    with tqdm(
        total=(x_range[1] - x_range[0]) * (y_range[1] - y_range[0]),
        desc="Checking initial velocities",
    ) as pbar:
        for v_x in range(*x_range):
            for v_y in range(*y_range):
                trajectory = set(yield_path([v_x, v_y], delta_y_target[0]))
                if any(
                    (
                        x >= delta_x_target[0]
                        and x <= delta_x_target[1]
                        and y >= delta_y_target[0]
                        and y <= delta_y_target[1]
                    )
                    for x, y in trajectory
                ):
                    within_target += 1
                pbar.update(1)
    print("Number of initial velocities within target:", within_target)
    return within_target


if __name__ == "__main__":
    solve_a()
    solve_b()
