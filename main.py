import random
from src.window import Window
from src.line import Line
from src.point import Point


def main():
    win = Window(800, 600)

    for n in range(0, 10):
        x1, x2 = random.randint(0, 800), random.randint(0, 800)
        y1, y2 = random.randint(0, 800), random.randint(0, 800)
        point_a = Point(x1, x2)
        point_b = Point(y1, y2)
        line = Line(point_a, point_b)
        fill_color = 'black'
        win.draw_line(line, fill_color)

    win.wait_for_close()


if __name__ == '__main__':
    main()