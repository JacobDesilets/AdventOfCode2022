from pathlib import Path

def main():
    infile = Path(__file__).with_name('day3.txt')
    with open(infile) as f:
        part1(f)

    with open(infile) as f:
        part2(f)



def part1(f):
    sum = 0
    for line in f.readlines():
        l1 = line[:len(line)//2]
        l2 = line[len(line)//2:]
        common = find_common(l1, l2)
        priority = find_priority(common)
        sum += priority

    print(f'Part 1: {sum}')


def part2(f):
    sum = 0
    groups = []

    while True:
        g = [f.readline(), f.readline(), f.readline()]
        if '' in g:
            break
        groups.append(g)

    for group in groups:
        common = find_common_three(group[0].strip(), group[1].strip(), group[2].strip())
        priority = find_priority(common)
        sum += priority

    print(f'Part 2: {sum}')


def find_common(l1, l2):
    return list(set(l1).intersection(l2))[0]


def find_common_three(l1, l2, l3):
    return list(set(l1).intersection(l2, l3))[0]


def find_priority(char):
    try:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return alphabet.index(char) + 1
    except ValueError:
        print(f'Error on: "{char}"')


if __name__ == '__main__':
    main()
