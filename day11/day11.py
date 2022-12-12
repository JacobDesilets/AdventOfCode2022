from pathlib import Path


def main():
    infile = Path(__file__).with_name('day11.txt')
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


def part1(lines):
    monkeys = parse_monkeys(lines)
    for i in range(20):
        for monkey in monkeys:
            monkey.inspect()
            monkey.throw()

    monkeys.sort(key=lambda m: m.inspect_count, reverse=True)
    monkey_business = monkeys[0].inspect_count * monkeys[1].inspect_count
    print(f'Part 1: {monkey_business}')


def part2(lines):
    monkeys = parse_monkeys(lines, worry_divisor=1)
    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect()
            monkey.throw()

    monkeys.sort(key=lambda m: m.inspect_count, reverse=True)
    monkey_business = monkeys[0].inspect_count * monkeys[1].inspect_count
    print(f'Part 2: {monkey_business}')


def parse_monkeys(lines, worry_divisor=3):
    monkeys = []
    multiple = 1
    for i in range(0, 56, 7):
        line_items = lines[i + 1].strip().replace(' ', '')
        items = line_items.split(':')[1].split(',')
        items = [int(i) for i in items]

        line_op = lines[i + 2].strip()
        op = line_op[21:]

        line_div = lines[i + 3].strip()
        div = int(line_div[19:])
        multiple *= div

        line_true = lines[i + 4].strip()
        true = int(line_true[25:])

        line_false = lines[i + 5].strip()
        false = int(line_false[25:])

        monkeys.append(Monkey(items, op, div, true, false, worry_divisor=worry_divisor))

    for monkey in monkeys:
        monkey.monkey_list = monkeys
        monkey.multiple = multiple

    return monkeys


class Monkey:
    def __init__(self, items, operation, div_test, if_true, if_false, monkey_list=None, worry_divisor=3, multiple=None):
        self.items = items  # [int]
        self.operation = operation  # '{+ or *} {int or 'old'}'
        self.div_test = div_test  # int
        self.if_true = if_true  # int
        self.if_false = if_false  # int
        self.monkey_list = monkey_list  # [Monkey]
        self.inspect_count = 0
        self.worry_divisor = worry_divisor
        self.multiple = multiple

    def inspect(self):
        op_tokens = self.operation.split(' ')
        operator = op_tokens[0]
        operand = op_tokens[1]
        for i in range(len(self.items)):
            self.inspect_count += 1
            num = None
            if operand == 'old':
                num = self.items[i]
            else:
                num = int(operand)

            match operator:
                case '+':
                    self.items[i] += num
                case '*':
                    self.items[i] *= num

            self.items[i] = self.items[i] // self.worry_divisor
            self.items[i] %= self.multiple  # Modulo the number by the product of each divisible check (which are all
                                            # prime) won't affect the next divisibility check

    def throw(self):
        while True:
            if not self.items:
                break
            item = self.items.pop(0)
            if item % self.div_test == 0:
                self.monkey_list[self.if_true].catch(item)
            else:
                self.monkey_list[self.if_false].catch(item)

    def catch(self, item):
        self.items.append(item)


if __name__ == '__main__':
    main()
