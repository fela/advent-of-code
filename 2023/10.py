data = open('d/10').read().strip().splitlines()

dirs = {
    'J': ([-1, 0], [0, -1]),
    'L': ([+1, 0], [0, -1]),
    '7': ([-1, 0], [0, +1]),
    'F': ([+1, 0], [0, +1]),
    '|': ([0, -1], [0, +1]),
    '-': ([-1, 0], [+1, 0]),
}


def connections(row, col):
    shape = data[row][col]
    if shape not in dirs:
        return []
    vals = [(row+dr, col+dc) for dc, dr in dirs[shape]]
    return vals


for r, l in enumerate(data):
    if 'S' in l:
        c = l.index('S')
        break

prev = None
dist = 0

visited = {(r, c)}

while prev is None or data[r][c] != 'S':
    dist += 1
    if prev is None:
        for rr in range(max(0, r-1), min(r+2, len(data))):
            for cc in range(max(0, c-1), min(c+2, len(data[0]))):
                conn = connections(rr, cc)
                if (r, c) in conn:
                    start = rr, cc
        prev = r, c
        r, c = start
        visited.add(start)
    else:
        conn = connections(r, c)
        prev, (r, c) = (r, c), conn[1 if conn[0] == prev else 0]
        visited.add((r, c))

inside_count = 0
for rr, line in enumerate(data):
    borders = 0
    last = 0
    for cc, el in enumerate(line):
        if (rr, cc) in visited:
            el = data[rr][cc]
            # hard-coding S might be different with different data
            if el in 'SLJ':
                if last == 1:
                    borders += 1
                last -= 1
                if last == -2:
                    last = 0
            elif el in 'F7':
                if last == -1:
                    borders += 1
                last += 1
                if last == 2:
                    last = 0
            elif el == '|':
                borders += 1
        else:
            inside_count += borders % 2

print(dist//2, inside_count)
