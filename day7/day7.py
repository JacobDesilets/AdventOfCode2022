from pathlib import Path


def main():
    infile = Path(__file__).with_name('day7.txt')
    with open(infile) as f:
        lines = f.readlines()
        root = Directory('/')
        all_dirs = parse_cli(root, lines)
        part1(all_dirs)
        part2(all_dirs)


def part1(dirs):
    target_dirs_total_size = 0
    MAX_SIZE = 100000
    for dir in dirs:
        size = dir.get_dir_size()
        if size <= MAX_SIZE:
            target_dirs_total_size += size

    print(f'Part 1: {target_dirs_total_size}')


def part2(dirs):
    TOTAL_SPACE = 70000000
    NEEDED_SPACE = 30000000

    root = dirs[0]
    assert(root.name == '/')

    unused_space = TOTAL_SPACE - root.get_dir_size()

    deletion_candidates = []
    for dir in dirs:
        dir_size = dir.get_dir_size()
        if unused_space + dir_size >= NEEDED_SPACE:
            deletion_candidates.append(dir)

    minimum_size_dir = min(deletion_candidates, key=lambda d: d.get_dir_size())

    print(f'Part 2: {minimum_size_dir.get_dir_size()}')


def parse_cli(root, lines):
    all_dirs = [root]
    active_dir = root
    is_ls = False
    for line in lines[1:]:  # Skip first line since we are already at root
        tokens = line.strip().split(' ')
        if tokens[0] == '$':  # Commands
            is_ls = False
            if tokens[1] == 'ls':
                is_ls = True
                continue
            elif tokens[1] == 'cd':
                dirname = tokens[2]
                if dirname == '..':
                    active_dir = active_dir.parent
                else:
                    for child in active_dir.children:
                        if child.name == dirname:
                            active_dir = child
        if is_ls:  # Should only get here if the last command was ls
            if tokens[0] == 'dir':
                new_dir = Directory(tokens[1])
                active_dir.add_child(new_dir)
                all_dirs.append(new_dir)
            else:
                new_file = File(tokens[1], int(tokens[0]))
                active_dir.add_child(new_file)

    return all_dirs


class File:
    def __init__(self, name, size):
        self.parent = None
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_dir_size(self):
        size = 0
        for child in self.children:
            if isinstance(child, File):
                size += child.size
            elif isinstance(child, Directory):
                size += child.get_dir_size()
        return size


if __name__ == '__main__':
    main()
