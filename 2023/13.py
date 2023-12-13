data = open('d/13').read().strip().split('\n\n')


def check_row(pattern: list[str], row: int) -> bool:
    for r1, r2 in zip(range(row, -1, -1), range(row+1, len(pattern))):
        if pattern[r1] != pattern[r2]:
            return False
    return True


def check_col(pattern: list[str], col: int) -> bool:
    for c1, c2 in zip(range(col, -1, -1), range(col+1, len(pattern[0]))):
        if any(l[c1] != l[c2] for l in pattern):
            return False
    return True


def reflection_line(pattern_raw: str, exclude: int = -1) -> int:
    pattern = pattern_raw.splitlines()
    for i in range(len(pattern) - 1):
        if check_row(pattern, i):
            val = (i+1)*100
            if val != exclude:
                return val

    for i in range(len(pattern[0]) - 1):
        if check_col(pattern, i):
            val = i+1
            if val != exclude:
                return val

    return -1


def reflection_fix(pattern_raw: str, exclude: int = -1) -> int:
    for i, char in enumerate(pattern_raw):
        if char in '.#':
            swap = '.' if char == '#' else '#'
            fix_attempt = pattern_raw[:i] + swap + pattern_raw[i + 1:]
            val = reflection_line(fix_attempt, exclude)
            if val != -1:
                return val
    raise ValueError("No solution")


part1 = 0
part2 = 0
for patt in data:
    reflection1 = reflection_line(patt)
    part1 += reflection1
    part2 += reflection_fix(patt, reflection1)


print(part1, part2)
