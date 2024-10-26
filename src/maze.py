import random
from time import sleep
from tkinter import Canvas
from typing import Type

from cell import Cell


class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            rows: int,
            cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Type[Canvas]|None = None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = random.seed(seed) if seed else None
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        
    def _create_cells(self):
        rows = range(0, self.rows)
        for row in rows:
            y1 = self.y1 + self.cell_size_y * row
            y2 = y1 + self.cell_size_y
            cell_column = []
            for col in range(0, self.cols):
                x1 = self.x1 + self.cell_size_x * col 
                x2 = x1 + self.cell_size_x
                cell_column.append(Cell(x1, y1, x2, y2, self.win))
            self._cells.append(cell_column)

        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                cell.draw()

                
    def get_neighbors(self, i, j):
        neighbors = []

        for n in [-1, 1]:
            d0 = i + n
            if d0 == (i-1) or d0 == (i+1):
                if d0 >= 0 and d0 < self.rows:
                    neighbors.append((d0, j))
            d1 = j + n
            if d1 == (j-1) or d1 == (j+1):
                if d1 >= 0 and d1 < self.cols:
                    neighbors.append((i, d1))

        return neighbors

        
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []
            neighbors = self.get_neighbors(i, j)
            for neighbor in neighbors:
                x, y = neighbor
                n_cell = self._cells[x][y]
                if not n_cell.visited:
                    to_visit.append((x, y))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            m, n = to_visit[random.randrange(0, len(to_visit))]
            if j < n:
                self._cells[i][j].right_wall = False
                self._cells[m][n].left_wall = False
            if n < j:
                self._cells[i][j].left_wall = False
                self._cells[m][n].right_wall = False
            if i < m:
                self._cells[i][j].bottom_wall = False
                self._cells[m][n].top_wall = False
            if m < i:
                self._cells[i][j].top_wall = False
                self._cells[m][n].bottom_wall = False

            self._break_walls_r(m, n)
            

    def _reset_cells_visited(self):
        cells = self._cells
        for row in cells:
            for cell in row:
                cell.visited = False


    def _break_entrance_and_exit(self):
        _entrance = self._cells[0][0]
        _entrance.top_wall = False
        self._draw_cell(0, 0)

        _exit = self._cells[-1][-1]
        _exit.bottom_wall = False
        self._draw_cell(-1, -1)

            
    def _draw_cell(self, i, j):
        # i: col, j: row
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

        
    def _animate(self):
        self.win.redraw()
        sleep(0.05)
    
    
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if (i == self.rows - 1) and (j == self.cols - 1):
            return True

        neighbors = self.get_neighbors(i, j)
        for neighbor in neighbors:
            m, n = neighbor
            n_cell = self._cells[m][n]
            if n_cell.visited:
                continue

            # (0, 0) (1, 0) => (-1, 0) DOWN
            # (1, 0) (0, 0) => (1, 0) UP
            # (0, 0) (0, 1) => (0, -1) RIGHT
            # (0, 1) (0, 0) => (0, 1) LEFT
            dx = i - m
            dy = j - n
            print(f"dx: {dx}, dy: {dy}")

            if dx == -1: # DOWN
                bottom = n_cell
                top = current_cell
                if not top.bottom_wall and not bottom.top_wall:
                    current_cell.draw_move(n_cell)
                    solve_next_cell = self._solve_r(m, n)
                    if solve_next_cell:
                        return True
                    else:
                        current_cell.draw_move(n_cell, undo=True)
            if dx == 1: # UP
                top = n_cell
                bottom = current_cell
                if not top.bottom_wall and not bottom.top_wall:
                    current_cell.draw_move(n_cell)
                    solve_next_cell = self._solve_r(m, n)
                    if solve_next_cell:
                        return True
                    else:
                        current_cell.draw_move(n_cell, undo=True)
                    
            if dy == -1: # RIGHT
                left = current_cell
                right = n_cell
                if not left.right_wall and not right.left_wall:
                    current_cell.draw_move(n_cell)
                    solved = self._solve_r(m, n)
                    if solved:
                        return True
                    current_cell.draw_move(n_cell, undo=True)
            if dy == 1: # LEFT
                left = n_cell
                right = current_cell
                if not left.right_wall and not right.left_wall:
                    current_cell.draw_move(n_cell)
                    solve_next_cell = self._solve_r(m, n)
                    if solve_next_cell:
                        return True
                    else:
                        current_cell.draw_move(n_cell, undo=True)
                    
        print("_solve_r => False")
        print(f"current_cell: ({i}, {j}), visited: {current_cell.visited}")
        print(f"n_cell: ({m}, {n}), visited: {n_cell.visited}")
        return False

        
    def solve(self):
        self._solve_r(0, 0)
