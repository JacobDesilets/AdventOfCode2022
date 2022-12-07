from pathlib import Path


def main():
    infile = Path(__file__).with_name('day6.txt')
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


def part1(lines):
    line = lines[0]
    for i in range(4, len(line)+1):
        marker = line[i-4:i]
        if unique(marker):
            print(f'Part 1: {i}')
            break


def part2(lines):
    line = lines[0]
    for i in range(14, len(line) + 1):
        marker = line[i - 14:i]
        if unique(marker):
            print(f'Part 2: {i}')
            break


def unique(str):
    for c in str:
        count = 0
        for c2 in str:
            if c == c2:
                count += 1
        if count > 1:
            return False
    return True


if __name__ == '__main__':
    main()
