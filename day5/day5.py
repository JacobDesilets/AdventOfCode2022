from pathlib import Path


def main():
    infile = Path(__file__).with_name('day5.txt')
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


def part1(lines):
    stack_lines = lines[0:8]
    move_lines = lines[10:]
    stacks = get_stacks(stack_lines)

    for line in move_lines:
        amt, frm, to = parse_move(line)
        # print(f'move {amt} from {frm} to {to}')
        stacks = move_stack(amt, frm, to, stacks)

    output = ''
    for stack in stacks:
        output += stack[0]

    print(f'Part 1: {output}')


def part2(lines):
    stack_lines = lines[0:8]
    move_lines = lines[10:]
    stacks = get_stacks(stack_lines)

    for line in move_lines:
        amt, frm, to = parse_move(line)
        # print(f'move {amt} from {frm} to {to}')
        stacks = move_stack_pt2(amt, frm, to, stacks)

    output = ''
    for stack in stacks:
        output += stack[0]

    print(f'Part 2: {output}')


def parse_move(line):
    tokens = line.split(' ')
    return tokens[1], tokens[3], tokens[5].strip()


def move_stack(amt, frm, to, stacks):
    for i in range(0, int(amt)):
        item = stacks[int(frm)-1].pop(0)
        stacks[int(to)-1].insert(0, item)
    return stacks


def move_stack_pt2(amt, frm, to, stacks):
    amt, frm, to = int(amt), int(frm)-1, int(to)-1
    item = stacks[frm][:amt]
    stacks[frm] = stacks[frm][amt:]
    item.extend(stacks[to])
    stacks[to] = item
    return stacks


def get_stacks(lines):
    rows = []
    for line in lines:
        if line == ' 1   2   3   4   5   6   7   8   9\n':
            break
        row = []
        for i, j in enumerate(range(0, len(line), 4)):

            item = line[j:j + 4]
            if item == '    ':
                row.append('NONE')
            else:
                row.append(item[1])

        diff = 9 - len(row)
        for i in range(0, diff):
            row.append('NONE')
        rows.append(row)

    stacks = [[] for i in range(0, 9)]
    for row in rows:
        for i, item in enumerate(row):
            if item == 'NONE':
                continue
            else:
                stacks[i].append(item)

    return stacks


if __name__ == '__main__':
    main()
