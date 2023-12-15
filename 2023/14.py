data = open('d/14').read().strip().splitlines()

data = [list(s) for s in data]


cycling = True


def cycle_one(d):
    tot = 0
    for row, line in enumerate(d):
        for col, el in enumerate(line):
            if el == 'O':
                d[row][col] = '.'
                r = row
                while r > 0 and d[r-1][col] == '.':
                    r -= 1
                d[r][col] = 'O'
                tot += len(d)-r
    return tot


def p(d):
    print('\n'.join(''.join(l) for l in d))


def cycle(d):
    # north
    cycle_one(d)

    # west
    d = [list(l) for l in zip(*d)]
    cycle_one(d)

    # south
    d = [list(l) for l in reversed(list(zip(*d)))]
    cycle_one(d)

    # east
    d = [list(l) for l in reversed(list(zip(*d)))]
    cycle_one(d)

    d = list(reversed([list(l) for l in zip(*reversed(d))]))

    val = 0
    for row, line in enumerate(d):
        for col, el in enumerate(line):
            if el == 'O':
                val += len(data)-row

    return d, val


seen = dict()
i = 0
while True:
    data, res = cycle(data)
    hash = '\n'.join(''.join(l) for l in data)
    # print(res)
    if hash in seen:
        first_seen = seen[hash]
        period = i - first_seen
        to_go = (1000000000-1 - first_seen) - period
        to_go %= period
        print(f"going extre {to_go}")
        for _ in range(to_go):
            data, res = cycle(data)
        break
    else:
        seen[hash] = i
    i += 1

print(res)
