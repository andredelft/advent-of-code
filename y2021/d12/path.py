class NodeNotAvailable(Exception):
    pass


class PathTracker(object):
    def __init__(self, visited: set = set(), path: list[str] = []):
        self.visited = visited
        self.path = path

    def __repr__(self):
        return f"<Path: {self}>"

    def __str__(self):
        return ",".join(self.path) if self.path else "[]"

    def __add__(self, node: str):

        if not isinstance(node, str):
            raise TypeError("Only addition with strings is possible")

        new_path = PathTracker(self.visited.copy(), self.path.copy())
        new_path.add(node)
        return new_path

    def add(self, node):
        if self.is_available(node):
            self.visited.add(node)
            self.path.append(node)
        else:
            raise NodeNotAvailable("Node not available")

    def current_node(self):
        return self.path[-1] if self.path else None

    def is_available(self, node: str):
        return node.isupper() or node not in self.visited


class PathTracker2(PathTracker):
    def __init__(
        self,
        visited: dict[str, int] = dict(),
        path: list[str] = [],
        small_cave_double_visit: bool = False,
    ):
        self.visited = visited
        self.small_cave_double_visit = small_cave_double_visit
        self.path = path

    def is_available(self, node: str):
        num_visits = self.visited.get(node, 0)
        if node.isupper():
            return True
        elif node in ["start", "end"]:
            return num_visits == 0
        else:
            match num_visits:
                case 0:
                    return True
                case 1:
                    if self.small_cave_double_visit:
                        return False
                    else:
                        return True
                case _:
                    return False

    def __add__(self, node: str):

        if not isinstance(node, str):
            raise TypeError("Only addition with strings is possible")

        new_path = PathTracker2(
            self.visited.copy(), self.path.copy(), self.small_cave_double_visit
        )
        new_path.add(node)
        return new_path

    def add(self, node):
        if self.is_available(node):
            num_visits = self.visited.get(node, 0)

            if (
                num_visits == 1
                and not self.small_cave_double_visit
                and node.islower()
                and node not in ["start", "end"]
            ):
                self.small_cave_double_visit = True

            self.visited[node] = num_visits + 1
            self.path.append(node)
        else:
            raise NodeNotAvailable("Node not available")
