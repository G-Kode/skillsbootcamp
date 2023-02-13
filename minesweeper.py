# Open the input.txt file and split each row
with open('mines.txt', 'r') as f:
    grid = f.read().split('], ')

total_rows = len(grid) # Check the number of rows in the grid
total_columns = len(grid[0].split(',')) # Check the number of columns in the grid

# Create a blank minesweeper grid
grid_input = [[None] * total_columns for i in range(total_rows)]

# Create a 2d array from input data
# Iterate through the rows and columns with the enumerate function
# Save the x & y grid position as 'col'
for x, row in enumerate(grid):
    my_row = row.split(',')
    for y, col in enumerate(my_row):
        grid_input[x][y] = col

# Iterate through each row and column index using the enumerate function.
# If the position contains a '#', set the same position in the grid to '#'.
# If the position contains a '-', set the position to 0.
# Iterate through the surrounding rows and columns and check that indeces are within the boundaries.
# If the index is in bounds, check if it is a mine('#'). Increment the current position by 1.
# Finally, convert the numbers into strings and enter them into the grid.
for x, row in enumerate(grid_input):
    for y, col in enumerate(row):
        if col.find('#') != -1:
            grid_input[x][y] = '#'
        elif col.find('-') != -1:
            mines = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < total_rows and 0 <= j < total_columns:
                        if grid_input[i][j].find('#') != -1:
                            mines += 1
            grid_input[x][y] = str(mines)

# Ouutput each row, displaying the full grid.
for row in grid_input:
    print(row)