from units import Cell
import time

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_columns,
                 cell_size_x,
                 cell_size_y):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []

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


    


         


        

