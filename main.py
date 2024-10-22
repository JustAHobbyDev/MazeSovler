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


def main():
    win = Window(1000, 1000)
    m = Maze(10, 10, 10, 12, 80, 80, win=win)
    m._break_entrance_and_exit()
    m._animate()

    win.wait_for_close()


if __name__ == '__main__':
    main()