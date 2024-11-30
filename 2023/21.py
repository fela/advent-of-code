import re
import math as m
from collections import Counter, defaultdict

data = open('d/21').read().strip().splitlines()
# data = '''
# ...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........
# '''.strip().splitlines()

rows, cols = len(data), len(data[0])

def get_start():
    for row, line in enumerate(data):
        for col, block in enumerate(line):
            if block == 'S':
                return row, col


def solve(n):
    reachable = {get_start()}
    for _ in range(n):
        new_reachable = set()
        for row, col in reachable:
            for new_row, new_col in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                if 0 <= new_row < rows and 0 <= new_col < cols and data[new_row][new_col] != '#':
                    new_reachable.add((new_row, new_col))
        reachable = new_reachable
        # print(len(reachable))
    # print(reachable)
    return len(reachable)


def solve2(n):
    reachable = {get_start()}
    counts = defaultdict(int)
    for _ in range(n):
        new_reachable = set()
        counts = defaultdict(int)
        for row, col in reachable:
            for new_row, new_col in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                if data[new_row%rows][new_col%cols] != '#':
                    if (new_row, new_col) not in new_reachable:
                        new_reachable.add((new_row, new_col))
                        counts[new_row//rows, new_col//cols] += 1
        reachable = new_reachable
        # print(len(reachable))
    # print(reachable)
    print(counts)
    for r in range(-10, 10):
        for c in range(0, 10):
            if (r, c) in counts:
                print(counts[r, c], end='  ')
        print()

    for r in range(-10, 10):
        for c in range(0, 10):
            if (r, -c) in counts:
                print(counts[r,-c], end='  ')
        print()
    assert sum(counts.values()) == len(reachable), (sum(counts.values()), len(reachable))
    return len(reachable)


def test():
    for steps, reach in [(6, 45), (200, 34482), (201, 34902), (300, 76706), (301, 77087)]:
        pass


def tri(n):
    return n*(n+1) // 2

# print(solve2(65+131*4))
full_blocks = 26501365 // 131
# full_blocks = (65+131*4) // 131
print(
    (927+921+949+941)*full_blocks +
    (6381+6356+6366+6383)*(full_blocks-1) +
    5482+5484+5474+5472 +
    7325*(tri(full_blocks)+tri(full_blocks-1)) +
    7265*(tri(full_blocks-1)+tri(full_blocks-2))
)

# assert 26501365 == full_blocks * 131 + 65

'''
5482  927  
7325  5472  
5474  921  

5482  949  
7325  5484  
5474  941  



5482  927  
7325  6381  927  
7265  7325  5472  
7325  6356  921  
5474  921  

5482  949  
7325  6366  949  
7265  7325  5484  
7325  6383  941  
5474  941  




5482  927  
7325  6381  927  
7265  7325  6381  927  
7325  7265  7325  5472  
7265  7325  6356  921  
7325  6356  921  
5474  921  

5482  949  
7325  6366  949  
7265  7325  6366  949  
7325  7265  7325  5484  
7265  7325  6383  941  
7325  6383  941  
5474  941  






5482  927  
7325  6381  927  
7265  7325  6381  927  
7325  7265  7325  6381  927  
7265  7325  7265  7325  5472  
7325  7265  7325  6356  921  
7265  7325  6356  921  
7325  6356  921  
5474  921  


5482  949  
7325  6366  949  
7265  7325  6366  949  
7325  7265  7325  6366  949  
7265  7325  7265  7325  5484  
7325  7265  7325  6383  941  
7265  7325  6383  941  
7325  6383  941  
5474  941  


295907
'''
