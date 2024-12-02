data = open('d/02').read().splitlines()

def check(vals):
    diffs = [x-y for x, y in zip(vals, vals[1:])]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def check_part2(vals):
    return any(check(vals[:i]+vals[i+1:]) for i in range(len(vals)))

part1, part2 = 0, 0
for i, el in enumerate(data):
    vals = [int(p) for p in el.split()]
    if check(vals):
        part1 += 1
    if check_part2(vals):
        part2 += 1

print(part1, part2)
