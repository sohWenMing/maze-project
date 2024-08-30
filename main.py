from window import Window
from maze import Maze


window = Window(1000, 800)
maze = Maze(10, 10, 12, 12, 50, 50, 10)
maze.create_cells()
maze.draw_all_cells(window)
maze.break_entrance_and_exit(window)
maze.break_walls_r(0,0,window)
maze.reset_cells_visited()
maze.solve(window)

window.wait_for_close()



