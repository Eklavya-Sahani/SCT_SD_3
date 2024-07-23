def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0], l[1] = row, col
                return True
    return False

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    return num in [grid[row][col] for row in range(9)]

def used_in_box(grid, box_start_row, box_start_col, num):
    for row in range(3):
        for col in range(3):
            if grid[box_start_row + row][box_start_col + col] == num:
                return True
    return False

def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and \
           not used_in_col(grid, col, num) and \
           not used_in_box(grid, row - row % 3, col - col % 3, num)

def solve_sudoku(grid):
    l = [0, 0]
    if not find_empty_location(grid, l):
        return True

    row, col = l[0], l[1]
    
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

if __name__ == "__main__":
    # Input grid representing an unsolved Sudoku puzzle
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    print("Original Sudoku puzzle:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSolved Sudoku puzzle:")
        print_grid(grid)
    else:
        print("No solution exists")
