import re, math

data = [l.strip() for l in open('03.txt').readlines()]
rows, cols = len(data), len(data[0])

# Build data structure
numbers = []
pos_to_idx = {}
for row, line in enumerate(data):
    for match in re.finditer(r'\d+', line):
        numbers.append(int(match.group()))
        for col in range(match.start(), match.end()):
            pos_to_idx[row, col] = len(numbers)-1

def neighbors(row, col):
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if 0 <= r < rows and 0 <= c < cols:
                yield r, c

part1_indices = set()
part2 = 0
for row, line in enumerate(data):
    for col, char in enumerate(line):
        if not char.isdigit() and char != '.':
            indices = set()
            for r, c in neighbors(row, col):
                if (r, c) in pos_to_idx:
                    indices.add(pos_to_idx[r, c])
            if char == '*' and len(indices) == 2:
                part2 += math.prod(numbers[i] for i in indices)
            part1_indices.update(indices)

print(sum(numbers[i] for i in part1_indices), part2)
