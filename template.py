from pathlib import Path


def main():
    infile = Path(__file__).with_name('dayn.txt')
    with open(infile) as f:
        part1(f)

    with open(infile) as f:
        part2(f)


def part1(f):
    pass


def part2(f):
    pass


if __name__ == '__main__':
    main()
