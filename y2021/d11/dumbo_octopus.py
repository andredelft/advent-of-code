from pathlib import Path
from octopus import OctopusArray


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def solve_a(input_string=INPUT_STRING):
    octopus_array = OctopusArray(input_string)
    # octopus_array.animate(num_steps=100)
    octopus_array.perform_steps(100)

    print(f"{octopus_array.num_flashes} number of flashes occured")
    return octopus_array.num_flashes


def solve_b(input_string=INPUT_STRING):
    octopus_array = OctopusArray(input_string)
    step_counter = 0
    while sum(octopus_array) != 0:
        octopus_array.perform_step()
        step_counter += 1

    print(f"Octopuses synchronized after {step_counter} steps")
    return step_counter


if __name__ == "__main__":
    solve_a()
    solve_b()
