from functools import total_ordering
from typing import TypeVar
from tqdm import tqdm

from lib.array import SortedList

Node = TypeVar("Node")


@total_ordering
class DistanceEntry(object):
    def __init__(self, distance: int, prev_node: Node):
        self.distance = distance
        self.prev_node = prev_node

    def __eq__(self, other):
        return self.prev_node == other.prev_node and self.distance == other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return f"({repr(self.prev_node)}, {repr(self.distance)})"


class DistanceMap(object):
    def __init__(self, start_node: Node):
        self.distance_map = {start_node: DistanceEntry(0, None)}

    def get_distance(self, node):
        distance_entry = self.distance_map.get(node)

        if not distance_entry:
            raise KeyError("No record exist of this node")

        return distance_entry.distance

    def nodes(self):
        return self.distance_map.keys()

    def add(self, node_from: Node, node_to: Node, distance: int):
        self.distance_map[node_to] = DistanceEntry(distance, node_from)

    def backtrace_path(self, node):
        current_node = node
        while current_node != None:
            yield current_node
            current_node = self.distance_map[current_node].prev_node


class NoPossiblePath(Exception):
    pass


def dijkstra(start_node: Node, end_node, get_neighbours, total_nodes: int = None):
    distance_map = DistanceMap(start_node)
    visited = {start_node}
    unvisited = SortedList([start_node], key=distance_map.get_distance)

    is_end_node = (
        lambda node: end_node(node) if callable(end_node) else end_node == node
    )

    current_node = start_node
    with tqdm(total=total_nodes, desc="Performing Dijkstra's algorithm") as pbar:
        while not is_end_node(current_node):
            try:
                current_node = unvisited.pop(0)
            except IndexError:
                raise NoPossiblePath("No path possible between start and end node")

            for neighbour, distance in get_neighbours(current_node):
                current_distance = distance_map.get_distance(current_node) + distance

                if neighbour in distance_map.nodes():
                    existing_distance = distance_map.get_distance(neighbour)

                    if existing_distance > current_distance:
                        neighbour_index = unvisited.find(neighbour)
                        unvisited.pop(neighbour_index)
                    else:
                        continue

                distance_map.add(current_node, neighbour, current_distance)
                unvisited.add(neighbour)

            visited.add(current_node)
            pbar.update()

    if callable(end_node):
        return distance_map, current_node

    return distance_map
