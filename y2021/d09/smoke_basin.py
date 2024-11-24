from pathlib import Path


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    return [[int(n) for n in line] for line in input_string.split("\n")]


def yield_neighbours(i, j, width, height):
    if i > 0:
        yield (i - 1, j)
    if i < height - 1:
        yield (i + 1, j)
    if j > 0:
        yield (i, j - 1)
    if j < width - 1:
        yield (i, j + 1)


def solve_a(input_string=INPUT_STRING):
    floor = parse_input(input_string)
    width, height = len(floor[0]), len(floor)

    low_points = []
    for i in range(height):
        for j in range(width):
            if all(
                floor[i][j] < floor[k][l]
                for (k, l) in yield_neighbours(i, j, width, height)
            ):
                low_points.append(floor[i][j])

    print(f"{len(low_points)} low points found")

    risk_level = len(low_points) + sum(low_points)

    print(f"Risk level: {risk_level}")

    return risk_level


def solve_b(input_string=INPUT_STRING):
    floor = parse_input(input_string)
    width, height = len(floor[0]), len(floor)

    basins = []
    current_basin = set()
    for i in range(height):
        for j in range(width):
            if floor[i][j] != 9:
                current_basin.add((i, j))
                basin_neighbours = list(
                    (k, l)
                    for k, l in yield_neighbours(i, j, width, height)
                    if floor[k][l] != 9
                )

                while basin_neighbours:
                    current_basin.update(basin_neighbours)
                    next_neighbours = []
                    for k, l in basin_neighbours:
                        next_neighbours += list(
                            (m, n)
                            for m, n in yield_neighbours(k, l, width, height)
                            if (m, n) not in current_basin and floor[m][n] != 9
                        )
                    basin_neighbours = next_neighbours

                # Basin found, fill up with 9's
                for k, l in current_basin:
                    floor[k][l] = 9

                basins.append(current_basin)
                current_basin = set()

    print(f"{len(basins)} basins found")
    basin_sizes = sorted(len(basin) for basin in basins)
    basin_product = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    print(basin_product)
    return basin_product


if __name__ == "__main__":
    solve_a()
    solve_b()
