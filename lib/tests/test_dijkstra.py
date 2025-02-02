from lib.dijkstra import dijkstra
import pytest


@pytest.fixture
def nodes():
    return ["A", "B", "C", "D", "E"]


@pytest.fixture
def distances():
    return {
        ("A", "D"): 1,
        ("A", "B"): 6,
        ("B", "C"): 5,
        ("B", "D"): 2,
        ("B", "E"): 2,
        ("C", "E"): 5,
        ("D", "E"): 1,
    }


@pytest.fixture
def expected_path():
    return ["C", "E", "D", "A"]


def test_dijkstra(nodes, distances, expected_path):
    def get_neighbours(node):
        for neighbour in nodes:
            try:
                yield (neighbour, distances[tuple(sorted([node, neighbour]))])
            except KeyError:
                pass

    distance_map = dijkstra("A", "C", get_neighbours)

    assert list(distance_map.backtrace_path("C")) == expected_path


if __name__ == "__main__":
    test_dijkstra()
