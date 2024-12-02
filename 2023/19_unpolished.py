import re

import sys
sys.setrecursionlimit(10000)

data = open('d/19').read().strip()

workflows_str, shapes_str = data.split('\n\n')

workflows = {}
shapes = []

for line in shapes_str.splitlines():
    shapes.append({k: int(v) for k, v in re.findall(r'(\w)=(\d+)', line)})

for line in workflows_str.splitlines():
    name, description = re.match(r'(\w+){(.+)}', line).groups()
    parts = []
    workflows[name] = re.findall(r'(\w)(.)(\d+):(\w+)', description), description.split(',')[-1]


# def execute(range, items):
#     unknown = [range]
#     for sym, op, val, nxt in params:
#         if op == '>':
#             if shape[sym] > int(val):
#                 return nxt
#         if op == '<':
#             if shape[sym] < int(val):
#                 return nxt
#     return unknow, accepted


# def accept(sh):
#     curr = 'in'
#     while curr not in 'AR':
#         curr = execute(sh, workflows[curr])
#     return curr == 'A'

def num_accepted(ranges, workflow_name):
    if workflow_name == 'A':
        res = 1
        for k, r in ranges.items():
            for low, high in r:
                res *= high-low
        return res
    if workflow_name == 'R':
        return 0

    if any(len(r) == 0 for r in ranges.values()):
        return 0

    params, default = workflows[workflow_name]
    for sym, op, val, nxt in params:
        val = int(val)
        if op == '<':
            val -= 1
        lowest = min(l for l, _ in ranges[sym])
        highest = max(h-1 for _, h in ranges[sym])
        if lowest <= val < highest:
            ranges0 = ranges.copy()  # <= val
            ranges1 = ranges.copy()  # > val
            new0 = []
            new1 = []
            for l, h in ranges[sym]:
                if l > val:
                    new1.append((l, h))
                elif h-1 <= val:
                    new0.append((l, h))
                else:
                    new0.append((l, val+1))
                    new1.append((val+1, h))
            ranges0[sym] = new0
            ranges1[sym] = new1
            if op == '<':
                ranges0, ranges1 = ranges1, ranges0
            return num_accepted(ranges0, workflow_name) + num_accepted(ranges1, workflow_name)
        else:
            if op == '<':
                if any(l <= val for l, h in ranges[sym]):
                    assert all(h-1 <= val for l, h in ranges[sym])
                    return num_accepted(ranges, nxt)
            if op == '>':
                if any(h-1 > val for l, h in ranges[sym]):
                    assert all(l > val for l, h in ranges[sym])
                    return num_accepted(ranges, nxt)
    return num_accepted(ranges, default)


ranges = {v: [(1, 4001)] for v in 'xmas'}




# print(sum(sum(s.values()) for s in shapes if accept(s)))
# print(167409079868000)
print(num_accepted(ranges, 'in'))
