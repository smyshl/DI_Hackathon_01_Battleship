class Board:

    DTS = [(0,0),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] # cells around ship

    def __init__(self, row: int = 10, col: int = 10) -> None:
        self.board = [[Cell(row, col) for _ in range(col)] for _ in range(row)]
        self.col = col
        self.row = row
        self.moves = []
        self.moves_counter = 0

    def move_fixating(self, x: int, y: int):
        '''Record opponent's moves, who fires'''
        self.moves[y][x] = self.moves_counter

    def push_to_db(self):
        ...

    def is_in_board(self, r, c) -> bool:
        '''check cell's coordinate.'''
        if r not in range(self.row) or c not in range(self.col):
            return False
        return True
    
    def fix_ship_in_board(self, is_fix:bool=True) -> None:
        '''if is_fix = True place ship in the board, else turn off .is_deck.'''
        for r in range(self.row):
            for c in range(self.col):
                if self.board[r][c].is_deck:
                    if is_fix:
                        self.board[r][c].ship_inside = True
                    self.board[r][c].is_deck = False
    
    def place_ship(self, ship: Ship) -> bool:
        '''Place a ship after check out it's position.'''
        for deck in ship.hull:
            r, c = deck
            for dt in Board.DTS:
                dr, dc = dt
                if self.is_in_board(r+dr, c+dc):
                    if self.board[r+dr][c+dc].ship_inside:
                        self.fix_ship_in_board(False)
                        return False
            self.board[r][c].is_deck = True
        self.fix_ship_in_board()
        return True

class Fleet:

    def __init__(self,
                 board: Board,
                 one_unit_ship_amount: int = 4, 
                 two_unit_ship_amount: int = 3,
                 three_unit_ship_amount: int = 2,
                 four_unit_ship_amount: int = 1,
                 ) -> None:
        self.board = board
        self.live_units_amount = one_unit_ship_amount + 2* two_unit_ship_amount + 3 * three_unit_ship_amount + 4 * four_unit_ship_amount
        self.ships = []
        self.one_unit_ship_amount = one_unit_ship_amount 
        self.two_unit_ship_amount = two_unit_ship_amount
        self.three_unit_ship_amount = three_unit_ship_amount
        self.four_unit_ship_amount = four_unit_ship_amount
        self.create_ships()


    def create_ships(self):

        for _ in range(self.one_unit_ship_amount):       #  Not the best solution, but I haven't figured out how
            (start_row, start_col), direct = ask_ship_position(1)
            self.ships.append(Ship(1, start_row, start_col, direct))                 #  to create list .... can't say it in english :))

        for _ in range(self.two_unit_ship_amount):
            (start_row, start_col), direct = ask_ship_position(2)
            self.ships.append(Ship(2, start_row, start_col, direct))

        for _ in range(self.three_unit_ship_amount):
            (start_row, start_col), direct = ask_ship_position(3)
            self.ships.append(Ship(3, start_row, start_col, direct))

        for _ in range(self.four_unit_ship_amount):
            (start_row, start_col), direct = ask_ship_position(4)
            self.ships.append(Ship(4, start_row, start_col, direct))
