import re
data = open('d/03').read()

part1, part2 = 0, 0
enabled = True
for match in re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', data):
    x, y, do, dont = match
    if do:
        enabled = True
    elif dont:
        enabled = False
    else:
        part1 += int(x) * int(y)
        if enabled:
            part2 += int(x) * int(y)

print(part1, part2)
