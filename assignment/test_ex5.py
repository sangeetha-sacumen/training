import pytest
from ex5 import Rectangle,Triangle,Square,Circle


def test_rectangle():
    """
    test case for Rectangle
    """
    rectangle= Rectangle(6,7)
    area = rectangle.area()
    assert area == 42


def test_triangle():
    """
    test case for Triangle
    """
    triangle= Triangle(8,9)
    area = triangle.area()
    assert area== 36


def test_square():
    """
    test case for Square
    """
    square = Square(4)
    area = square.area()
    assert area == 16


def test_circle():
    """
    test case for Circle
    """
    circle = Circle(9)
    area = circle.area()
    perimeter=circle.perimeter()
    assert area == 254.34
    assert perimeter == 56.52
