import re
import math as m
from collections import Counter

data = open('d/14').read().strip().split('\n')

width, height = 101, 103

def parse_robot(l):
    p, v = l.split(' v=')
    x, y = p.split(',')
    x = x.split('=')[1]
    vx, vy = v.split(',')
    return int(x), int(y), int(vx), int(vy)


def quadrant(x, y):
    if x > width//2 and y > height//2:
        return 0
    if x > width//2 and y < height//2:
        return 1
    if x < width//2 and y > height//2:
        return 2
    if x < width//2 and y < height//2:
        return 3
    return None

def final_quadrant(robot_line):
    x, y, px, py = parse_robot(robot_line)
    for _ in range(100):
        x = (x + px) % width
        y = (y + py) % height
    return quadrant(x, y)

def solve1():
    quadrants = Counter(final_quadrant(l) for l in data if l is not None)
    prod = 1
    for v in quadrants.values():
        prod *= v
    return prod

def solve2():
    robots = [parse_robot(l) for l in data]
    for i in range(10000):
        # all zeros matrix
        canvas = [[0 for _ in range(width)] for _ in range(height)]
        for x, y, px, py in robots:
            x = (x + px*i) % width
            y = (y + py*i) % height
            canvas[y][x] += 1

        neighbors = 0
        for x in range(width-1):
            for y in range(height-1):
                if canvas[y][x] == 0 and canvas[y+1][x]:
                    neighbors += 1
        if neighbors < 350:
            # for row in canvas:
            #     print(''.join(str(x) for x in row))
            return i

print(solve1(), solve2())
