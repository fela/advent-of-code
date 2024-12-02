data = open('d/02').read().splitlines()
data = [list(map(int, el.split())) for el in data]

def check(vals):
    diffs = [x-y for x, y in zip(vals, vals[1:])]
    return (
        all(1 <= d <= 3 for d in diffs) or 
        all(-3 <= d <= -1 for d in diffs)
    )

def check_part2(vals):
    return any(check(vals[:i]+vals[i+1:]) for i in range(len(vals)))

print(
    sum(check(v) for v in data), 
    sum(check_part2(v) for v in data)
)
