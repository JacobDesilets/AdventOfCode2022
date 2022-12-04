from pathlib import Path


def main():
    infile = Path(__file__).with_name('day4.txt')
    with open(infile) as f:
        part1(f)

    with open(infile) as f:
        part2(f)


def part1(f):
    count = 0
    for line in f.readlines():
        line = line.strip()
        assignments = []
        for a in line.split(','):
            sections = a.split('-')
            assignments.append(Assignment(int(sections[0]), int(sections[1])))

        if (assignments[0].contains(assignments[1])) or (assignments[1].contains(assignments[0])):
            count += 1

    print(f'Part 1: {count}')


def part2(f):
    count = 0
    for line in f.readlines():
        line = line.strip()
        assignments = []
        for a in line.split(','):
            sections = a.split('-')
            assignments.append(Assignment(int(sections[0]), int(sections[1])))

        if assignments[0].overlaps(assignments[1]):
            count += 1

    print(f'Part 2: {count}')


class Assignment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'<{self.start}-{self.end}>'

    def contains(self, other):
        return (self.start <= other.start) and (self.end >= other.end)

    def overlaps(self, other):
        return (self.end >= other.start) and (self.start <= other.end)


if __name__ == '__main__':
    main()
