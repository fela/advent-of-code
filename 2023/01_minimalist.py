# A more minimalist solution

data = open('02.txt').readlines()
digit_names = 'one two three four five six seven eight nine'.split()

def solve(part):
    tot = 0
    for line in data:
        if part == 'second':
            for i, name in enumerate(digit_names):
                line = line.replace(name, f'{name}{i+1}{name}')
        digits = [c for c in line if c.isdigit()]
        tot += int(digits[0] + digits[-1])
    return tot

print(solve('first'), solve('second'))
