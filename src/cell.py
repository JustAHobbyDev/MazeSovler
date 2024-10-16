from typing import Type
from tkinter import Canvas

from src.line import Line
from src.point import Point


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

        
    def draw(self):
        if self.left_wall:
            p0 = Point(self._x1, self._y1)
            p1 = Point(self._x1, self._y2)
            l1 = Line(p0, p1)
            self._win.draw_line(l1, "black")
        if self.right_wall:
            p0 = Point(self._x2, self._y1)
            p1 = Point(self._x2, self._y2)
            l2 = Line(p0, p1)
            self._win.draw_line(l2, "black")
        if self.top_wall:
            p0 = Point(self._x1, self._y2)
            p1 = Point(self._x2, self._y2)
            l3 = Line(p0, p1)
            self._win.draw_line(l3, "black")
        if self.bottom_wall:
            p0 = Point(self._x1, self._y1)
            p1 = Point(self._x2, self._y1)
            l4 = Line(p0, p1)
            self._win.draw_line(l4, "black")