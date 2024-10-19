import os
import sys

this_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(this_dir, "src"))
sys.path.insert(0, base_dir)


import random
from copy import deepcopy
from maze import Maze
from src.cell import Cell
from src.window import Window
from src.line import Line
from src.point import Point

def draw_cell(cell):
    cell.draw()
    
def draw_left_wall(c, win):
    c.left_wall = True
    c.right_wall = False
    c.top_wall = False
    c.bottom_wall = False
    c.draw()

def draw_right_wall(c, win):
    c.right_wall = True
    c.left_wall = False
    c.top_wall = False
    c.bottom_wall = False
    c.draw()


def draw_top_wall(c, win):
    c.right_wall = False
    c.left_wall = False
    c.top_wall = True
    c.bottom_wall = False
    c.draw()


def draw_bottom_wall(c, win):
    c.right_wall = False
    c.left_wall = False
    c.top_wall = False
    c.bottom_wall = True
    c.draw()


def main():
    win = Window(800, 600)

    # for n in range(0, 10):
    #     # x1, x2 = random.randint(10, 400), random.randint(410, 790)
        # y1, y2 = random.randint(10, 400), random.randint(410, 790)
        # point_a = Point(x1, x2)
        # point_b = Point(y1, y2)
        # line = Line(point_a, point_b)
        # fill_color = 'black'
        # win.draw_line(line, fill_color)

    # a, b = 100, 10
    # cell_width = a - b
    # c1 = Cell(a, a, b, b, win)
    # draw_cell(c1)

    # c, d = a + cell_width, b + cell_width
    # c2 = Cell(c, a, d, b, win)
    # draw_cell(c2)
    # c1.draw_move(c2)

    m = Maze(10, 10, 10, 13, 40, 60, win=win)
    for i, col in enumerate(m._cells):
        for j, cell in enumerate(col):
            print(f'cell:{i}:{j} => x1:{cell._x1}, y1:{cell._y1}, x2:{cell._x2}, y2:{cell._y2}')
            cell.draw()


    win.wait_for_close()


if __name__ == '__main__':
    main()