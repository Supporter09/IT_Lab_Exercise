import math

class LengthException(Exception):
    pass

class InvalidTriangleException(Exception):
    pass

class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise LengthException("Width and height must be greater than 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def set_width(self, new_width):
        if new_width <= 0:
            raise LengthException("Width must be greater than 0")
        self.width = new_width

    def set_height(self, new_height):
        if new_height <= 0:
            raise LengthException("Height must be greater than 0")
        self.height = new_height

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise LengthException("Radius must be greater than 0")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise LengthException("All sides of the triangle must be greater than 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise InvalidTriangleException("Invalid triangle: The sum of any two sides must be greater than the third side")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c))**0.5

    def perimeter(self):
        return self.a + self.b + self.c
    
    def get_height_a(self):
        return (2 * self.area()) / self.a

    def get_height_b(self):
        return (2 * self.area()) / self.b

    def get_height_c(self):
        return (2 * self.area()) / self.c

# Example usage
try:
    rectangle = Rectangle(4, 5)
    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
except LengthException as e:
    print(str(type(e)) + ' was raised')

try:
    circle = Circle(3)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())
except LengthException as e:
    print(str(type(e)) + ' was raised')

try:
    triangle = Triangle(-1, 4, 5)
    print("Triangle Area:", triangle.area())
    print("Triangle Perimeter:", triangle.perimeter())
except (LengthException, InvalidTriangleException) as e:
    print(str(type(e)) + ' was raised')
