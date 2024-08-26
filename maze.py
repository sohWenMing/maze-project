from units import Cell
import time
import random
from enum import Enum
from exceptions import SameCellException, DifferenceTooLargeException, BothDirectionException

class NeighbourDirection(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

def check_neighbour_direction(current, neighbour):
    print("current", current)
    print("neighbour", neighbour)
    
    class Exception_Type(Enum):
        EX_SAME_CELL = 1
        EX_DIFFERENCE_TOO_LARGE = 2
        EX_BOTH_DIRECTION = 3
    
    def throw_exception(exception_type: Exception_Type):
        if not isinstance(exception_type, Exception_Type):
            raise ValueError("Invalid exception type. Must be instance of exceptoin type enum")
        
        if exception_type == Exception_Type.EX_SAME_CELL:
            raise SameCellException("Cells passed into check_neighbour_direction cannot be the same")
        if exception_type == Exception_Type.EX_DIFFERENCE_TOO_LARGE:
            raise DifferenceTooLargeException("Differnce between i or j value cannot be more than 1")
        if exception_type == Exception_Type.EX_BOTH_DIRECTION:
            raise BothDirectionException("cell cannot have difference in both i and j values")
    
    def check_difference(current_val, neighbour_val):
        if abs(current_val - neighbour_val) != 1:
            throw_exception(Exception_Type.EX_DIFFERENCE_TOO_LARGE)

    def check_other_direction(current_other_val, current_neighbour_val):
        if current_other_val != current_neighbour_val:
            throw_exception(Exception_Type.EX_BOTH_DIRECTION)
    
    if current == neighbour:
        throw_exception(Exception_Type.EX_SAME_CELL)

    is_left = False
    is_right = False
    is_up = False
    is_down = False 
 
    current_i = current[0]
    current_j = current[1]
    neighbour_i = neighbour[0]
    neighbour_j = neighbour[1]

    #check for neighbour left of current
    if neighbour_j < current_j:
        
        check_difference(neighbour_j, current_j)
        check_other_direction(neighbour_i, current_i)
        is_left = True
    #check for neighbour right of current
    if neighbour_j > current_j:
        check_difference(neighbour_j, current_j)
        check_other_direction(neighbour_i, current_i)
        is_right = True
    #check for neighbour above current
    if neighbour_i < current_i:
        check_difference(neighbour_i, current_i)
        check_other_direction(neighbour_j, current_j)
        is_up = True
    #check for neighbour below current
    if neighbour_i > current_i:
        check_difference(neighbour_i, current_i)
        check_other_direction(neighbour_j, current_j)
        is_down = True 
    
    if is_left:
        return NeighbourDirection.LEFT
    if is_right:
        return NeighbourDirection.RIGHT
    if is_up:
        return NeighbourDirection.UP
    if is_down:
        return NeighbourDirection.DOWN
        
def set_current_and_neighbour_walls(current: Cell, neighbour: Cell, direction: NeighbourDirection):
    if direction == NeighbourDirection.LEFT:
        current.has_left_wall = False
        neighbour.has_right_wall = False
        return
    elif direction == NeighbourDirection.RIGHT:
        current.has_right_wall = False
        neighbour.has_left_wall = False
        return
    elif direction == NeighbourDirection.UP:
        current.has_top_wall = False
        neighbour.has_bottom_wall = False
        return
    else:
        #this defaults to down
        current.has_bottom_wall = False 
        neighbour.has_top_wall = False
        return



    

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_columns,
                 cell_size_x,
                 cell_size_y,
                 seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self.visited_for_break = []
        self.to_visit_for_break = []
        self.seed = None
        random.seed(self.seed)
        
        
    def create_rows(self):
        while len(self.cells) < self.num_rows:
            self.cells.append([])

    def create_row_cells(self, initial_x, initial_y, row):
        x_current = initial_x 
        while len(row) < self.num_columns:
            cell = Cell(x_current, 
                        x_current + self.cell_size_x,
                        initial_y,
                        initial_y + self.cell_size_y)
            row.append(cell)
            x_current += self.cell_size_x
            
    def create_cells(self):
        #first, create the number of rows in self.cells
        self.create_rows()
        added_y = 0
        for row in self.cells:
            self.create_row_cells(self.x1, self.y1 + added_y, row)
            added_y += self.cell_size_y
        
        """
        the first cell will have an x1 of self.x1, and an x2 of 
        self.x1 + self.cell_size_x
        
        it will also have a y1 of self.x1, and a 
        y2 of self.y1 + self.cell_size_y
        """
    
    def draw_cell(self, window, cell):
        canvas = window.get_canvas()
        cell.draw(canvas)
        self.animate(window)

    def animate(self, window):
        window.redraw()
        time.sleep(0.1)

    def draw_all_cells(self, window):
        for row in self.cells:
            for cell in row:
                self.draw_cell(window, cell)

    def break_entrance_and_exit(self, window):
        entrance_cell = self.cells[0][0]
        exit_cell = self.cells[-1][-1]

        #remove the top of the entrance cell
        entrance_cell.has_top_wall = False
        self.draw_cell(window, entrance_cell)
        exit_cell.has_bottom_wall = False
        self.draw_cell(window, exit_cell)

    def break_walls_r(self,i,j, window):
        """
        i and j are the respective rows and columns of the cells within
        the maze
        """
        current = (i, j)
        print(f"in break_walls_r: current: {current}")
        self.cells[current[0]][current[1]].visited = True
        while True:
            current_neighbours = self.get_cell_neighbours(current[0], current[1])
            not_visited_list = list(filter(lambda coords: self.cells[coords[0]][coords[1]].visited == False, current_neighbours))
            if len(not_visited_list) == 0:
                current_cell = self.cells[current[0]][current[1]]
                self.draw_cell(window, current_cell)
                return
            else:
                neighbour_to_visit = not_visited_list[random.randrange(len(not_visited_list))]
                neighbour_direction = check_neighbour_direction(current, neighbour_to_visit)
                current_cell = self.cells[current[0]][current[1]]
                neighbour_cell = self.cells[neighbour_to_visit[0]][neighbour_to_visit[1]]
                set_current_and_neighbour_walls(current_cell, neighbour_cell, neighbour_direction)
                self.break_walls_r(neighbour_to_visit[0], neighbour_to_visit[1], window)
        
    def get_cell_neighbours(self, i, j):
        neighbours = []
        if j > 0:
            neighbours.append((i, j-1))
        if i > 0:
            neighbours.append((i-1, j))
        if j < self.num_columns - 1:
            neighbours.append((i, j+1))
        if i < self.num_rows - 1:
            neighbours.append((i+1, j))
        return neighbours

    
            
    
   
        
        

        
        
    


         


        

