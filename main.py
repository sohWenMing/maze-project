from window import Window
from maze import Maze


window = Window(800, 600)
maze = Maze(10, 10, 3, 3, 50, 50)
maze.create_cells()
maze.draw_all_cells(window)
maze.break_entrance_and_exit(window)




window.wait_for_close()



