import re
import time


class OctopusArray:
    def __init__(self, input_string):
        self.array = [
            [int(n) for n in re.findall(r"\d", line)]
            for line in input_string.split("\n")
        ]

        self.height = len(self.array)
        self.width = len(self.array[0])

        self.num_flashes = 0

        if not all(len(row) == self.width for row in self.array):
            raise ValueError("Array is not rectangular")

    def _yield_neighbours(self, i, j):
        if i > 0:
            yield (i - 1, j)
        if i < self.height - 1:
            yield (i + 1, j)
        if j > 0:
            yield (i, j - 1)
        if j < self.width - 1:
            yield (i, j + 1)
        if i > 0 and j > 0:
            yield (i - 1, j - 1)
        if i > 0 and j < self.width - 1:
            yield (i - 1, j + 1)
        if i < self.height - 1 and j > 0:
            yield (i + 1, j - 1)
        if i < self.height - 1 and j < self.height - 1:
            yield (i + 1, j + 1)

    def __str__(self):
        return "\n".join(
            "".join(f"{self.array[i][j]}" for j in range(self.width))
            for i in range(self.height)
        )

    def _iter_indices(self):
        for i in range(self.height):
            for j in range(self.width):
                yield (i, j)

    def __iter__(self):
        for (i, j) in self._iter_indices():
            yield self[i][j]

    def __getitem__(self, item):
        return self.array[item]

    def perform_step(self):
        to_flash = []
        for (i, j) in self._iter_indices():
            self[i][j] += 1
            if self[i][j] > 9:
                to_flash.append((i, j))

        flashed = set()
        while to_flash:
            # Flash all charged octopuses
            for (i_flash, j_flash) in to_flash:
                for (i, j) in self._yield_neighbours(i_flash, j_flash):
                    self[i][j] += 1
                flashed.add((i_flash, j_flash))

            # Find all new octopuses that are fully charged
            to_flash = [
                (i, j)
                for (i, j) in self._iter_indices()
                if self[i][j] > 9 and (i, j) not in flashed
            ]

        # Record number of flashes
        self.num_flashes += len(flashed)

        # Set all values > 9 to zero
        for (i, j) in self._iter_indices():
            if self[i][j] > 9:
                self[i][j] = 0

    def perform_steps(self, num_steps: int):
        for _ in range(num_steps):
            self.perform_step()

    def animate(self, delay=0.1, num_steps=100):
        print(self, "\n")
        for _ in range(num_steps):
            time.sleep(delay)
            self.perform_step()
            print(self, "\n")
