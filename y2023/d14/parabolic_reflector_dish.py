from tqdm import tqdm
from itertools import count

from lib.field import Field


def solve_a(input_string: str):
    field = Field(input_string)

    load = 0
    current_roll_position = [0 for _ in range(field.width)]
    for (j, i), space in field.enumerate():
        match space:
            case "O":
                load += field.height - current_roll_position[i]
                current_roll_position[i] += 1
            case "#":
                current_roll_position[i] = j + 1

    return load


def tilt_and_rotate(field: Field):
    for _ in range(4):
        # Tilt
        current_roll_position = [0 for _ in range(field.width)]
        for (j, i), space in field.enumerate():
            match space:
                case "O":
                    field[j, i] = "."
                    field[current_roll_position[i], i] = "O"
                    current_roll_position[i] += 1
                case "#":
                    current_roll_position[i] = j + 1

        # Rotate
        field = Field(
            [
                [field[(field.height - 1) - i, j] for i in range(field.width)]
                for j in range(field.height)
            ]
        )

    return field


def get_load(field: Field):
    load = 0
    for j, row in enumerate(field.rows()):
        load += row.count("O") * (field.height - j)

    return load


def solve_b(input_string: str, N=1_000_000_000):
    field = Field(input_string)
    history: dict[Field, int] = dict()

    for n in tqdm(count(start=1), desc="Tilting and rotating"):
        # We build the new field from a copy to prevent mutations in the history
        # dictionary keys.
        field = tilt_and_rotate(field.copy())

        if field in history.keys():
            break
        else:
            history[field] = n

    # When the current state is already encountered in the history, the future
    # will become cyclical. We calculate the period of these cycles and extrapolate
    # to determine what the final state of the field will be after N steps.
    n_1 = history[field]
    n_2 = n

    period = n_2 - n_1
    rest = (N - n_1) % period

    final_state = next(field for field, n in history.items() if n == n_1 + rest)

    print(final_state)
    return get_load(final_state)
