from y2019.intcode import Intcode
from itertools import permutations, cycle


def run_amplifiers(intcode: Intcode, phase_settings: list[int]):
    value = 0

    for phase_setting in phase_settings:
        value = intcode.run(phase_setting, value, reset=True)

    return value


def solve_a(input_string):
    num_amplifiers = 5
    intcode = Intcode.parse_input(input_string)
    max_value = 0

    for phase_settings in permutations(range(num_amplifiers), num_amplifiers):
        value = run_amplifiers(intcode, phase_settings)
        max_value = max(max_value, value)

    return max_value


def run_amplifiers_with_feedback(amplifiers: list[Intcode], phase_settings: list[int]):
    for amplifier, phase_setting in zip(amplifiers, phase_settings, strict=True):
        # Initial spin
        amplifier.run(phase_setting, pause_on_input=True)

    value = 0

    for i, amplifier in enumerate(cycle(amplifiers)):
        response = amplifier.run(value, pause_on_input=True)
        value = amplifier.value

        if i % len(amplifiers) == len(amplifiers) - 1 and response != None:
            break

    return value


def solve_b(input_string):
    num_amplifiers = 5
    amplifiers = [Intcode.parse_input(input_string) for _ in range(num_amplifiers)]

    max_value = 0

    for phase_settings in permutations(
        range(num_amplifiers, 2 * num_amplifiers), num_amplifiers
    ):
        value = run_amplifiers_with_feedback(amplifiers, phase_settings)
        max_value = max(value, max_value)
        for amplifier in amplifiers:
            amplifier.reset()

    return max_value
