data = open('d/15').read().strip().split(',')
hashmap = [[] for _ in range(256)]


def hash_func(string):
    curr = 0
    for c in string:
        curr = (curr + ord(c)) * 17 % 256
    return curr


part1 = 0
for el in data:
    part1 += hash_func(el)

    if '-' in el:
        label = el[:-1]
        lst = hashmap[hash_func(label)]
        hashmap[hash_func(label)] = [e for e in lst if e[0] != label]
    else:
        label = el[:-2]
        lens = el[-1]
        lst = hashmap[hash_func(label)]
        found = False
        for i, (l, v) in enumerate(lst):
            if l == label:
                found = True
                lst[i] = [l, lens]
        if not found:
            lst.append([label, lens])

part2 = 0
for i, box in enumerate(hashmap):
    for j, (_, v) in enumerate(box):
        part2 += (i+1)*(j+1)*int(v)

print(part1, part2)

