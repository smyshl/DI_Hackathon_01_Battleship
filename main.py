from view import display_2_boards, game_title
from classes import Ship, Board, Fleet


def main():
    game_title()
    bl = Board()
    br = Board()
    fleet_1 = Fleet(br, {3:1})
    # fleet_2 = Fleet(br, {3:1})
    print(fleet_1)
    # print(fleet_2)
    print(br.board[0][2].fired())
    display_2_boards(br.board, br.board)


if __name__ == "__main__":
    main()
