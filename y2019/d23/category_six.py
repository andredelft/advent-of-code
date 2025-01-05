from y2019.intcode import Intcode

from itertools import batched, cycle


def run_computers(intcode: Intcode, return_first_nat=False, return_duplicate_nat=False):
    computers = [intcode.copy() for _ in range(50)]

    for n, computer in enumerate(computers):
        computer.run(n)

    queues = [[] for _ in range(len(computers))]
    nat = None
    prev_nat_y = None

    while True:
        for i, computer in enumerate(computers):
            try:
                message = queues[i].pop(0)
            except IndexError:
                message = [-1]

            value = computers[i].run(*message)

            for address, *message in batched(value, 3):
                if address == 255:
                    nat = message

                    if return_first_nat:
                        return nat[1]
                else:
                    queues[address].append(message)

        if nat and all(len(queue) == 0 for queue in queues):
            if return_duplicate_nat and prev_nat_y == nat[1]:
                return nat[1]

            queues[0].append(nat)
            prev_nat_y = nat[1]


def solve_a(input_string: str):
    intcode = Intcode.parse_input(
        input_string, pause_on_input=True, output_as_array=True
    )

    return run_computers(intcode, return_first_nat=True)


def solve_b(input_string: str):
    intcode = Intcode.parse_input(
        input_string, pause_on_input=True, output_as_array=True
    )

    return run_computers(intcode, return_duplicate_nat=True)
