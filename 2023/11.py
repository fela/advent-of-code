data = open('d/11').read().strip().splitlines()

empty_rows = [r for r, l in enumerate(data) if '#' not in l]
empty_cols = [c for c in range(len(data[0])) if all(d[c] != '#' for d in data)]


def solve(expansion):
    coords = []

    for r, line in enumerate(data):
        for c, el in enumerate(line):
            if el == '#':
                coords.append((
                    r + sum(el < r for el in empty_rows)*(expansion-1),
                    c + sum(el < c for el in empty_cols)*(expansion-1),
                ))

    tot = 0
    for galaxy1 in coords:
        for galaxy2 in coords:
            if galaxy1 < galaxy2:
                tot += abs(galaxy1[0] - galaxy2[0])
                tot += abs(galaxy1[1] - galaxy2[1])

    return tot


print(solve(2), solve(1000000))
