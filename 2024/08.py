from itertools import combinations
from collections import defaultdict

data = open('d/08').read().strip().split('\n')
antennas = defaultdict(list)
part1 = set()
part2 = set()

for r, l in enumerate(data):
    for c, ch in enumerate(l):
        if ch != '.':
            antennas[ch].append((r, c))

def in_range(r, c):
    return 0 <= r < len(data) and 0 <= c < len(data[0])

for lst in antennas.values():
    for (r0, c0), (r1, c1) in combinations(lst, 2):
        dr, dc = r1 - r0, c1 - c0
        for (r, c) in [(r0-dr, c0-dc), (r1+dr, c1+dc)]:
            if in_range(r, c):
                part1.add((r, c))
        for n in [2, 3, 5, 7]:
            while dr % n == 0 and dc % n == 0:
                dr //= n
                dc //= n
        r, c = r0, c0
        part2.add((r0, c0))
        while in_range(r + dr, c + dc):
            r, c = r + dr, c + dc
            part2.add((r, c))
        r, c = r0, c0
        while in_range(r - dr, c - dc):
            r, c = r - dr, c - dc
            part2.add((r, c))

print(len(part1), len(part2))
