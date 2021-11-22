"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.
Print number of sides, area of each object and Perimeter of Circle object
import math
class Shape(object):
    def __init__(self, sides):
        self.sides= sides
class Rectangle(Shape):        
    def __init__(self, length, width):  
    super().__init__(length,width)
        self.length = length
        self.width = width
    def area(self):
        print("Are of Rectangle")
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + 2 * self.width
class Triangle(Shape):
    def __init__(self,a,b,c):
    super().__init(a,b,c)
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c)))**0.5
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def area(self):
        print("Area of a square")
        area = super().area()
        return area - 1
class Circle(Shape):
    def __init__(self,radius):
    super().__init(radius)
        self.radius=radius
    def area(self):
        area=math.pi*self.radius**2
    def perimeter(self):
        perimeter=2*math.pi*self.radius
if __name__ == "__main__":
   Circle = circle(5)
    print("Area of a Circle: ", Circle.area())
    print("Perimeter of a square: ", Circle.perimeter())
