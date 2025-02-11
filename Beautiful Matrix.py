# Initialize the matrix
matrix = [list(map(int, input().split())) for _ in range(5)]

# Find the position of the single '1'
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row, col = i, j
            break

# Calculate the number of moves needed
# Rows: Move the '1' to row 2 (since Python uses 0-based indexing, row 2 is the middle)
row_moves = abs(row - 2)
# Columns: Move the '1' to column 2 (middle column)
col_moves = abs(col - 2)

# Total moves is the sum of row and column moves
total_moves = row_moves + col_moves

# Print the result
print(total_moves)