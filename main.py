import os
import sys

this_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(this_dir, "src"))
sys.path.insert(0, base_dir)
print(sys.path)

from maze import Maze  # noqa: E402
from src.window import Window  # noqa: E402




def main():
    win = Window(1000, 1000)
    m = Maze(10, 10, 10, 10, 80, 80, win=win)
    m.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
