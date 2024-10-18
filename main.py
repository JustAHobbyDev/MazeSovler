import random
from copy import deepcopy
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
    a, b = 10, 100
    cell_width = b - a
    c1 = Cell(a, a, b, b, win)
    draw_cell(c1)

    c, d = a + cell_width, b + cell_width
    c2 = Cell(c, a, d, b, win)
    draw_cell(c2)

    c1.draw_move(c2)



    win.wait_for_close()


if __name__ == '__main__':
    main()