from pathlib import Path
from path import PathTracker, PathTracker2


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    nodes = set()
    edges = dict()
    for line in input_string.split("\n"):
        edge = line.split("-")
        nodes.update(edge)

        for i in [0, 1]:
            edges[edge[i]] = edges.get(edge[i], []) + [edge[1 - i]]

    return edges


def solve_a(input_string=INPUT_STRING, PathClass=PathTracker):
    edges = parse_input(input_string)

    active_paths = [PathClass() + "start"]
    finished_paths = []
    stranded_paths = []

    while active_paths:
        path = active_paths.pop(0)

        new_paths = []
        for node in edges[path.current_node()]:
            if path.is_available(node):
                new_paths.append(path + node)

        if new_paths:
            for new_path in new_paths:
                if new_path.current_node() == "end":
                    finished_paths.append(new_path)
                else:
                    active_paths.append(new_path)
        else:
            stranded_paths.append(path)

    # print("Finished paths:", "\n".join(str(path) for path in finished_paths), sep="\n")
    # print("Stranded paths:", "\n".join(str(path) for path in stranded_paths), sep="\n")
    print(f"{len(finished_paths)} paths finished, {len(stranded_paths)} stranded")
    return len(finished_paths)


def solve_b(input_string=INPUT_STRING):
    return solve_a(input_string, PathClass=PathTracker2)


if __name__ == "__main__":
    solve_a()
    solve_b()
