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

