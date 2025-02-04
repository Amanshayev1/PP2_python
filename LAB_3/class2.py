class Shape:
    def __init__(self):
        self.area_value = 0
        
    def area(self):
        return self.area_value
        
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        
    def area(self):
        return self.length * self.length
    
class Rectangle(Shape): 
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width


shape = Shape()
print("Площадь фигуры по умолчанию:", shape.area())

square = Square(5)
print("Площадь квадрата со стороной 5:", square.area())

rectangle = Rectangle(3, 8)
print("Площадь прямоугольника со сторонами 3 и 8:", rectangle.area())