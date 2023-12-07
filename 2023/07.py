import re
from collections import Counter

data = open('07.txt').read()


def score(cards: str, part) -> int:
    jokers = cards.count('J')

    # transform in hex
    if part == 'second':
        cards = cards.replace('J', '1')
    for c, h in zip('AKQJT', 'EDCBA'):
        cards = cards.replace(c, h)
    value = int(cards, 16)

    # don't count Js as separate counts
    count_values = Counter(cards.replace('1', '')).values()
    if len(count_values) == 0:  # all jokers
        return 10**15
    max_count = max(count_values)
    for count in count_values:
        if part == 'second' and count == max_count:
            count += jokers
            max_count = -1
        value += 10**(10+count)
    return value


def solve(part):
    processed = [
        (score(c, part), int(b)) for i, (c, b) in
        enumerate(re.findall(r'(\w+)\s+(\d+)', data))
    ]

    return sum((i+1)*b for i, (_, b) in enumerate(sorted(processed)))


print(solve('first'), solve('second'))
