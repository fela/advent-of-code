# A more minimalist solution

from math import prod

with open('02.txt') as f:
    data = f.readlines()

limits = {'red': 12, 'green': 13, 'blue': 14}


solution1 = 0
solution2 = 0
for i, line in enumerate(data):
    min_cubes = {k: 0 for k in limits}
    for draw in line.split(': ')[1].split('; '):
        for card in draw.split(', '):
            num, color = card.split()
            min_cubes[color] = max(min_cubes[color], int(num))

    if all(min_cubes[color] <= limits[color] for color in limits):
        solution1 += i+1
    solution2 += prod(min_cubes.values())

print(solution1, solution2)
