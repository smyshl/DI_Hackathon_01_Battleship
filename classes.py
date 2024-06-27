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


    def __str__(self):
        if self.moved:
            if self.ship_inside:
                return "X"
            else:
                return "-"
        else:
            return " "
        

class Fleet:
    def __init__(self) -> None:
        pass
            
class Ship:
    def __init__(self, start_row:int, start_col:int, size:int, direct:str) -> None:
        pass    


def main():
    ...



if __name__ == "__main__":
    main()
