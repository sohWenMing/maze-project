from window import Window
from maze import Maze


window = Window(800, 600)
maze = Maze(10, 10, 10, 10, 50, 50, 10)
maze.create_cells()
maze.draw_all_cells(window)
maze.break_entrance_and_exit(window)
maze.break_walls_r(0,0,window)




window.wait_for_close()



