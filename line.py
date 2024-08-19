class Line:
    def __init__(self, point_1, point_2, fill_color):
        self.point_1 = point_1
        self.point_2 = point_2
        self.fill_color = fill_color

    def draw(self, canvas):
        canvas.create_line(self.point_1.x_coord, self.point_1.y_coord, self.point_2.x_coord, self.point_2.y_coord, fill=self.fill_color, width=2)