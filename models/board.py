from models import Cell
import random

class Board:
    def __init__(self, rows, cols, mines_cnt):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.mines_cnt = mines_cnt
        self.initialize_board()

    def initialize_board(self):
        self.grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(Cell(r, c))
            self.grid.append(row)
        
        self._place_mines()

    def _place_mines(self):
        all_coordinates = [(r,c) for r in range(self.rows) for c in range(self.cols)]
        mine_coords = random.sample(all_coordinates, self.mines_cnt)

        for r, c in mine_coords:
            self.grid[r][c].is_mine = True


