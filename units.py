def create_point(x_coord, y_coord):
            return Point(x_coord, y_coord)

def create_line(x1, y1, x2, y2, fill_color="black"):
    point_1 = create_point(x1, y1)
    point_2 = create_point(x2, y2)
    return Line(point_1, point_2, fill_color)

def draw_cell_line(x1, y1, x2, y2, canvas, fill_color="black"):
    line = (create_line(x1, y1, x2, y2, fill_color))
    line.draw(canvas)

class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

class Line:
    def __init__(self, point_1, point_2, fill_color):
        self.point_1 = point_1
        self.point_2 = point_2
        self.fill_color = fill_color

    def draw(self, canvas):
        canvas.create_line(self.point_1.x_coord, self.point_1.y_coord, 
                           self.point_2.x_coord, self.point_2.y_coord, 
                           fill=self.fill_color, width=2)

class Cell: 
    def __init__(self, _x1, _x2, _y1, _y2,has_left_wall=True, 
                 has_right_wall=True, has_top_wall=True,
                 has_bottom_wall=True):
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        """
        _x1 _y1 is the top left corner of the cell 
        _x1 _y2 is the bottom left corner of the cell 
        _x2 _y1 is the top right corner of the cell 
        _x2 _y2 is the bottom right corner of the cell
        """

    def draw(self, canvas):
        
        if self.has_left_wall:
            #draw a line from top left to bottom left
            draw_cell_line(self._x1, self._y1, self._x1, self._y2, canvas)
        
        if self.has_right_wall:
            #draw a line from top right to bottom right
            draw_cell_line(self._x2, self._y1, self._x2, self._y2, canvas)
        
        if self.has_top_wall:
            #draw line from top left to top right
            draw_cell_line(self._x1, self._y1, self._x2, self._y1, canvas)
        else:
             draw_cell_line(self._x1, self._y1, self._x2, self._y1, 
                            canvas, fill_color="white")
        
        if self.has_bottom_wall:
            #draw line from bottom left to bottom right
            draw_cell_line(self._x1, self._y2, self._x2, self._y2, canvas)
        else:
            draw_cell_line(self._x1, self._y2, self._x2, self._y2, 
                           canvas, fill_color="white")
             
        
    def draw_move(self, to_cell, canvas, undo=False):
         
         def get_middle_coord(greater_coord, lesser_coord):
              return(0 if greater_coord - lesser_coord == 0 
                     else (greater_coord + lesser_coord) / 2) 
         self_x_middle = get_middle_coord(self._x2, self._x1)
         self_y_middle = get_middle_coord(self._y2, self._y1)
         to_x_middle = get_middle_coord(to_cell._x2, to_cell._x1)
         to_y_middle = get_middle_coord(to_cell._y2, to_cell._y1)
         draw_cell_line(self_x_middle, self_y_middle, 
                        to_x_middle, to_y_middle, canvas, 
                        fill_color="grey" if undo == False else "red") 

        
            