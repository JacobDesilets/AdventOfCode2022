from pathlib import Path


def main():
    infile = Path(__file__).with_name('day2.txt')
    with open(infile) as f:
        total_score = 0
        for line in f.readlines():
            shapes = line.strip().split(' ')
            you = shapes[0]
            me = shapes[1]
            total_score += find_round_score(you, me)

        print(total_score)


def find_round_score(you, me):
    shapes = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
    you = shapes[you]
    me = shapes[me]
    score = 0
    # Find the portion of the score based on what I played
    score += me
    # Find the portion of the score based on the outcome
    # draw
    if you == me:
        score += 3
    # I win
    elif (me == 1 and you == 3) or (me == 2 and you == 1) or (me == 3 and you == 2):
        score += 6
    # You win
    else:
        score += 0

    return score


if __name__ == '__main__':
    main()
