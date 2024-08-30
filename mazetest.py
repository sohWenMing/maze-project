import unittest
from maze import Maze, check_neighbour_direction, set_current_and_neighbour_walls, NeighbourDirection, check_can_move_to_neighbour
from exceptions import SameCellException, DifferenceTooLargeException, BothDirectionException
from window import Window

class Suite_1_MazeTest(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(0, 0, 3, 3, 10, 10)
            
    def test_1_create_rows(self):
        
        self.maze.create_rows()
        self.assertEqual(len(self.maze.cells), self.maze.num_rows,
                         "Number of rows in self.maze.cells should match self.maze.num_rows")

    
    def test_2_create_row_cells(self):
        
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
        self.maze.create_cells()

        added_y = 0
        for row in self.maze.cells:
            self.assertEqual(row[0]._y1, self.maze.y1 + added_y, 
                             "Test that y coord of each row is properly incrented")
            added_y += self.maze.cell_size_y

    def test_4_get_cell_neighbours(self):
       
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

class Suite_2_HelperTest(unittest.TestCase):
    def test_5_test_check_neighbour_direction(self):
        
        test_cases = [
            (
                ((0,1), (0,0)), NeighbourDirection.LEFT
            ),
            (
                ((0,0), (0,1)), NeighbourDirection.RIGHT
            ),
            (
                ((1,0), (0,0)), NeighbourDirection.UP
            ),
            (
                ((0,0), (1,0)), NeighbourDirection.DOWN
            ),

        ]
        for (i, j), expected in test_cases:
            self.assertEqual(check_neighbour_direction(i, j), expected)

    def test_6_test_check_neighbour_directions_exceptions(self):
       
        with self.assertRaises(SameCellException):
            check_neighbour_direction((0,0), (0,0))
        with self.assertRaises(BothDirectionException):
            check_neighbour_direction((0,0), (1,1)) 
        with self.assertRaises(DifferenceTooLargeException):
            check_neighbour_direction((0,0), (0, 2))

    def test_7_test_set_current_and_neighbour_walls(self):
        
        self.maze = Maze(0, 0, 3, 3, 10, 10)
        self.maze.create_cells()
        
        # definition of test case: (current_cell, neighbour_cell), [[has walls of current], [has walls of neighbour]]
        # has walls are set as has_left_wall, has_right_wall, has_top_wall, has_bottom_wall
        #cells 1 - 9 are cells in a 3 x 3 matrix

        ###################
        # 1 2 3 #
        # 4 5 6 #
        # 7 8 9 # 
        ###################

        cell_1 = self.maze.cells[0][0]
        cell_2 = self.maze.cells[0][1]
        cell_3 = self.maze.cells[0][2]
        cell_6 = self.maze.cells[1][2]
        cell_9 = self.maze.cells[2][2]

        test_cases = [
            ((cell_2, cell_1), NeighbourDirection.LEFT, [False, True, True, True], [True, False, True, True]),
            ((cell_2, cell_3), NeighbourDirection.RIGHT, [False, False, True, True], [False, True, True, True]),
            ((cell_6, cell_3), NeighbourDirection.UP, [True, True, False, True], [False, True, True, False]),
            ((cell_6, cell_9), NeighbourDirection.DOWN, [True, True, False, False], [True, True, False, True])
        ]

        for (i,j), neighbour_direction, expected_current_walls, expected_neighbour_walls in test_cases:
            set_current_and_neighbour_walls(i, j, neighbour_direction)
            self.assertEqual([i.has_left_wall, i.has_right_wall, i.has_top_wall, i.has_bottom_wall], expected_current_walls)
            self.assertEqual([j.has_left_wall, j.has_right_wall, j.has_top_wall, j.has_bottom_wall], expected_neighbour_walls)
        #for this to work, there has to be a maze for context to be setup

# class Suite_3_VisitAndResetTest(unittest.TestCase):
#     def test_8_visit_break_walls_and_reset(self):
#         self.maze = Maze(10, 10, 10, 10, 50, 50, seed=10)
#         self.maze.create_cells()
#         self.window = Window(800, 600)
#         self.maze.draw_all_cells(self.window)
#         self.maze.break_entrance_and_exit(self.window)
#         self.maze.break_walls_r(0,0, self.window)

#         for row in self.maze.cells:
#             for cell in row:
#                 self.assertEqual(cell.visited, True)
        
#         self.maze.reset_cells_visited()
#         for row in self.maze.cells:
#             for cell in row:
#                 self.assertEqual(cell.visited, False)

class Suite_4_CheckCanMoveToNeighbours(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(10, 10, 3, 3, 50, 50, seed=10)
    
    def test_9_check_can_move_to_neighbour(self):    
        self.maze.create_cells()
        self.maze.cells[0][0].has_right_wall = False
        self.assertEqual(check_can_move_to_neighbour((0,0), (0,1), self.maze.cells[0][0]), True, "Check can move right, should return True")
        self.assertEqual(check_can_move_to_neighbour((0,1), (0,2), self.maze.cells[0][1]), False, "Check can move right, should return False")
        self.maze.cells[0][0].has_bottom_wall = False
        self.assertEqual(check_can_move_to_neighbour((0,0), (1,0), self.maze.cells[0][0]), True, "Check can move down, should return True")
        self.assertEqual(check_can_move_to_neighbour((0,1), (1,1), self.maze.cells[0][1]), False, "Check can move down, shoudl return False")
        self.maze.cells[0][1].has_left_wall = False
        self.assertEqual(check_can_move_to_neighbour((0,1), (0,0), self.maze.cells[0][1]), True, "Check can move left, should return True")
        self.assertEqual(check_can_move_to_neighbour((0,2), (0,1), self.maze.cells[0][2]), False, "Check can move left, shoudl return False")
        self.maze.cells[1][0].has_top_wall = False
        self.assertEqual(check_can_move_to_neighbour((1,0), (0,0), self.maze.cells[1][0]), True, "Check can move up, should return True")
        self.assertEqual(check_can_move_to_neighbour((2,0), (1,0), self.maze.cells[2][0]), False, "Check can move up, should return False")


        


        
if __name__ ==  '__main__':
    unittest.main(verbosity=2)


