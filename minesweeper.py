# Request number of rows and columns
rows = int(input("Enter a number of rows for the grid: "))
cols = int(input("Enter a number of columns for the grid: "))
# Create a grid of dashes
minesweeper = [["-"] * cols for _ in range(rows)]
# Request the number of mines and their positions, place them in the grid
mine_num = int(input("Enter the number of mines you want to place: "))
for x in range(mine_num):
    row = int(input(f"Enter a row index to place the bomb from 0 to {rows - 1}: "))
    col = int(input(f"Enter a column index to place the bomb from 0 to {cols - 1}: "))
    minesweeper[row][col] = "#"
# Print the grid before modification
print("Input:")
for row in minesweeper:
    print(row)
# Iterate through nested loops 
for i in range(len(minesweeper)):
    for j in range(len(minesweeper[i])):
        # Perform checks for mines only for items with dashes
        if minesweeper[i][j] == "-":
            # for upper left corner
            if i == 0 and j == 0:
                bomb_counter = 0
                if minesweeper[i][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j+1] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for upper right corner
            if i == 0 and j == (len(minesweeper[i])-1):
                bomb_counter = 0
                if minesweeper[i][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j] == "#":    
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for middle parts
            if i < (len(minesweeper)-1) and j < (len(minesweeper[i])-1) and i > 0 and j > 0:
                bomb_counter = 0
                if minesweeper[i-1][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j+1] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for lower left corner
            if i == (len(minesweeper)-1) and j == 0:
                bomb_counter = 0
                if minesweeper[i-1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i][j+1] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for lower right corner
            if i == (len(minesweeper)-1) and j == (len(minesweeper[i])-1):
                bomb_counter = 0
                if minesweeper[i][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j] == "#":    
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for the first column (middle rows)
            if i < (len(minesweeper)-1) and i > 0 and j == 0:
                bomb_counter = 0
                if minesweeper[i-1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j+1] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for the last column (middle rows)
            if i < (len(minesweeper)-1) and i > 0 and j == (len(minesweeper[i])-1):
                bomb_counter = 0
                if minesweeper[i-1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # for the last row (middle columns)
            if i == (len(minesweeper)-1) and j > 0 and j < (len(minesweeper[i])-1):
                bomb_counter = 0
                if minesweeper[i][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i-1][j] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
            # Items in the first row (middle columns)
            if i == 0 and j > 0 and j < (len(minesweeper[i])-1):
                bomb_counter = 0
                if minesweeper[i][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j-1] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j] == "#":
                    bomb_counter += 1
                if minesweeper[i+1][j+1] == "#":
                    bomb_counter += 1
                if minesweeper[i][j+1] == "#":
                    bomb_counter += 1
                minesweeper[i][j] = str(bomb_counter)
print("Output:")
for row in minesweeper:
    print(row)
