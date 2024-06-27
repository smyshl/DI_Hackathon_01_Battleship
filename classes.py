from tools import coordinate_convert


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.board = Board()
        self.fleet = Fleet(self.board)



class Board:
    def __init__(self, dim_x: int = 10, dim_y: int = 10) -> None:
        self.cells = []
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.moves = []
        self.moves_counter = 0
        self.initial_placement()
    

    def move_fixating(self, x: int, y: int):
        '''Record opponent's moves, who fires'''
        self.moves[y][x] = self.moves_counter

    def initial_placement(self):
        '''Makes initial placement of ship on the board'''
        '''Checks if the ship is on board's limits'''

        for y in range(self.dim_y):
            self.cells[y] = []
            self.moves[y] = []
            for x in range(self.dim_x):
                self.cells[y][x] = Cell(y, x)
                self.moves[y][x] = []



    def make_move(self, x: int, y: int):   # x and y in range from 0 to dim_x - 1 and dim_y - 1
        self.moves_counter += 1
        self.cells[y][x].fired()
        self.move_fixating(x, y)


    def push_to_db(self):
        ...


class Cell:
    def __init__(self, y, x) -> None:
        self.moved = False
        self.visible = False
        self.ship_inside = False
        self_y_pos = y
        self_x_pos = x


    def fired(self):
        self.moved = True
        self.visible = True
        # if self.ship_inside:



    def __str__(self):
        if self.moved:
            if self.ship_inside:
                return "X"
            else:
                return "-"
        else:
            return " "
        

class Ship: ...


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

           
class Ship(Fleet):
    def __init__(self, size:int) -> None:
        self.size = size
        self.start_x_poz = None
        self.start_y_poz = None
        self.direction = None
        self.place_ship_on_board()

    
    def place_ship_on_board(self):
        self.start_y_poz, self.start_x_poz, self.direction = ask_ship_position(self.size)
        self.direction = ask_ship_position()
        validate_position(self.start_x_poz, self.start_y_poz, self.direction, ) #  Здесь надо бы как-то передать доску,
                                                                              #  но я что-то не соображу как


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
