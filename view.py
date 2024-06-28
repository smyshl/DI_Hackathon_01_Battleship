import os

# System call
os.system("")

# Class of different styles
class style():
    BOLD='\033[01m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BG_blue = '\033[44m'
    BG_cayn='\033[46m'

# board = [["x" for _ in range(10)] for _ in range(10)]

# def display_board(board:list) -> None:
#     """display the board (GUI :-). 
#     board = list[list[Cell]]."""

#     rows_num = len(board)
#     cols_num = len(board[0])
#     print(style.BG_cayn)
#     grid_row = "|---" * cols_num + "|"
#     for row in range(rows_num):
#         data_row = ""
#         for column in range(cols_num):
#             data_row += f"| {board[row][column]} "
#         data_row += "|"
#         print(grid_row)
#         print(data_row)
#     print(grid_row)
#     print(style.RESET)

def display_2_boards(board_l:list, board_r:list) -> None:
    """display the 2 boards (GUI :-) left board >= right board. 
    board = list[list[Cell]]."""

    interval = "         "
    rows_num_l = len(board_l)
    cols_num_l = len(board_l[0])
    rows_num_r = len(board_r)
    cols_num_r = len(board_r[0])
    print(style.BG_cayn)
    print(style.BOLD)
    print("      ", "self_name", " " * (cols_num_l*4-10), interval, " ", "enemy_name", " " * (cols_num_r*4-10))

    # print header
    head = "    " + "".join([f"  {i+1} " for i in range(cols_num_l)])
    head += interval + "  "
    head += "".join([f"  {i+1} " for i in range(cols_num_r)])
    print(head)

    # create grid rows
    grid_row_l = "    " + "|---" * cols_num_l + "|"
    grid_row = grid_row_l + interval + "  "
    grid_row += "|---" * cols_num_r + "|"
    grid_row_end = grid_row

    # create data rows
    for row in range(rows_num_l):
        data_row_l = "  " + chr(97+row) + " "     # left board data row
        for column in range(cols_num_l):
            data_row_l += f"| {board_l[row][column]} "
        data_row_l += "|"

        data_row = data_row_l + interval + chr(97+row) + " " # full data row
        if row in range(rows_num_r):
            for column in range(cols_num_r):
                data_row += f"| {board_r[row][column]} "
            data_row += "|"
        if row < rows_num_r:
            print(grid_row)
            print(data_row)
        elif row == rows_num_r:
            print(grid_row)
            print(data_row_l)
        else:
            print(grid_row_l)
            print(data_row_l)
            grid_row_end = grid_row_l
    print(grid_row_end)
    print(style.RESET)


def game_title():
    print(style.BG_blue +'''
        +---------------------------------------------------------------------------------------------+
        |                                                                                             |  
        |        OOOO      OO    OOOOOOO  OOOOOOO  O      OOOOO   OOOO    O    O    O   OOOO          |
        |        O.  O    O  O      O.       O.    O.     O      O.       O.   O.   O.  O.  O.        |
        |  ====  O.  O   O.   O.    O.       O.    O.     O.     O.       O.   O.   O.  O.  O.  ====  |
        |  ++++  OOOO .  OOOOOO     O.       O.    O.     OOOOO.   OOO.   OOOOOO.   O.  OOOO.   ++++  |
        |  ====  O.  O.  O.   O.    O.       O.    O.     O           O.  O.   O.   O.  O.      ====  |
        |        O.  O.  O.   O.    O.       O.    O.     O.          O.  O.   O.   O.  O.            |
        |        OOOO.   O.   O.    O.       O.    OOOOOO OOOOO.  OOOO.   O.   O.   O.  O.            |
        |                                                                                             |
        +---------------------------------------------------------------------------------------------+
        © 2024 EUGENE & SASHA
    '''+ style.RESET)
    print(style.YELLOW + '''
        INSTRUCTION:
        You have a board 10 x 10. You need to place in it 10 ships: 1 - 4x, 2 - 3x, 3 - 2x, 4 - 1x.
        Your competitor need to do so. You make shot by turn entering a cell coordinate, exp. a0, b3.
        The goal is to kill all of competitor's ships. If your shot is successful, then you shot out of turn.
    '''+ style.RESET)
    input(style.RED +"               ----------- P R E S S   E N T E R   T O   S T A R T ----------"+ style.RESET)
