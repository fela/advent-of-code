from collections import Counter

data = open('d/01').read().splitlines()
l1, l2 = zip(*(map(int, el.split()) for el in data))

part1 = sum(abs(x-y) for x, y in zip(sorted(l1), sorted(l2)))

counts = Counter(l2)
part2 = sum(counts[x]*x for x in l1)

print(part1, part2)