from pathlib import Path


def main():
    infile = Path(__file__).with_name('day1.txt')

    elves = {}
    cals = 0
    elf_count = 1

    with open(infile) as f:
        for line in f.readlines():
            if line == '\n':
                elves[elf_count] = cals
                elf_count += 1
                cals = 0
                continue
            else:
                cals += int(line)

    max_cals = max(elves, key=elves.get)
    print(elves[max_cals])


if __name__ == '__main__':
    main()
