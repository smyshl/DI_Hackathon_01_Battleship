
board = [["x" for _ in range(10)] for _ in range(10)]

def display_board() -> None:
    """To display the board (GUI :-)."""

    rows_num = len(board)
    cols_num = len(board[0])

    grid_row = "|---" * cols_num + "|"
    for row in range(rows_num):
        data_row = ""
        for column in range(cols_num):
            data_row += f"| {board[row][column]} "
        data_row += "|"
        print(grid_row)
        print(data_row)
    print(grid_row)

display_board()
