import re
from collections import defaultdict

orderings_raw, updates = open('d/05').read().split('\n\n')
orderings = defaultdict(list)
for a, b in re.findall(r'(\d+)\|(\d+)', orderings_raw):
    orderings[int(a)].append(int(b))
updates = [list(map(int, el.split(','))) for el in updates.splitlines()]

def bubble(upd):
    change = True
    while change:
        change = False
        for i in range(len(upd)-1):
            if upd[i] in orderings[upd[i+1]]:
                upd[i], upd[i+1] = upd[i+1], upd[i]
                change = True

part1, part2 = 0, 0

for u in updates:
    orig = list(u)  # copy
    bubble(u)
    mid = u[len(u)//2]
    if orig == u:
        part1 += mid
    else:
        part2 += mid

print(part1, part2)
