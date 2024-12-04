data = open('d/02').read().splitlines()
data = [list(map(int, el.split())) for el in data]

def safe(vals):
    diffs = [x-y for x, y in zip(vals, vals[1:])]
    return (
        all(1 <= d <= 3 for d in diffs) or 
        all(-3 <= d <= -1 for d in diffs)
    )

def safe_part2(vals):
    return any(check(vals[:i]+vals[i+1:]) for i in range(len(vals)))

print(
    sum(safe(v) for v in data), 
    sum(safe_part2(v) for v in data)
)
