class Point():
    pass

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("Point: (<{}>, <{}>)".format(self.x, self.y))

p = Point(0,0)
p.display()


# print("Point: (<{}>, <{}>".display(self.x, self.y))