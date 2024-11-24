from y2022.d07.file_system import FileSystem

TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def parse_input(input_string):
    return FileSystem.from_terminal_output(input_string)


def solve_a(input_string=TEST_INPUT):
    fs = parse_input(input_string)
    cumulative_size = 0
    for name in fs.walk():
        if fs.is_dir(name):
            size = fs.size(name)
            if size < 100_000:
                cumulative_size += size

    return cumulative_size


def solve_b(input_string=TEST_INPUT):
    fs = parse_input(input_string)
    used_space = sum(fs.size(name) for name in fs.ls(quiet=True))
    unused_space = 70_000_000 - used_space
    necessary_space = 30_000_000 - unused_space

    smallest_deletable_size = used_space
    for name in fs.walk():
        if fs.is_dir(name):
            size = fs.size(name)
            if size >= necessary_space and size < smallest_deletable_size:
                smallest_deletable_size = size

    return smallest_deletable_size
