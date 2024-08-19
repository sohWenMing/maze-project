import unittest
from maze import Maze

class MazeTest(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(0, 0, 3, 3, 10, 10)
        self.maze.create_cells()
    
    def test_create_cells(self):
        self.assertEqual(len(self.maze.cells), 3)
    
    def test_create_row_cells(self):
        self.maze.create_row_cells(self.maze.x1, self.maze.y1, 
                               self.maze.cells[0])
        for cell in self.maze.cells[0]:
            print(f"cell x1: {cell._x1}")


if __name__ ==  '__main__':
    unittest.main()


