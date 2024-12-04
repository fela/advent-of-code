import re

data = open('d/04').read().strip().split('\n')
data_flipped = '\n'.join(''.join(x) for x in zip(*data))

data_shifted = [i*'x' + l + (len(data)-i)*'x' for i, l in enumerate(data)]
data_shifted_flipped = '\n'.join(''.join(x) for x in zip(*data_shifted))

data_reverse_shifted = [(len(data_shifted)-i)*'x' + l + i*'x' for i, l in enumerate(data)]
data_reverse_shifted_flipped = '\n'.join(''.join(x) for x in zip(*data_reverse_shifted))

part1 = 0
for match in ['XMAS', 'SAMX']:
    for d in ['_'.join(data), data_flipped, data_shifted_flipped, data_reverse_shifted_flipped]:
        part1 += len(re.findall(match, d))

def diag1(row, col):
    return data[row-1][col-1] + data[row][col] + data[row+1][col+1]

def diag2(row, col):
    return data[row-1][col+1] + data[row][col] + data[row+1][col-1]

part2 = 0
matches = ['MAS', 'SAM']
for row in range(1, len(data)-1):
    for col in range(1, len(data[0])-1):
        if diag1(row, col) in matches and diag2(row, col) in matches:
            part2 += 1
            
print(part1, part2)


