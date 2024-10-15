# imports
from tkinter import Canvas
from typing import Type
from src.point import Point


class Line():
    def __init__(self, point_1: Type[Point], point_2: Type[Point]):
        self.point_1 = point_1
        self.point_2 = point_2

        
    def draw(self, canvas: Type[Canvas], fill_color: str) -> None:
        x1, x2 = self.point_1.x, self.point_1.y
        y1, y2 = self.point_2.x, self.point_2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)