from typing import Type
from tkinter import Canvas

from line import Line
from point import Point


class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
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
        p0 = Point(self._x1, self._y1)
        p1 = Point(self._x1, self._y2)
        if self.left_wall:
            self._win.draw_line(Line(p0, p1), "black")
        else:
            self._win.draw_line(Line(p0, p1),self._win.canvas['background'])

        p0 = Point(self._x2, self._y1)
        p1 = Point(self._x2, self._y2)
        if self.right_wall:
            self._win.draw_line(Line(p0, p1), "black")
        else:
            self._win.draw_line(Line(p0, p1), self._win.canvas['background'])

        if self.top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), self._win.canvas['background'])

        if self.bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), self._win.canvas['background'])

            
    def draw_move(self, to_cell, undo=False):
        line_color = 'gray' if undo else 'red'
        # xy to ab
        _x = self._x1 + (self._x2 - self._x1) / 2.0
        _y = self._y1 + (self._y2 - self._y1) / 2.0
        a = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2.0
        b = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2.0
        p0, p1 = Point(_x, _y), Point(a, b)
        line = Line(p0, p1)
        self._win.draw_line(line, line_color)