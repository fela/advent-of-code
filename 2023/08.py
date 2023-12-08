import re
import numpy as np

data = open('d/08').read().strip()

dirs, rest = data.split('\n\n')
graph = {}

for a, b, c in re.findall(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', rest):
    graph[a] = b, c

dirs = [0 if d == 'L' else 1 for d in dirs]


current = [v for v in graph if v.endswith('A')]

vals = []
for i, el in enumerate(current):
    val = 0
    while True:
        for d in dirs:
            el = graph[el][d]
            val += 1
        if el[2] == 'Z':
            vals.append(val)
            break

print(vals[0], np.lcm.reduce(vals))
