class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.moved = False
        self.visible = False
        self.ship_inside = False
        self.row = row
        self.col = col

    def fired(self):
        self.moved = True
        self.visible = True

    def __str__(self):
        if self.moved:
            if self.ship_inside:
                return "X"
            else:
                return "•"
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


class Ship:
    MAX_HULL_SIZE = 4

    @classmethod
    def get_hull(size: int, start_row: int, start_col: int, direct: str) -> list:
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
            hull.append(row, col)
            row += d_row
            col += d_col
        return hull

    def __init__(self, size: int, start_row: int, start_col: int, direct: str = None) -> None:
        self.size = size
        self.hull = Ship.get_hull(size, start_row, start_col, direct)
        self.is_killed = False


class Fleet:
    def __init__(self) -> None:
        pass


def main():
    ...


if __name__ == "__main__":
    main()
