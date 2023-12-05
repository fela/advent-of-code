import re

input_string = open('05.txt').read()
first_line, rest = input_string.split('\n', maxsplit=1)


def solve(part):
    seeds = list(int(s) for s in re.findall(r'(\d+)', first_line))
    current = []
    for i in range(0, len(seeds), 2):
        first, second = seeds[i:i+2]
        if part == 'first':
            current += [(first, first+1), (second, second+1)]
        else:
            current.append((first, first+second))

    for sec_from, sec_to, section in re.findall(r'(\w+)-to-(\w+) map:\n([\n\d ]+)', rest):
        prev = current.copy()
        current = []

        def add_ranges(map_start, map_end, diff):
            for prev_start, prev_end in prev:
                curr_start = max(prev_start, map_start)
                curr_end = min(map_end, prev_end)
                if curr_end > curr_start:
                    current.append((curr_start+diff, curr_end+diff))

        lowest_map = float('inf')
        highest_map = 0
        for m in re.findall(r'(\d+) (\d+) (\d+)', section):
            a, b, c = [int(s) for s in m]
            add_ranges(map_start=b, map_end=b+c, diff=a-b)
            lowest_map = min(lowest_map, b)
            highest_map = max(highest_map, b+c)

        add_ranges(map_start=0, map_end=lowest_map, diff=0)
        add_ranges(map_start=highest_map, map_end=max(el[1] for el in prev), diff=0)

    return min(current)[0]


print(solve('first'), solve('second'))
