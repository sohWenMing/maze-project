from units import Cell
import time
import random

def check_neighbour_direction(current, neighbour):
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
        is_left = True
    #check for neighbour right of current
    if neighbour_j > current_j:
        is_right = True
    #check for neighbour above current
    if neighbour_i < current_i:
        is_up = True
    #check for neighbour below current
    if neighbour_i > current_i:
        is_down = True

    return {
        is_left,
        is_right,
        is_up, 
        is_down
    }
    

    

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
        while len(self.cells) < self.num_rows:
            self.cells.append([])
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
        time.sleep(1)

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

    def break_walls_r(self,i,j):
        """
        i and j are the respective rows and columns of the cells within
        the maze
        """
        current = (i, j)
        self.visited_for_break.append(current)
        current_neighbours = self.get_cell_neighbours(current)
        for neighbour in current_neighbours:
            if neighbour not in self.visited_for_break and neighbour not in self.to_visit_for_break:
                self.to_visit_for_break.append(neighbour)
        if len(self.to_visit_for_break) == 0:
            return
        else:
            neighbour_to_visit = self.to_visit_for_break.pop(random.randrange(len(self.to_visit_for_break)))

            #compare the coordinates of current to neighbour_to_visit
           




        
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

    
            
    
   
        
        

        
        
    


         


        

