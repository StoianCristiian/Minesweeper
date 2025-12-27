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
        
        self._neighbours_()

    def _neighbours_(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].is_mine:
                    continue

                neigh_count = 0
                for neigh in self._check_neighbours_(r, c):
                    if neigh.is_mine:
                        neigh_count+=1
                self.grid[r][c].neighbours_mines = neigh_count

    def _check_neighbours_(self,r,c):
        neigh = []
        coord = [-1, 0, 1]
        for rand in coord:
            for coloana in coord:
                cellr = rand + r
                cellc = coloana + c
                if 0 <= cellr < self.rows and 0 <= cellc < self.cols:
                    neigh.append(self.grid[cellr][cellc])
        return neigh

