# A more minimalist solution

with open('01.txt') as f:
    data = f.readlines()


def solve(second_part: bool):
    tot = 0
    for line in data:
        if second_part:
            for i, digit in enumerate('one two three four five six seven eight nine'.split()):
                line = line.replace(digit, f'{digit}{i+1}{digit}')
        digits = [i for i in line if i.isdigit()]
        tot += int(digits[0] + digits[-1])
    return tot


print(solve(False))
print(solve(True))
