from pathlib import Path


def main():
    infile = Path(__file__).with_name('day8.txt')
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


def part1(lines):
    forest = []
    for line in lines:
        forest.append([*(line.strip())])
    visible = count_visible(forest)
    print(f'Part 1: {visible}')


def part2(lines):
    forest = []
    for line in lines:
        forest.append([*(line.strip())])

    all_scores = []
    for i in range(0, len(forest)):
        for j in range(0, len(forest[0])):
            all_scores.append(calc_scenic_score(forest, i, j))

    max_scenic_score = max(all_scores)
    print(f'Part 2: {max_scenic_score}')


def count_visible(forest):
    border_count = 0
    visible_count = 0
    MAX_COL = len(forest) - 1
    MAX_ROW = len(forest[0]) - 1
    for i in range(0, len(forest)):
        for j in range(0, len(forest[0])):
            if i == 0 or i == MAX_COL or j == 0 or j == MAX_ROW:
                border_count += 1
            else:
                left = forest[i][:j]
                right = forest[i][j + 1:]
                top = [row[j] for row in forest[:i]]
                bottom = [row[j] for row in forest[i + 1:]]
                tree = int(forest[i][j])
                if (all(tree > int(x) for x in left)) or \
                        (all(tree > int(x) for x in right)) or \
                        (all(tree > int(x) for x in top)) or \
                        (all(tree > int(x) for x in bottom)):
                    visible_count += 1

    return border_count + visible_count


# Calculates the scenic score for a tree at forest[row][col]
def calc_scenic_score(forest, i, j):
    target_tree = int(forest[i][j])
    direction_scores = [0, 0, 0, 0]
    left = forest[i][:j]
    left.reverse()
    right = forest[i][j + 1:]
    top = [row[j] for row in forest[:i]]
    top.reverse()
    bottom = [row[j] for row in forest[i + 1:]]
    directions = [left, right, top, bottom]
    for i, direction in enumerate(directions):
        score = 1
        if not direction:
            direction_scores[i] = 0
            continue
        for tree in direction[:len(direction)-1]:
            if target_tree > int(tree):
                score += 1
            else:
                break
        direction_scores[i] = score

    total_score = direction_scores[0]
    for score in direction_scores[1:]:
        total_score *= score
    return total_score


if __name__ == '__main__':
    main()
