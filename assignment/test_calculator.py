import pytest
from calculator import addition, subtraction,multiplication,division

def test_addition():
    """
    test case for addition method
    """
    result=addition(10,10)
    assert result == 20


def test_subtraction():
    """
    test case for subtraction method
    """
    result=subtraction(20,10)
    assert result == 10


def test_multiplication():
    """
    test case for multiplication method
    """
    result=multiplication(8,5)
    assert result == 40


def test_division():
    """
    test case for division method
    """
    result=division(10,2)
    assert result == 5
