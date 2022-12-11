from pathlib import Path
from collections import namedtuple


def main():
    infile = Path(__file__).with_name('day9.txt')
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


def part1(lines):
    tail = Knot()
    head = Knot(child=tail)
    for line in lines:
        direction, distance = line.strip().split(' ')
        head.move(direction, distance)

    print(f'Part 1: {len(tail.visited)}')


def part2(lines):
    knots = [Knot() for _ in range(10)]
    for i in range(9):
        knots[i].child = knots[i+1]

    head = knots[0]
    tail = knots[9]
    for line in lines:
        direction, distance = line.strip().split(' ')
        head.move(direction, distance)

    print(f'Part 2: {len(tail.visited)}')


def sign(num):
    return 1 if num > 0 else -1


class Knot:
    def __init__(self, child=None):
        self.pos = (0, 0)
        self.child = child
        self.visited = {(0, 0)}

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    def add_pos(self, pos2):
        if isinstance(pos2, Knot):  # pos2 is a Knot
            self.pos = (self.x + pos2.x, self.y + pos2.y)
        else:  # pos2 is just a tuple
            self.pos = (self.x + pos2[0], self.y + pos2[1])

    def move(self, direction, distance):  # Should only be called on head knot
        directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        d = directions[direction]
        for _ in range(0, int(distance)):
            self.add_pos(d)
            self.child.follow(self)

    def follow(self, parent):
        child_move = (0, 0)
        dx = parent.x - self.x
        dy = parent.y - self.y

        if dy == 0 and abs(dx) == 2:
            child_move = (sign(dx), 0)
        elif dx == 0 and abs(dy) == 2:
            child_move = (0, sign(dy))
        elif (abs(dx) > 1 and abs(dy) >= 1) or (abs(dy) > 1 and abs(dx) >= 1):
            child_move = (sign(dx), sign(dy))

        self.add_pos(child_move)
        self.visited.add(self.pos)

        if self.child is not None:
            self.child.follow(self)


if __name__ == '__main__':
    main()
