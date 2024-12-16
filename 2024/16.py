from heapq import heappush, heappop
from typing import Set, Tuple, List

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
TURN_PENALTY = 1001

data = open('2024/d/16').read().strip().split('\n')
data = list(reversed(data))

def solve():
    """
    Finds the shortest path to 'E' and counts unique positions visited.
    Returns (shortest_distance, number_of_good_positions).
    """
    start_x, start_y = 1, 1
    frontier = [(0, start_x, start_y, 0, 1, {(start_x, start_y)})]
    best_length = None
    visited = set()  # includes visit direction
    on_shortest_path = set()

    while frontier:
        distance, x, y, current_dx, current_dy, path = heappop(frontier)
        
        if data[x][y] == 'E':
            if best_length is None:
                best_length = distance
                on_shortest_path = path
            elif distance == best_length:
                on_shortest_path.update(path)
            else:
                return best_length, len(on_shortest_path)
            continue

        visited.add((x, y, current_dx, current_dy))
        
        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            if data[next_x][next_y] != '#' and (next_x, next_y, dx, dy) not in visited:
                new_distance = distance + (TURN_PENALTY if (dx != current_dx or dy != current_dy) else 1)
                new_path = path.copy()
                new_path.add((next_x, next_y))
                heappush(frontier, (new_distance, next_x, next_y, dx, dy, new_path))

print(*solve())
