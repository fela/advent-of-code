# A more minimalist solution

with open('01.txt') as f:
    data = f.readlines()


def solve(part):
    tot = 0
    for line in data:
        if part == 'second':
            for i, digit in enumerate('one two three four five six seven eight nine'.split()):
                line = line.replace(digit, f'{digit}{i+1}{digit}')
        digits = [c for c in line if c.isdigit()]
        tot += int(digits[0] + digits[-1])
    return tot


print(solve('first'))
print(solve('second'))
