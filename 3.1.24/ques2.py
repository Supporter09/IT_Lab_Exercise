class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input()) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        self.n = 3
    def findArea(self):
        p = sum(self.sides) / 2
        area = (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))**(1/2)
        print('The area of the triangle is %.2f' % area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()