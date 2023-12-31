import re, math

limits = {'red': 12, 'green': 13, 'blue': 14}
solution1, solution2 = 0, 0

for i, line in enumerate(open('d/02')):
    min_cubes = {k: 0 for k in limits}
    for num, color in re.findall(r'(\d+) (\w+)', line):
        min_cubes[color] = max(min_cubes[color], int(num))

    if all(min_cubes[color] <= limits[color] for color in limits):
        solution1 += i+1
    solution2 += math.prod(min_cubes.values())

print(solution1, solution2)
