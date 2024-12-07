data = open('d/06').read().split("\n")
data = [list(d) for d in data]

def compute_guard_pos():
    for r, d in enumerate(data):
        for c, dd in enumerate(d):
            if dd == '^':
                return r, c

guard_pos = compute_guard_pos()

next = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

def blocks_visited(data):
    # returns -1 if in a loop
    r, c = guard_pos
    dir_r, dir_c = -1, 0
    counts = 0
    visited = set()
    while 0 <= r+dir_r < len(data) and 0 <= c+dir_c < len(data[0]):
        if (r, c, dir_r, dir_c) in visited: 
            return -1
        visited.add((r, c, dir_r, dir_c))
        
        while data[r+dir_r][c+dir_c] == '#':
            dir_r, dir_c = next[dir_r, dir_c]
            if not(0 <= r+dir_r < len(data) and 0 <= c+dir_c < len(data[0])):
                return counts
        if data[r][c] != 'G':
            data[r][c] = 'G'
            counts += 1
        r, c = r+dir_r, c+dir_c
    return counts

def part2():
    loops = 0
    for r in range(len(data)):
        print(f"{r}/{len(data)}\r", end='')
        for c in range(len(data[0])):
            if data[r][c] == '^':
                continue
            new_data = [list(d) for d in data]
            if new_data[r][c] != '#':
                new_data[r][c] = '#'
                if blocks_visited(new_data) == -1:
                    loops += 1
    return loops

print(blocks_visited(data), part2())
