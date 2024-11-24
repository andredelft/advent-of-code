from enum import Enum
import re


class LineType(Enum):
    CD = "cd"
    LS = "ls"
    DIR = "dir"
    FILE = "file"


def parse_terminal_output(terminal_output: str):
    for line in terminal_output.split("\n"):
        m = re.search(r"^(\$ (?:cd|ls)|dir|\d+)\s*(.*)$", line)

        if not m:
            raise SyntaxError(f"Line not recognised")

        match m.group(1):
            case "$ cd":
                yield LineType.CD, m.group(2)
            case "$ ls":
                yield LineType.LS, None
            case "dir":
                yield LineType.DIR, m.group(2)
            case _:  # \d+
                yield LineType.FILE, [int(m.group(1)), m.group(2)]


class FileSystem(object):
    cpath = []
    filesystem = {}

    def _get_cdir(self):
        cdir = self.filesystem
        for dirname in self.cpath:
            cdir = cdir.get(dirname)

        return cdir

    def exists(self, name: str):
        cdir = self._get_cdir()
        return name in cdir.keys()

    def is_dir(self, name):
        cdir = self._get_cdir()
        return self.exists(name) and isinstance(cdir[name], dict)

    def is_file(self, name):
        cdir = self._get_cdir()
        return self.exists(name) and isinstance(cdir[name], int)

    def cd(self, dirname: str):
        match dirname:
            case "/":
                self.cpath = []
            case "..":
                self.cpath = self.cpath[:-1]
            case _:
                if self.is_dir(dirname):
                    self.cpath = [*self.cpath, dirname]

    def ls(self, quiet=False):
        cdir = self._get_cdir()

        if not quiet:
            for name, content in cdir.items():
                print(
                    f"{name: <10}{content if isinstance(content, int) else 'dir': >10}"
                )

        return list(cdir.keys())

    def add_dir(self, dirname: str):
        cdir = self._get_cdir()

        cdir[dirname] = {}

    def add_file(self, size: int, filename: str):
        cdir = self._get_cdir()

        cdir[filename] = size

    def _get_size_recursively(self, content) -> int:
        if isinstance(content, int):
            return content
        else:  # isinstance(content, dict)
            return sum(self._get_size_recursively(c) for c in content.values())

    def size(self, dirname: str):
        cdir = self._get_cdir()

        return self._get_size_recursively(cdir[dirname])

    def walk(self):
        cdir = self._get_cdir()
        for name, content in cdir.items():
            yield name

            if isinstance(content, dict):
                self.cd(name)
                for name in self.walk():
                    yield name
                self.cd("..")

    @classmethod
    def from_terminal_output(cls, input_string: str):
        input_stream = parse_terminal_output(input_string)

        fs = cls()
        try:
            line_type, data = next(input_stream)
            while True:
                match line_type:
                    case LineType.CD:
                        fs.cd(data)
                        line_type, data = next(input_stream)
                    case LineType.LS:
                        while True:
                            line_type, data = next(input_stream)
                            match line_type:
                                case LineType.DIR:
                                    fs.add_dir(data)
                                case LineType.FILE:
                                    fs.add_file(*data)
                                case _:
                                    break

        except StopIteration:
            fs.cd("/")
            return fs
