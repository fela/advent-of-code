import re

data = open('d/12').read().strip().splitlines()


cache = {}
def arrangements(blocks: list[list], vals: list[int]) -> int:
    key = tuple(blocks), tuple(vals)
    if key not in cache:
        cache[key] = arrangements_(blocks, vals)
    return cache[key]


def arrangements_(blocks: list[list], vals: list[int]) -> int:
    # base cases
    if not vals:
        if any('#' in b for b in blocks):
            return 0
        else:
            return 1

    if not blocks:
        return 0

    tot = 0
    # ignore first '?'
    if blocks[0][0] == '?':
        blocks2 = blocks.copy()
        blocks2[0] = blocks2[0][1:]
        if not blocks2[0]:
            blocks2 = blocks2[1:]

        tot += arrangements(blocks2, vals)

    # use next element (will be either '?' or '#')
    if len(blocks[0]) == vals[0] or (len(blocks[0]) > vals[0] and blocks[0][vals[0]] == '?'):
        vals2 = vals[1:]

        blocks2 = blocks.copy()
        blocks2[0] = blocks2[0][vals[0]+1:]
        if not blocks2[0]:
            blocks2 = blocks2[1:]
        tot += arrangements(blocks2, vals2)

    return tot


def solve(duplications):
    res = 0
    for line in data:
        blocks, values = line.split()
        values = [int(s) for s in values.split(',')]

        blocks2 = re.split(r'\.+', '?'.join([blocks]*5))
        res += arrangements([b for b in blocks2 if b], values * 5)


print(solve(1), solve(5))
