data = open('d/02').read().strip().splitlines()


def solve(part):
    outcomes = {}
    for i, opponent in enumerate('ABC'):
        for j, you in enumerate('XYZ'):
            if part == 'second':
                j = (i+j-1) % 3
            score = (j-i+1) % 3 * 3
            outcomes[f'{opponent} {you}'] = score + j + 1
    return sum(outcomes[line] for line in data)


print(solve('first'), solve('second'))
