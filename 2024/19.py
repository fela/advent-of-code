inp = open('d/19').read().strip()

patterns, designs = inp.strip().split('\n\n')
patterns = [p.strip() for p in patterns.split(',')]
designs = designs.strip().split('\n')

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def build_trie(patterns):
    root = TrieNode()
    for pattern in patterns:
        node = root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    return root

trie = build_trie(patterns)

def build_design(design, trie):
    started_tries = [(trie, 1)]
    for c in design:
        next_tries = []
        ends_found = 0
        for t, n in started_tries:
            if c in t.children:
                next_tries.append((t.children[c], n))
                if t.children[c].is_end:
                    ends_found += n
        started_tries = next_tries
        if ends_found > 0:
            started_tries.append((trie, ends_found))
    return ends_found

options = [build_design(d, trie) for d in designs]

print(
    sum(o > 0 for o in options),
    sum(options),
)
