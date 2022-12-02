from pathlib import Path


def main():
    infile = Path(__file__).with_name('day2.txt')
    with open(infile) as f:
        total_score = 0
        for line in f.readlines():
            shapes = line.strip().split(' ')
            you = shapes[0]
            outcome = shapes[1]
            total_score += find_round_score(you, outcome)

        print(total_score)


def find_round_score(you, outcome):
    shapes = {'A': 1, 'X': 0, 'B': 2, 'Y': 3, 'C': 3, 'Z': 6}
    you = shapes[you]
    outcome = shapes[outcome]
    score = 0
    # Find the portion of the score based on the outcome
    score += outcome
    # Find the portion of the score based on what I played
    # I lose
    if outcome == 0:
        if you == 1:    score += 3  # I played scissors
        elif you == 2:  score += 1  # I played rock
        else:           score += 2  # I played paper
    # Draw
    elif outcome == 3:
        score += you  # I played whatever you played
    # I win
    elif outcome == 6:
        if you == 1:    score += 2  # I played paper
        elif you == 2:  score += 3  # I played scissors
        else:           score += 1  # I played rock

    return score


if __name__ == '__main__':
    main()
