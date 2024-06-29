from view import display_2_boards, game_title
from classes import Ship, Board


def main():
    game_title()
    b_self = Board()
    b_enemy = Board()
    # b_self.board[3][5].moved = True
    # b_self.board[7][8].moved = True
    # b_self.board[0][0].ship_inside = True
    # b_enemy.board[1][4].moved = True

    ship = Ship(3, 0, 7, "right")
    print(b_self.check_ship_position(ship))
    # print(b_self.place_ship(ship))
    ship = Ship(2, 2, 6, "down")
    print(b_self.check_ship_position(ship))

    display_2_boards(b_self.board, b_enemy.board)


if __name__ == "__main__":
    main()

