from collections import defaultdict

data = open('d/04').readlines()

part1, part2 = 0, 0
copies = defaultdict(lambda: 1)
for i, line in enumerate(data):
    winning, on_card = line.split(':')[1].split('|')
    winning = set(winning.strip().split())
    num = len(winning & set(on_card.strip().split()))
    if num > 0:
        part1 += 2**(num-1)
    for j in range(i+1, i+1+num):
        copies[j] = copies[j] + copies[i]
    part2 += copies[i]

print(part1, part2)
