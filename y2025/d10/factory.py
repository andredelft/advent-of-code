from collections import Counter
from lib.regex import parse_numbers
from lib.dijkstra import dijkstra
from itertools import chain, combinations_with_replacement


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        end_node, *buttons, joltage_requirements = line.split(" ")

        end_node = tuple((1 if char == "#" else 0) for char in end_node[1:-1])
        buttons = [parse_numbers(button, cast_as=set) for button in buttons]
        joltage_requirements = parse_numbers(joltage_requirements, cast_as=tuple)

        yield end_node, buttons, joltage_requirements


def get_neighbours(node, buttons):
    for button in buttons:
        yield tuple((1 - n if i in button else n) for i, n in enumerate(node)), 1


def solve_a(input_string: str):
    min_presses = 0

    for end_node, buttons, _ in parse_input(input_string):
        start_node = tuple(0 for _ in range(len(end_node)))

        distance_map = dijkstra(
            start_node, end_node, lambda n: get_neighbours(n, buttons)
        )

        min_presses += distance_map.get_distance(end_node)

    return min_presses


def get_indicator_neighbours(node, buttons, max_counters):
    # print(node)
    # time.sleep(0.05)
    for button in buttons:
        if not all(node[i] < max_counters[i] for i in button):
            continue

        max_presses = min(max_counters[i] - node[i] for i in button)
        # print(max_presses)
        for num_presses in range(1, max_presses + 1):
            yield tuple(
                (n + num_presses if i in button else n) for i, n in enumerate(node)
            ), num_presses

        # if not all(n <= m for n, m in zip(new_node, max_counters)):
        #     continue

        # yield new_node, 1


def get_configurations(
    buttons: list[set[int]],
    end_state: tuple[int, ...],
    locked_indices: set[int] = set(),
):
    print(end_state, locked_indices)
    for index, count in enumerate(end_state):
        if (index in locked_indices) or (count == 0):
            continue

        button_subset = [button for button in buttons if index in button]

        for button_presses in combinations_with_replacement(button_subset, count):
            c = Counter(chain.from_iterable(button_presses))

            if all(c[i] == n for i, n in enumerate(end_state)):
                yield c

            elif all(c[i] <= n for i, n in enumerate(end_state)):
                # print(locked_indices)
                locked_indices = locked_indices.union([index])
                new_end_state = tuple(n - c[i] for i, n in enumerate(end_state))

                for configuration in get_configurations(
                    buttons, new_end_state, locked_indices
                ):
                    yield c + configuration


def solve_b(input_string: str):
    min_presses = 0

    for _, buttons, end_state in parse_input(input_string):
        print(buttons, end_state)
        list(get_configurations(buttons, end_state))

        # buttons_considered = set()

        # for index, count in sorted(enumerate(end_state), key=lambda x: x[1]):
        #     button_subset = [i for i, button in enumerate(buttons) if index in button]

        #     buttons_considered.add(button_subset)

        #     if len(buttons_considered) == len(buttons):
        #         break

        # print(index, count, len(button_subset))

        # for button_presses in combinations_with_replacement(button_subset, count):
        #     c = Counter(chain(*button_presses))

        #     print([c[i] for i in range(len(end_state))])
        # if all(c[i] == n for i, n in enumerate(end_state)):
        #     print(c)

        ######

        # A = np.matrix(
        #     [[int(i in button) for i in range(len(end_node))] for button in buttons]
        # )
        # print(A)
        # return np.linalg.solve(A, end_node)

        ######

        # start_node = tuple(0 for _ in range(len(end_node)))

        # print(start_node, end_node)
        # return

        # distance_map = dijkstra(
        #     start_node,
        #     end_node,
        #     lambda n: get_indicator_neighbours(n, buttons, end_node),
        #     # silent=True,
        # )

        # min_presses += distance_map.get_distance(end_node)

    # return min_presses
