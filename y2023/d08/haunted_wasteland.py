import re
from itertools import cycle

from lib.math import lcm


def parse_input(input_string: str):
    instructions, lines = input_string.split("\n\n")

    nodes = [re.findall(r"[A-Z]{3}", line) for line in lines.split("\n")]

    node_map = {node: (left, right) for (node, left, right) in nodes}

    return (instructions, node_map)


def part_a(input_string: str):
    instructions, node_map = parse_input(input_string)
    current_node = "AAA"

    for num_steps, direction in enumerate(cycle(instructions), 1):
        left, right = node_map[current_node]

        match direction:
            case "L":
                current_node = left
            case "R":
                current_node = right

        if current_node == "ZZZ":
            break

    return num_steps


def part_b(input_string: str):
    instructions, node_map = parse_input(input_string)
    starting_nodes = [node for node in node_map.keys() if node[2] == "A"]

    num_rounds = []
    for node in starting_nodes:
        step_index = 0
        history = [list() for _ in instructions]

        # When the node has already been visited at the current `step_index`,
        # a cycle will be formed, which is already contained in the history.
        # Therefore we can stop traversing when this happens.
        while node not in history[step_index]:
            history[step_index].append(node)

            direction = instructions[step_index]
            left, right = node_map[node]

            match direction:
                case "L":
                    node = left
                case "R":
                    node = right

            step_index = (step_index + 1) % len(instructions)

        # Inspection of the history data reveals that each travling node:
        #
        # - Ends up at exactly one coordinate ending with 'Z' in its history
        #   when the loop has stopped.
        # - This coordinate is always reached at step_index = 0.
        # - Within the round it visits this coordinate, at a certain step, it
        #   visits a node it had already visited before on that step, thus
        #   forming a cycle.
        # - This previously visited node has always been visited on the first
        #   round. Hence the cycle length is always given by the number of
        #   rounds it has made. This is equal to `len(history[0]) - 1`.

        num_rounds.append(len(history[0]) - 1)

    # The minimal number of rounds required in order for all nodes to end up at
    # the coordinate ending with 'Z' is now given by the least common multiple
    # of these rounds. The number of steps is then given by multiplying this
    # number of rounds with the round length `len(instructions)`.

    return lcm(*num_rounds) * len(instructions)
