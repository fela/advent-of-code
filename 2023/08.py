import re
import numpy as np

data = open('d/08').read().strip()

dirs, rest = data.split('\n\n')
graph = {}

dirs = [0 if d == 'L' else 1 for d in dirs]
for a, b, c in re.findall(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', rest):
    graph[a] = b, c

starts = [v for v in graph if v.endswith('A')]
periods = []
for i, el in enumerate(starts):
    period = 0
    while True:
        for d in dirs:
            el = graph[el][d]
            period += 1
        if el.endswith('Z'):
            periods.append(period)
            break

print(periods[0], np.lcm.reduce(periods))
