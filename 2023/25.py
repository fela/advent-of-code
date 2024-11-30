import re
import math as m
from collections import Counter

data = open('d/25').read().strip()
# data = '''
# jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr
# '''.strip()

connections = []
elements = set()

for a, b in re.findall(r'(\w+):([\w ]+)', data):
    elements.add(a)
    for bb in b.split():
        elements.add(bb)
        connections.append((a, bb))

for e in elements:
    pass
    # print(e)
for x, y in connections:
    pass
    # print(x, y)

print(len(elements))