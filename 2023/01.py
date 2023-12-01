import os
from typing import Optional

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


DIGITS = '1234567890'
DIGIT_NAMES = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEST1 = '''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
TEST2 = '''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''


def main():
    inp = puzzle_input()
    print(solve1(inp))
    print(solve2(inp))


def puzzle_input() -> list[str]:
    with open("01.txt", mode="r") as f:
        return f.read().strip().splitlines()


def solve1(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        digits = [i for i in line if i in DIGITS]
        tot += int(digits[0] + digits[-1])
    return tot


def solve2(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        tot += int(find_first_digit(line) + find_last_digit(line))
    return tot


def find_first_digit(line: str) -> str:
    for i in range(len(line)):
        if line[i] in DIGITS:
            return line[i]
        d = is_digit_name(line, i)
        if d is not None:
            return d

    raise ValueError('no digit found')


def find_last_digit(line: str) -> str:
    for i in range(len(line)-1, -1, -1):
        if line[i] in DIGITS:
            return line[i]
        d = is_digit_name(line, i)
        if d is not None:
            return d

    raise ValueError('no digit found')


def is_digit_name(line: str, idx: int) -> Optional[str]:
    """
    Returns the digit named at the given index,
    or None if there is no digit name at the given index.
    """
    for i, name in enumerate(DIGIT_NAMES):
        if line[idx:idx+len(name)] == name:
            return str(i+1)
    return None


def test():
    sol = solve1(TEST1.strip().splitlines())
    assert sol == 142, sol

    assert find_first_digit('twone') == '2'
    assert find_last_digit('twone') == '1'
    assert find_first_digit('one2') == '1'
    assert find_last_digit('one2') == '2'
    assert find_first_digit('1two') == '1'
    assert find_last_digit('1two') == '2'

    sol = solve2(TEST2.strip().splitlines())
    assert sol == 281, sol

    print('test successful!')


if __name__ == '__main__':
    test()
    main()
