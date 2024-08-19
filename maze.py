from tkinter import Tk, Canvas, BOTH
from point import Point
from line import Line

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

         
         




window = Window(800, 600)
point_1 = Point(0, 0)
point_2 = Point(100, 100)
test_line = Line(point_1, point_2, "black")
window.draw_line(test_line)
window.wait_for_close()

    

