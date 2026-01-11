class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"X is {self.x} and Y is {self.y}")

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


p1 = Point(3, 2)
p2 = Point(6, 3)

p1.show()

p3 = p1 + p2   
p3.show()
