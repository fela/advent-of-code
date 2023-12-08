data = open('d/03').read().strip()


def solve(part):
    tot = 0
    lines = data.splitlines()
    if part == 'first':
        rng = range(len(lines))
    else:
        rng = range(0, len(lines), 3)
    for i in rng:
        if part == 'first':
            line = lines[i]
            half = len(line) // 2
            c, = set(line[half:]) & set(line[:half])
        else:
            c, = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
        o = ord(c)
        if o > 96:
            o = o - ord('a') + 1
        else:
            o = o-ord('A') + 27
        tot += o
    return tot


print(solve('first'), solve('second'))
