import sys
sys.setrecursionlimit(10**6)

data = open('d/16').read().strip().splitlines()

nrows = len(data)
ncols = len(data[0])


def outside(r, c):
    return r < 0 or r >= nrows or c < 0 or c >= ncols


def compute(start_row, start_col, direction):
    left, right, up, down = set(), set(), set(), set()

    def light_right(r, c):
        c += 1
        if outside(r, c):
            return
        if (r, c) in right:
            return
        right.add((r, c))

        el = data[r][c]
        if el in '.-':
            light_right(r, c)

        if el in '\\|':
            light_down(r, c)

        if el in '/|':
            light_up(r, c)

    def light_left(r, c):
        c -= 1
        if outside(r, c):
            return
        if (r, c) in left:
            return
        left.add((r, c))

        el = data[r][c]
        if el in '.-':
            light_left(r, c)

        if el in '/|':
            light_down(r, c)

        if el in '\\|':
            light_up(r, c)

    def light_down(r, c):
        r += 1
        if outside(r, c):
            return
        if (r, c) in down:
            return
        down.add((r, c))
        el = data[r][c]
        if el in '.|':
            light_down(r, c)
        if el in '\\-':
            light_right(r, c)
        if el in '/-':
            light_left(r, c)

    def light_up(r, c):
        r -= 1
        if outside(r, c):
            return
        if (r, c) in up:
            return
        up.add((r, c))
        el = data[r][c]
        if el in '.|':
            light_up(r, c)
        if el in '/-':
            light_right(r, c)
        if el in '\\-':
            light_left(r, c)

    if direction == 'r':
        light_right(start_row, start_col)
    if direction == 'l':
        light_left(start_row, start_col)
    if direction == 'u':
        light_up(start_row, start_col)
    if direction == 'd':
        light_down(start_row, start_col)
    tot = 0
    for row in range(nrows):
        for col in range(ncols):
            if any((row, col) in v for v in [left, right, up, down]):
                tot += 1
    return tot


part2 = 0
for row in range(nrows):
    a = compute(row, -1, 'r')
    b = compute(row, ncols, 'l')
    part2 = max(part2, a, b)
for col in range(ncols):
    a = compute(-1, col, 'd')
    b = compute(nrows, col, 'u')
    part2 = max(part2, a, b)

print(compute(0, -1, 'r'), part2)
