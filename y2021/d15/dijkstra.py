from bisect import insort
from tqdm import tqdm


class DistanceEntry:
    def __init__(self, position, shortest_distance=None, prev_pos=None):
        self.position = position
        self.shortest_distance = shortest_distance
        self.prev_pos = prev_pos

    def __lt__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance < other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __le__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance <= other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __gt__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance > other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __ge__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance >= other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __eq__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance == other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __ne__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance != other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")


class DistanceTable:
    def __init__(self, positions):
        self._distance_table = {
            position: DistanceEntry(position) for position in positions
        }

        self._sorted_entries: list[DistanceEntry] = []

    def __getitem__(self, pos):
        return self._distance_table[pos]

    def yield_visited(self, pos):
        distance_entry = self._distance_table[pos]
        while distance_entry.prev_pos != None:
            yield distance_entry.prev_pos
            distance_entry = self._distance_table[distance_entry.prev_pos]

    def get_shortest_unvisited_distance(self, unvisited: set):
        index = next(
            i
            for i, entry in enumerate(self._sorted_entries)
            if entry.position in unvisited
        )
        return self._sorted_entries.pop(index)

    def set(self, pos, distance: int, prev_pos):
        self._distance_table[pos].shortest_distance = distance
        self._distance_table[pos].prev_pos = prev_pos

        insort(self._sorted_entries, self._distance_table[pos])


# Specific functions for pathfinding in an array


def _iterate_indices(height, length):
    for i in range(height):
        for j in range(length):
            yield (i, j)


def _yield_neighbours(position, height, length):
    i, j = position
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)
    if i < height - 1:
        yield (i + 1, j)
    if j < length - 1:
        yield (i, j + 1)


# Entrypoint function to find path in an array from initial_position
def dijkstra_array(array, initial_position):
    height, length = array.shape

    positions = list(_iterate_indices(height, length))

    current_position = initial_position

    distance_table = DistanceTable(positions=positions)
    distance_table.set(pos=current_position, distance=0, prev_pos=None)

    visited = set()
    unvisited = set(positions)

    with tqdm(total=len(positions), desc="Performing Dijkstra's algorithm") as pbar:
        # Dijkstra's algorithm: https://www.youtube.com/watch?v=pVfj6mxhdMw
        while unvisited:

            # Visit the unvisited vertex with the smallest known distance from the start vertex
            current_distance_entry = distance_table.get_shortest_unvisited_distance(
                unvisited
            )

            current_position = current_distance_entry.position
            current_distance = current_distance_entry.shortest_distance

            neighbours = list(_yield_neighbours(current_position, height, length))

            # For the current position, calculate the distance of each neighbour from the start position
            for neighbour in neighbours:
                dist_to_neighbour = current_distance + array[neighbour]
                if (
                    not distance_table[neighbour].shortest_distance
                    or distance_table[neighbour].shortest_distance > dist_to_neighbour
                ):
                    # Update values if we found a smaller position or none is yet defined
                    distance_table.set(
                        pos=neighbour,
                        distance=dist_to_neighbour,
                        prev_pos=current_position,
                    )

            visited.add(current_position)
            unvisited.remove(current_position)
            pbar.update(1)

    return distance_table
