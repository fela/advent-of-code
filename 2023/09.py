data = open('d/09').read().strip().splitlines()


def extrapolate(lst: list[int]) -> int:
    if all(i == lst[0] for i in lst):
        return lst[0]

    diffs = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
    return lst[-1] + extrapolate(diffs)


def solve(f):
    tot = 0
    for line in data:
        els = [int(s) for s in f(line.split())]
        tot += extrapolate(els)
    return tot


print(solve(list), solve(reversed))
