import os
from math import prod

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


TEST1 = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''


def main():
    inp = puzzle_input()
    print(solve1(inp))
    print(solve2(inp))


def puzzle_input() -> list[str]:
    with open("02.txt", mode="r") as f:
        return f.read().strip().splitlines()


def solve1(lines: list[str]) -> int:
    return sum(i+1 for i, line in enumerate(lines) if possible(line))


limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def possible(line: str) -> bool:
    for draw in line.split(': ')[1].split('; '):
        for card in draw.split(', '):
            num, color = card.split()
            if int(num) > limits[color]:
                return False
    return True


def solve2(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        min_cubes = {k: 0 for k in limits}
        for draw in line.split(': ')[1].split('; '):
            for card in draw.split(', '):
                num, color = card.split()
                min_cubes[color] = max(min_cubes[color], int(num))
        tot += prod(min_cubes.values())
    return tot


def test():
    sol = solve1(TEST1.strip().splitlines())
    assert sol == 8, sol

    sol = solve2(TEST1.strip().splitlines())
    assert sol == 2286, sol

    print('test successful!')


if __name__ == '__main__':
    test()
    main()
