from tools import coordinate_convert
from view import display_board, display_2_boards


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.board = Board()
        self.fleet = Fleet(self.board, {1: 1, 2: 1})
        self.moves_counter = 1

    def make_move(self, other_players):

        for other_player in other_players:
            display_2_boards(self.board.board, other_player.board.board, self.name, other_player.name)    
            # print("Move #", self.moves_counter)
            print(self.name, "attacks", other_player.name)
            row, col = coordinate_convert(input("Please input coordinates of fire (ex. a1): "))
            # print(row, col, other_player.name)
            other_player.board.make_move(row, col)
            if other_player.board.board[row][col] == True:
                other_player.fleet.live_units_amount -= 1
            display_2_boards(self.board.board, other_player.board.board, self.name, other_player.name)
            if other_player.fleet.is_destroyed:
                print(other_player.name, "LOSE!")
                return
            input("Press enter for the next move")


class Game:
    def __init__(self, player_1: object, player_2: object) -> None:
        self.players = [player_1, player_2]

    def play(self):

        last_fleet_amounts = [player.fleet.live_units_amount for player in self.players]
        print("last fleet amount", last_fleet_amounts)

        while not (True in [player.fleet.is_destroyed for player in self.players]):

            for index in range(len(self.players)):

                who_moves = self.players[index]
                other_players = [self.players[_] for _ in range(len(self.players)) if _ != index]

                who_moves.make_move(other_players)

                if True in [player.fleet.is_destroyed for player in self.players]:
                    break

                # last_fleet_amounts = [player.fleet.live_units_amount for player in self.players]
                # print("last fleet amount", last_fleet_amounts)
            # if index == 0:      # player's 1 move
            #     # get row, col coordinates of fire
            #     # probably it should be function
            #     self.players[index + 1][1].board.make_move(row, col)
            #     if self.players[index + 1][1].board[row][col] == True:
            #         self.players[index + 1][2].live_units_amount -= 1
            #         # extra move
            # else:
            #     # get row, col coordinates of fire
            #     self.players[index - 1][1].board.make_move(row, col)
            #     if self.players[index - 1][1].board[row][col] == True:
            #         self.players[index - 1][2].live_units_amount -= 1
            #         # extra move
            # if index == 0:
            #     index = 1
            # else:
            #     index = 0


class Ship:
    MAX_HULL_SIZE = 4

    @classmethod
    def get_hull(cls, size: int, start_row: int, start_col: int, direct: str) -> list:
        d_row = 0
        d_col = 0
        if 0 < size <= Ship.MAX_HULL_SIZE:
            match direct:
                case "up":
                    d_row = -1
                case "down":
                    d_row = 1
                case "left":
                    d_col = -1
                case "right":
                    d_col = 1
                case _:
                    size = 1
        else:
            raise ValueError("Ship size out of range.")
        hull = []
        row = start_row
        col = start_col
        for _ in range(size):
            hull.append((row, col),)
            row += d_row
            col += d_col
        return hull

    def __init__(self, size: int, start_row: int, start_col: int, direct: str = None) -> None:
        self.size = size
        self.hull = Ship.get_hull(size, start_row, start_col, direct)
        self.decks_destroyed = 0

    @property
    def is_killed(self) -> bool:
        return self.decks_destroyed == self.size

    def __repr__(self) -> str:
        str = ""
        for deck in self.hull:
            str += f"({deck[0]}-{deck[1]}), "
        return str


class Cell:
    def __init__(self, row: int, col: int, visible: bool = True) -> None:
        self.visible = visible
        self.moved = False
        self.ship_inside = False
        self.is_deck = False
        self.row = row
        self.col = col
        self.ship: Ship = None

    def fired(self) -> str:
        self.moved = True
        self.visible = True
        if self.ship_inside:
            self.ship.decks_destroyed += 1
            if self.ship.is_killed:
                return "Ship is killed."
            else:
                return "Ship is damaged."
        return "Miss :-)"

    def __str__(self):      # view left board (myself)
        if self.moved:
            if self.ship_inside:
                return "X"
            else:
                return "•"
        else:
            if self.ship_inside:
                return "O"
            else:
                return " "

    def __repr__(self):     # view right board (enemy)
            if self.moved:
                if self.ship_inside:
                    return "X"
                else:
                    return "•"
            else:
                return " "


class Board:

    def __init__(self, row: int = 10, col: int = 10, visible: bool = True) -> None:
        self.board = [[Cell(row, col, visible)
                       for _ in range(col)] for _ in range(row)]
        self.col = col
        self.row = row
        self.moves = [[None for _ in range(col)]
                      for _ in range(row)]  # log list
        self.moves_counter = 0

        # self.initial_placement()
        # self.ships = []

    def move_fixating(self, row: int, col: int):
        '''Logging: record opponent's moves, who fires'''
        self.moves[row][col] = self.moves_counter

    def place_ship(self, ship: object) -> bool:
        '''Checks if the ship is on board's limits. Checks if the ship don't toches another ships. Place ship on board.'''
        # ship_hull = ship
        # print(ship_hull)

        if 0 <= ship.hull[0][0] <= self.row - 1 and 0 <= ship.hull[0][1] <= self.col - 1 and \
           0 <= ship.hull[-1][0] <= self.row - 1 and 0 <= ship.hull[-1][1] <= self.col - 1:  # check limits of the board

            # check another ships touching
            for row in range(ship.hull[0][0] - 1, ship.hull[-1][0] + 2, 1):
                for col in range(ship.hull[0][1] - 1, ship.hull[-1][1] + 2, 1):
                    # print(row, col)
                    if 0 <= row <= self.row - 1 and 0 <= col <= self.col - 1:
                        if self.board[row][col].ship_inside == True:
                            # print(row, col)
                            return False
        else:
            return False

        # self.ships.append(ship.hull)    # inserts ship into the board's ships list
        for unit in ship.hull:
            # marks cells with ship's unit inside
            self.board[unit[0]][unit[1]].ship_inside = True
            self.board[unit[0]][unit[1]].ship = ship

        return True

    # x and y in range from 0 to dim_x - 1 and dim_y - 1
    def make_move(self, row: int, col: int):
        self.moves_counter += 1
        print(self.board[row][col].fired())
        self.move_fixating(row, col)

    def push_to_db(self):
        ...


class Fleet:

    def __init__(self, board: Board, ships_types: dict = {1: 4, 2: 3, 3: 2, 4: 1}) -> None:
        self.board = board
        self.ships_types = ships_types
        self.live_units_amount = sum(ships_types.values())
        print(self.live_units_amount)
        self.ships = []
        self.create_ships()

    def create_ships(self):
        print("You need to place ships on board. Follow instructions.")
        display_board(self.board.board)
        for deck_numbers in self.ships_types:
            for _ in range(self.ships_types[deck_numbers]):
                need_input = True
                while need_input:
                    (start_row, start_col), direct = ask_ship_position(deck_numbers)
                    ship = Ship(deck_numbers, start_row, start_col, direct)
                    if self.board.place_ship(ship):
                        self.ships.append(ship)
                        display_board(self.board.board)
                        print("Ship placed. Next please.")
                        need_input = False
                    else:
                        print("The ship isn't coorrect. Repeat please.")
        print("Good! All ships are placed.")

    @property
    def is_destroyed(self) -> bool:
        for ship in self.ships:
            if not ship.is_killed:
                return False
        return True

    def __repr__(self) -> str:
        str = ""
        for ship in self.ships:
            str += repr(ship) + "\n"
        return str


def ask_ship_position(ship_size: int) -> tuple:  # it seems it should be tuple :)
    ship_directions = {"U": "up", "R": "right", "D": "down", "L": "left"}
    ship_direction_choice = None
    user_input = input(
        f"Please enter starting position (a1 or b5 etc.) of a ship which size is {ship_size}: ")
    if user_input == "q":
        exit()
    if ship_size == 1:
        return coordinate_convert(user_input), None
    else:
        while ship_direction_choice not in ship_directions:
            ship_direction_choice = input(
                f"Please enter direction (U, R, D, L) of a ship which size is {ship_size}: ").capitalize()
        return coordinate_convert(user_input), ship_directions[ship_direction_choice]


def main():

    p1 = Player("p1")
    p2 = Player("p2")
    game = Game(p1, p2)

    game.play()

    # board_1 = Board()
    # board_1.board[2][2].fired()
    # print(board_1.board[2][2])

    # ship_1 = [(6, 5), (7, 5), (8, 5), (9, 5)]
    # for unit in ship_1:
    #     board_1.board[unit[0]][unit[1]].ship_inside = True
    #     # print(board_1.board[unit[0]][unit[1]], board_1.board[unit[0]][unit[1]].ship_inside)
    # ship_2 = [(5, 1), (5, 2), (5, 3), (5, 4)]

    # print(board_1.check_ship_position(ship_2))


if __name__ == "__main__":
    main()
