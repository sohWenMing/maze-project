from tkinter import Tk, Canvas, BOTH
from units import Line, Point, Cell

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(expand=1, fill=BOTH)
        self.__is_running = False

    def redraw(self):
            self.__root.update_idletasks()
            self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running == True:
             self.redraw()
    
    def close(self):
         self.__is_running = False

    def get_canvas(self):
         return self.__canvas
    
    def draw_line(self, line):
         line.draw(self.__canvas)
    
    def draw_cell(self, cell):
         cell.draw(self.__canvas)

window = Window(800, 600)
test_cell = Cell(50, 100, 10, 60)
test_other_cell = Cell(150, 200, 60, 110)
window.draw_cell(test_cell)
window.draw_cell(test_other_cell)
test_cell.draw_move(test_other_cell, window.get_canvas(), undo=True)
window.wait_for_close()

    
