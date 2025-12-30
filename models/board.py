from models import Cell
import random

class Board:
    def __init__(self, rows, cols, mines_cnt):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.mines_cnt = mines_cnt
        self.game_over = False
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

    def _putFlag_(self,r,c):
        poz = self.grid[r][c]
        if not poz.is_revealed:
            poz.is_flagged = not poz.is_flagged
        return poz

    def _cell_click_reveal_(self, r, c):
        cell = self.grid[r][c]

        if cell.is_revealed or cell.is_flagged:
            return []

        cell.is_revealed = True
        all_revealed_cells = [cell]

        if cell.is_mine:
            self.game_over = True
            return all_revealed_cells
        
        if cell.neighbours_mines == 0:
            for neigh in self._check_neighbours_(r,c):
                if not neigh.is_revealed:
                    all_revealed_cells.extend(self._cell_click_reveal_(neigh.row, neigh.column))
        
        return all_revealed_cells
    
    def checkWin(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True


