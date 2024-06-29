from tools import coordinate_convert

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.board = Board()
        self.fleet = Fleet(self.board)

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
        self.is_killed = False

        
class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.moved = False
        self.visible = True
        self.ship_inside = False
        self.is_deck = False
        self.row = row
        self.col = col

    def fired(self):
        self.moved = True
        self.visible = True

    def __str__(self):
        if self.visible:
            if self.moved:
                if self.ship_inside:
                    return "X"
                else:
                    return "•"
            else:
                if self.ship_inside:
                    return "S"
                else:
                    return " "
        else:
            return " "

class Board:

    def __init__(self, row: int = 10, col: int = 10) -> None:
        self.board = [[Cell(row, col) for _ in range(col)] for _ in range(row)]
        # self.cells = []
        self.col = col
        self.row = row
        self.moves = []
        self.moves_counter = 0
        self.initial_placement()

    def move_fixating(self, x: int, y: int):
        '''Record opponent's moves, who fires'''
        self.moves[y][x] = self.moves_counter

    def initial_placement(self):
        '''Makes initial placement of ship on the board'''
        '''Checks if the ship is on board's limits'''

        # for y in range(self.dim_y):
        #     self.cells[y] = []
        #     self.moves[y] = []
        #     for x in range(self.dim_x):
        #         self.cells[y][x] = Cell(y, x)
        #         self.moves[y][x] = []


    def make_move(self, x: int, y: int):   # x and y in range from 0 to dim_x - 1 and dim_y - 1
        self.moves_counter += 1
        self.cells[y][x].fired()
        self.move_fixating(x, y)

    def push_to_db(self):
        ...

    def check_ship_position(self, ship: object) -> bool:
        '''Checks if the ship is on board's limits'''
        '''Checks if the ship don't toches another ships'''
        # ship_hull = ship
        # print(ship_hull)

        if 0 <= ship.hull[0][0] <= self.row -1 and 0 <= ship.hull[0][1] <= self.col -1 and \
           0 <= ship.hull[-1][0] <= self.row -1 and 0 <= ship.hull[-1][1]<= self.col - 1:  # check limits of the board

            for row in range(ship.hull[0][0] - 1, ship.hull[-1][0] + 2, 1):    # check another ships touching    
                for col in range(ship.hull[0][1] - 1, ship.hull[-1][1] + 2, 1):
                    print(row, col)
                    if 0 <= row <= self.row -1 and 0 <= col <= self.col -1:
                        if self.board[row][col].ship_inside == True:
                            print(row, col)
                            return False    
        else:
            return False

        # self.ships.append(ship.hull)    # inserts ship into the board's ships list
        for unit in ship.hull:
            self.board[unit[0]][unit[1]].ship_inside = True     # marks cells with ship's unit inside
        return True


class Fleet:

    def __init__(self, 
                 board,
                 one_unit_ship_amount: int = 4, 
                 two_unit_ship_amount: int = 3,
                 three_unit_ship_amount: int = 2,
                 four_unit_ship_amount: int = 1,
                 ) -> None:
        self.live_units_amount = one_unit_ship_amount + 2* two_unit_ship_amount + 3 * three_unit_ship_amount + 4 * four_unit_ship_amount
        self.ships = []
        self.one_unit_ship_amount = one_unit_ship_amount 
        self.two_unit_ship_amount = two_unit_ship_amount
        self.three_unit_ship_amount = three_unit_ship_amount
        self.four_unit_ship_amount = four_unit_ship_amount
        self.board = board


    def create_ships(self):

        for _ in range(self.one_unit_ship_amount):       #  Not the best solution, but I haven't figured out how
            self.ships.append(Ship(1))                   #  to create list .... can't say it in english :)
                                                         #
        for _ in range(self.two_unit_ship_amount):
            self.ships.append(Ship(2))

        for _ in range(self.three_unit_ship_amount):
            self.ships.append(Ship(3))

        for _ in range(self.four_unit_ship_amount):
            self.ships.append(Ship(4))

           
def validate_position(start_x_poz:int, start_y_poz:int, direction:str, ):
    ...


def ask_ship_position(ship_size: int) -> tuple:  # it seems it should be tuple :)
    ship_directions = ["N", "E", "S", "W"]
    ship_direction_choice = None
    user_input = input(f"Please enter starting position (a1 or b5 etc.) of a ship which size is {ship_size}: ")
    while ship_direction_choice not in ship_directions:
        ship_direction_choice = input(f"Please enter direction (N, E, S, W) of a ship which size is {ship_size}: ").capitalize()
    return coordinate_convert(user_input), ship_direction_choice



def main():
    ...


if __name__ == "__main__":
    main()
