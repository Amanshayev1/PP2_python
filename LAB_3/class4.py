import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def show(self):
        print("Координаты точек: х =", self.x, "y =", self.y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        print("Новые координаты: x =", self.x, "y =", self.y )
        
    def dist(self, other_point):
        print((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        
        
point1 = Point(3, 4)
point2 = Point(5, 6)

point1.show()
point1.move(4, 5)
point1.dist(point2)
