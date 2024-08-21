from window import Window
from maze import Maze


window = Window(800, 600)
maze = Maze(0, 0, 3, 3, 50, 50)
maze.create_cells()
print(maze.cells)
maze.draw_all_cells(window)




window.wait_for_close()



