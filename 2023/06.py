import re
from math import floor, ceil

part1, part2 = [], []
for line in open('d/06').readlines():
    nums = re.findall(r'(\d+)', line)
    part1.append([int(s) for s in nums])
    part2.append([int(''.join(nums))])

def solve(data):
    prod = 1
    for t, d in zip(*data):
        first = floor((t - (t*t-4*d)**0.5)/2 + 1)
        last = ceil((t + (t*t-4*d)**0.5)/2 - 1)
        prod *= (last-first+1)
    return prod

print(solve(part1), solve(part2))
