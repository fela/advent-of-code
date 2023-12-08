elves = open('d/01').read().split('\n\n')
vals = sorted(sum(int(i) for i in e.split()) for e in elves)
print(vals[-1], sum(vals[-3:]))
