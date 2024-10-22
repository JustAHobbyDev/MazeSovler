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
            win: Type[Canvas]|None = None
        ):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

        
    def _create_cells(self):
        for col in range(0, self.cols):
            x1 = self.x1 + self.cell_size_x * col 
            x2 = x1 + self.cell_size_x
            cell_column = []
            for row in range(0, self.rows):
                y1 = self.y1 + self.cell_size_y * row
                y2 = y1 + self.cell_size_y
                cell_column.append(Cell(x1, y1, x2, y2, self.win))
            self._cells.append(cell_column)

        for i, col in enumerate(self._cells):
            for j, cell in enumerate(col):
                print(f'cell:{i}:{j} => x1:{cell._x1}, y1:{cell._y1}, x2:{cell._x2}, y2:{cell._y2}')
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