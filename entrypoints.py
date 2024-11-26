import yaml
from pathlib import Path

ENTRYPOINTS_FILE = Path("entrypoints.yaml")


class Entrypoints:
    def __init__(self):
        with open(ENTRYPOINTS_FILE) as f:
            self.entrypoints = yaml.safe_load(f) or {}

    def __setitem__(self, name: tuple[int, int], value: str):
        year, day = name
        self.entrypoints[year] = self.entrypoints.get(year, {})
        self.entrypoints[year][day] = value

        with open(ENTRYPOINTS_FILE, "w") as f:
            yaml.safe_dump(self.entrypoints, f)

    def __getitem__(self, name: tuple[int, int]):
        year, day = name

        try:
            return self.entrypoints[year][day]
        except KeyError:
            raise KeyError(
                f"Module name for year {year} and day {day} does not exist yet"
            )


entrypoints = Entrypoints()
