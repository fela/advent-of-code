raw_grid, moves = open('d/15').read().split("\n\n")

conversion = {
    '#': ['#', '#'],
    '.': ['.', '.'],
    'O': ['[', ']'],
    '@': ['@', '.'],
}

directions = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0),
}

def move1(r, c, dr, dc, grid):
    if grid[r][c] == '#':
        return False
    if grid[r][c] == '.':
        return True
    if grid[r][c] in '@O':
        if move1(r + dr, c + dc, dr, dc, grid):
            grid[r+dr][c+dc] = grid[r][c]
            return True
        return False
    return False

def move2(r, c, dr, dc, grid):
    if grid[r][c] == '#':
        return False
    elif grid[r][c] == '.':
        return True
    elif grid[r][c] in '[]' and dc == 0:
        if grid[r][c] == ']':
            c -= 1
        backup = [list(row) for row in grid]
        if move2(r + dr, c, dr, dc, grid) and move2(r + dr, c+1, dr, dc, grid):
            grid[r+dr][c] = grid[r][c]
            grid[r+dr][c+1] = grid[r][c+1]
            grid[r][c] = '.'
            grid[r][c+1] = '.'
            return True
        grid[:] = backup
        return False
    elif grid[r][c] in '@[]':
        assert dr == 0 or grid[r][c] == '@'
        if move2(r + dr, c + dc, dr, dc, grid):
            grid[r+dr][c+dc] = grid[r][c]
            return True
        return False
    return False

def solve(part):
    grid = [list(l) for l in raw_grid.split("\n")]
    if part == 2:
        grid = [[c for char in row for c in conversion[char]] for row in grid]
    
    # find robot position
    robot = next((r, c) for r, row in enumerate(grid)
                 for c, val in enumerate(row) if val == '@')
    
    for m in moves:
        if m not in directions:
            continue  # newlines
        dr, dc = directions[m]
        r, c = robot
        move_fn = move2 if part == 2 else move1
        if move_fn(r, c, dr, dc, grid):
            robot = r + dr, c + dc
            grid[r][c] = '.'
    
    target = '[' if part == 2 else 'O'
    return sum(100 * r + c for r, row in enumerate(grid)
              for c, val in enumerate(row) if val == target)

print(solve(1), solve(2))
