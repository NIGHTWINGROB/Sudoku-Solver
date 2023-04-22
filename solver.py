def solve_sudoku(grid):
    # Find the next empty cell
    row, col = find_empty_cell(grid)

    # If there are no more empty cells, we're done!
    if row is None:
        return True

    # Try filling the empty cell with numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            # If the move is valid, fill the cell and recurse
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            # If the recursive call fails, backtrack and try a different number
            grid[row][col] = 0

    # If we've tried all numbers and none of them work, the puzzle is unsolvable
    return False


def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def is_valid_move(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check sub-grid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[subgrid_row + i][subgrid_col + j] == num:
                return False

    # If all checks pass, the move is valid
    return True
