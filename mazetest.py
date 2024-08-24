import unittest
from maze import Maze, check_neighbour_direction

class MazeTest(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(0, 0, 3, 3, 10, 10)
            
    def test_1_create_rows(self):
        """
        Test that create_rows initializes the correct number of rows
        """
        self.maze.create_rows()
        self.assertEqual(len(self.maze.cells), self.maze.num_rows,
                         "Number of rows in self.maze.cells should match self.maze.num_rows")

    
    def test_2_create_row_cells(self):
        """
        Test for create_row_cells
        """
        """
        This test checks that:
            * The number of cells created in a row is as defined in the maze class
            * The positioning of the starting x coord of each cell is correct
            * the size of each individual cell that is created is correct
        """
        self.maze.create_rows()
        self.maze.create_row_cells(self.maze.x1, 
                                   self.maze.y1, self.maze.cells[0])
        row_with_cells = self.maze.cells[0]
        self.assertEqual(len(row_with_cells), self.maze.num_columns,
                         "Number of cells should match self.maze.num_columns")
        #assert that the number of columns is as defined in Maze instantiation

        current_index = 0
        while current_index + 1 < len(row_with_cells):
            current_cell = row_with_cells[current_index]
            next_cell = row_with_cells[current_index + 1]
            self.assertEqual(next_cell._x1 - current_cell._x1, self.maze.cell_size_x,
                             "x1 of next cell minus x1 of current cell should be self.maze.cell_size_x")
            self.assertEqual(current_cell._x2, next_cell._x1,
                             "x2 of current cell should be x1 of next cell")
            current_index += 1

        
        current_index = 0
        while current_index < len(row_with_cells):
            current_cell = row_with_cells[current_index]
            self.assertEqual(current_cell._x2 - current_cell._x1, self.maze.cell_size_x,
                             "Each cell's x2 - x1 should be self.maze.cell_size_x")
            self.assertEqual(current_cell._y2 - current_cell._y1, self.maze.cell_size_y,
                             "Each cell's y2 - y1 should be self.maze.cell_size_y")
            current_index += 1
    
    def test_3_create_cells(self):
        """Complete test of create_cells"""
        self.maze.create_cells()

        added_y = 0
        for row in self.maze.cells:
            self.assertEqual(row[0]._y1, self.maze.y1 + added_y, 
                             "Test that y coord of each row is properly incrented")
            added_y += self.maze.cell_size_y

    def test_4_get_cell_neighbours(self):
        """Test that checks retrieval of neighbours of cell"""
        self.maze.create_cells()

        test_cases = [
            ((0, 0), [(1, 0), (0,1)]), 
            ((0, 1), [(0, 0), (0, 2), (1, 1)]), 
            ((0, 2), [(0, 1), (1, 2)]), 
            ((1, 0), [(0, 0), (1, 1), (2, 0)]), 
            ((1, 1), [(1, 0), (0, 1), (1, 2), (2, 1)]), 
            ((1, 2), [(1, 1), (0, 2), (2, 2)]), 
            ((2, 0), [(1, 0), (2, 1)]),
            ((2, 1), [(2, 0), (1, 1), (2, 2)]), 
            ((2, 2), [(2, 1), (1, 2)])
        ]

        for(i, j), expected in test_cases:
            self.assertEqual(sorted(self.maze.get_cell_neighbours(i, j)), sorted(expected), f"Testing cell ({i}, {j})" )

class HelperTest(unittest.TestCase):
    def test_5_test_check_neighbour_direction(self):
        """
        Testing of check neighbour direction function
        """
        test_cases = [
            (
                ((0,1), (0,0)), {True, False, False, False}
            ),
            (
                ((0,0), (0,1)), {False, True, False, False}
            ),
            (
                ((1,0), (0,0)), {False, False, True, False}
            ),
            (
                ((0,0), (2,0)), {False, False, False, True}
            ),

        ]
        for (i, j), expected in test_cases:
            self.assertEqual(check_neighbour_direction(i, j), expected)

if __name__ ==  '__main__':
    unittest.main(verbosity=2)


