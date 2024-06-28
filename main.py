import view, classes


def main():
    view.game_title()
    b_self = classes.Board()
    b_enemy = classes.Board(5,5)
    b_self.board[3][5].moved = True
    b_self.board[7][8].moved = True
    b_self.board[7][8].ship_inside = True
    b_enemy.board[1][4].moved = True
    view.display_2_boards(b_self.board, b_enemy.board)


if __name__ == "__main__":
    main()

