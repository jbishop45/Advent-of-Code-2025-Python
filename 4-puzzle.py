with open('4-input.txt','r') as file:
    grid = [line.strip() for line in file if line.strip() != '']
    for row, line in enumerate(grid):
        grid[row] = [c for c in line]

def get_adjacent(grid, row, col, wrap=False, include_self=False):
    R = len(grid) - 1
    C = len(grid[0]) - 1
    adj = []
    if (row > 0) and (col > 0):
        adj.append(grid[row-1][col-1])
    if (row > 0):
        adj.append(grid[row-1][col])
    if (row > 0) and (col < C):
        adj.append(grid[row-1][col+1])

    if (col > 0):
        adj.append(grid[row][col-1])
    if include_self:
        adj.append(grid[row][col])
    if (col < C):
        adj.append(grid[row][col+1])

    if (row < R) and (col > 0):
        adj.append(grid[row+1][col-1])
    if (row < R):
        adj.append(grid[row+1][col])
    if (row < R) and (col < C):
        adj.append(grid[row+1][col+1])
    #print(adj)
    return adj

rolls = 0
continue_searching = True
recursive_search = True
while continue_searching:
    continue_searching = False
    for row, line in enumerate(grid):
        for col, _ in enumerate(line):
            if (get_adjacent(grid, row, col).count('@') < 4) and grid[row][col]=='@':
                rolls += 1
                if recursive_search:
                    grid[row][col] = '.'
                    continue_searching = True

print(rolls)