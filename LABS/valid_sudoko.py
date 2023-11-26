def is_valid_sudoku(board):
    # check the rows first
    for row in board:
        visited_rows = []
        for num in row:
            if num != ".":
                if num in visited_rows:
                    return "NO"
                visited_rows.append(num)

    # check the colums next
    for col in range(9):
        visited_cols = []
        for row in range(9):
            num = board[row][col]
            if num != ".":
                if num in visited_cols:
                    return "NO"
                visited_cols.append(num)

    # checking the 3*3 boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            visited = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    num = board[row][col]
                    if num != ".":
                        if num in visited:
                            return "NO"
                        visited.append(num)

    return "YES"


n = int(input())
board = []
for i in range(n):
    row = input().split()
    board.append(row)

result = is_valid_sudoku(board)
print(result)
