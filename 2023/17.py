import heapq

data = open('d/17').read().strip().splitlines()

nrows = len(data)
ncols = len(data[0])


def last_segment(path):
    same_dir = []
    for d in reversed(path):
        if d == path[-1]:
            same_dir.append(d)
        else:
            break
    return tuple(same_dir)


def shortest_path(min_l, max_l):

    tentative = {}
    for row in range(nrows):
        for col in range(ncols):
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for reps in range(1, max_l+1):
                    tentative[row, col, tuple([dir]*reps)] = float('inf')

    pq = [(0, (0, 0), [])]
    while len(pq) > 0:
        dist, (r, c), path = heapq.heappop(pq)
        same_dir = last_segment(path)

        if len(path) > 0 and dist > tentative[r, c, same_dir]:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nbr = r+dr
            nbc = c+dc
            if nbr < 0 or nbr >= nrows or nbc < 0 or nbc >= ncols:
                continue
            if len(path) > 0 and dr == -path[-1][0] and dc == -path[-1][1]:
                continue
            nb_path = path + [(dr, dc)]
            segment_before = last_segment(path)
            segment = last_segment(nb_path)
            if len(segment) > max_l:
                continue
            if len(path) > 0 and len(segment_before) < min_l and len(segment) == 1:
                continue
            n_dist = dist + int(data[nbr][nbc])
            if n_dist < tentative[nbr, nbc, segment]:
                tentative[nbr, nbc, segment] = n_dist
                heapq.heappush(pq, (n_dist, (nbr, nbc), nb_path))

    best = float('inf')
    for (r, c, p), val in tentative.items():
        if (r, c) == (nrows-1, ncols-1):
            if len(last_segment(p)) >= min_l:
                best = min(best, val)
    return best


print(shortest_path(1, 3), shortest_path(4, 10))
