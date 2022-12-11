from pathlib import Path


def main():
    infile = Path(__file__).with_name('day10.txt')
    with open(infile) as f:
        lines = f.readlines()
        signals = gen_signals(lines)
        part1(signals)
        part2(signals)


def part1(signals):
    sum_sig_str = 0
    for i in range(20, 260, 40):
        sum_sig_str += (signals[i] * i)

    print(f'Part 1: {sum_sig_str}')


def part2(signals):
    crt = [''] * 40 * 6
    for c, X in signals.items():
        pos = (c-1) % 40
        if pos in [X-1, X, X+1]:
            crt[c-1] = '#'
        else:
            crt[c-1] = '.'

    for i in range(0, 260, 40):
        floor = 0 if i == 0 else i-40
        for char in crt[floor:i]:
            print(char, end='')
        print()


def gen_signals(lines):
    X = 1
    c = 0
    signals = {}
    for line in lines:
        line = line.strip().split(' ')
        instr = line[0]

        if instr == 'addx':
            c += 1
            signals[c] = X
            c += 1
            signals[c] = X
            X += int(line[1])
        elif instr == 'noop':
            c += 1
            signals[c] = X
    return signals


if __name__ == '__main__':
    main()
