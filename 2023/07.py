import re
from collections import Counter

data = open('d/07').read()


def score(cards: str, part) -> int:
    jokers = cards.count('J')

    # transform in hex
    if part == 'second':
        cards = cards.replace('J', '1')
    for c, h in zip('AKQJT', 'EDCBA'):
        cards = cards.replace(c, h)
    value = int(cards, 16)

    # counts excluding Js
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
    hands = re.findall(r'(\w+)\s+(\d+)', data)
    hands.sort(key=lambda c: score(c[0], part))

    return sum((i+1)*int(b) for i, (_, b) in enumerate(hands))


print(solve('first'), solve('second'))
