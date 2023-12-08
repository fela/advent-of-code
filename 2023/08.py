import re
import numpy as np

data = open('d/08').read().strip()

dirs, rest = data.split('\n\n')
map = {}

for a, b, c in re.findall(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', rest):
    map[a] = b, c

dirs = [0 if d == 'L' else 1 for d in dirs]


current = [v for v in map if v.endswith('A')]
s_to_i = {s: i for i, s in enumerate(map.keys())}

sets = [set() for _ in current]

vals = []
for i, el in enumerate(current):
    val = 0
    while True:
        for d in dirs:
            el = map[el][d]
            val += 1
        if el[2] == 'Z':
            vals.append(val)
            break

print(vals[0], np.lcm.reduce(vals))
