from pathlib import Path


def main():
    infile = Path(__file__).with_name('dayn.txt')
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


def part1(lines):
    pass


def part2(lines):
    pass


if __name__ == '__main__':
    main()
