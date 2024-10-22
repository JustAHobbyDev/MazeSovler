import unittest
from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def setUp(self):
        self.win = Window(800, 600)

    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        m = Maze(0, 0, rows, cols, 10, 10, self.win)
        self.assertEqual(len(m._cells), cols)
        self.assertEqual(len(m._cells[0]), rows)

    def test_break_entrance_and_exit(self):
        cols = 10
        rows = 11
        m = Maze(0, 0, rows, cols, 10, 10, self.win)
        m._break_entrance_and_exit()
        _entrance = m._cells[0][0]
        _exit = m._cells[-1][-1]
        self.assertFalse(_entrance.top_wall, "entrance has a top wall")
        self.assertFalse(_exit.bottom_wall, "exit has a bottom wall")

        
if __name__ == '__main__':
    unittest.main()