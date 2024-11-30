import re

data = open('d/18').read()

DIRS = {
    'D': (1, 0),
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

NEXT = {
    'R': 'D',
    'D': 'L',
    'L': 'U',
    'U': 'R',
}

dir_order = {
    (1, 0): 0,
    (0, -1): 1,
    (-1, 0): 2,
    (0, 1): 3,
}

DIRS_I = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def simplify3(s1, s2, s3):
    if s1[0][0] == -s2[0][0] and s1[0][1] == -s2[0][1]:
        area = min(s1[1], s2[1])
        if s1[1] == s2[1]:
            simplified = [s3]
        elif s1[1] > s2[1]:
            simplified = [(s1[0], s1[1]-s2[1]), s3]
        else:
            simplified = [(s2[0], s2[1]-s1[1]), s3]
    elif s3[0][0] == -s2[0][0] and s3[0][1] == -s2[0][1]:
        area = min(s3[1], s2[1])
        if s3[1] == s2[1]:
            simplified = [s1]
        elif s3[1] > s2[1]:
            simplified = [s1, (s3[0], s3[1]-s2[1])]
        else:
            simplified = [s1, (s2[0], s2[1]-s3[1])]
    elif s1[0] == s2[0]:
        area = 0
        simplified = [(s1[0], s1[1]+s2[1]), s3]
    elif s2[0] == s3[0]:
        area = 0
        simplified = [s1, (s2[0], s2[1]+s3[1])]
    elif s1[0][0] == -s3[0][0] and s1[0][1] == -s3[0][1]:  # opposing directions
        # assume clockwise so area is on the right
        is_negative = dir_order[s1[0]] == (dir_order[s2[0]]+1) % 4
        if s1[1] < s3[1]:
            simplified = [s2, (s3[0], s3[1]-s1[1])]
            if is_negative:
                area = -(s2[1]-1) * s1[1]
            else:
                area = (s2[1]+1) * s1[1]
        elif s1[1] == s3[1]:
            simplified = [s2]
            if is_negative:
                area = -(s2[1]-1) * s1[1]
            else:
                area = (s2[1]+1) * s1[1]
        else:
            simplified = [(s1[0], s1[1]-s3[1]), s2]

            if is_negative:
                area = -(s2[1]-1) * s3[1]
            else:
                area = (s2[1]+1) * s3[1]
    else:
        return None
    return simplified, area


def print_line(line):

    border = dict()
    row, col = 0, 0
    for (dr, dc), length in line:
        for _ in range(length):
            row += dr
            col += dc
            border[row, col] = True

    minr = min(r for r, _ in border.keys())
    minc = min(c for _, c in border.keys())
    new_border = {}
    n_rows = n_cols = 0
    for (r, c), v in border.items():
        r -= minr
        c -= minc
        new_border[r, c] = v

        n_rows = max(n_rows, r+1)
        n_cols = max(n_cols, c+1)
    border = new_border

    print()
    for r in range(n_rows):
        for c in range(n_cols):
            if (r, c) in border:
                print('#', end='')
            else:
                print('.', end='')
        print()


def compute(line):
    area = 0
    while len(line) > 4:
        best = None
        best_i = None
        best_l = None
        for i in range(len(line)-3):
            res = simplify3(*line[i:i+3])
            if res is None:
                continue
            if best_l is None or line[i+1] < best_l:
                best_l = line[i+1]
                best_i = i
                best = res

        area += best[1]
        line = line[:best_i] + best[0] + line[best_i+3:]

    return area + (line[0][1]+1)*(line[1][1]+1)


def part1():
    line = []
    for direction, length, color in re.findall(r'(\w)\s+(\d+) \(#(\w+)', data):
        line.append((DIRS[direction], int(length)))
    return compute(line)


def part2():
    line = []
    for _, _, len_hex, dir_i in re.findall(r'(\w)\s+(\d+) \(#(\w+)(\d)', data):
        line.append((DIRS_I[int(dir_i)], int(len_hex, base=16)))

    return compute(line)


print(part1(), part2())
