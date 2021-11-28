"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.

Print number of sides, area of each object and Perimeter of Circle object
"""


class Shape():
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        print("Area of shape: ", number_of_sides)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length= length
        self.width= width

    def area(self): 
        return self.length*self.width

class Triangle(Shape):
    def __init__(self, base,height):
        self.base= base
        self.height= height
    def area(self):
        return 0.5*self.base*self.height

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return super().area()

class Circle(Shape):
    def __init__(self, radius):
        self.pi= 3.14
        self.radius= radius

    def area(self):
        return self.pi*self.radius*self.radius

    def perimeter(self):
        return self.pi*2*self.radius

if __name__ == "__main__":
    shape= Shape(4)
    rectangle= Rectangle(6,7)
    triangle= Triangle(8,9)
    square= Square(4)
    circle= Circle(9)
    print("Area of Rectangle: ", rectangle.area())
    print("Area of Triangle: ", triangle.area())
    print("Area of Square: ", square.area())
    print("Area of Circle: ", circle.area())
    print("Perimeter of Circle: ", circle.perimeter())
        

        




    
