with open('input4.txt') as f:
    grid = [[ch for ch in line.strip()] for line in f]

deltas = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

accessible_rolls = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '@':
            continue
        
        count = 0
        for row_dir, col_dir in deltas:
            new_row, new_col = row + row_dir, col + col_dir
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == '@':
                    count += 1
            
        if count < 4:
            accessible_rolls += 1

print('Part 1:', accessible_rolls)

accessible_rolls = 0
accessible = True
while accessible:
    new_grid = []
    for row in range(len(grid)):
        new_grid_row = []
        for col in range(len(grid[0])):
            if grid[row][col] != '@':
                new_grid_row.append('.')
                continue
            
            count = 0
            for row_dir, col_dir in deltas:
                new_row, new_col = row + row_dir, col + col_dir

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if grid[new_row][new_col] == '@':
                        count += 1
                
            if count < 4:
                accessible_rolls += 1
                new_grid_row.append('.')
            else:
                new_grid_row.append('@')

        new_grid.append(new_grid_row)
    
    if new_grid == grid:
        accessible = False
    grid = new_grid

print('Part 2:', accessible_rolls)
