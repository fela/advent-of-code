from collections import Counter

data = open('d/01').read().splitlines()
l1, l2 = zip(*(map(int, el.split()) for el in data))
counts = Counter(l2)

print(
    sum(abs(x-y) for x, y in zip(sorted(l1), sorted(l2))),
    sum(counts[x]*x for x in l1)
)
