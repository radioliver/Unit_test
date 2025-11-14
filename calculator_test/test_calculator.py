import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(2,3) == 5
    assert sum(-2,-3) == -5
    assert sum(-1,1) == 0
    assert sum(0,0) == 0

def test_subtract():
    assert subtract(2,3) == -1
    assert subtract(-2,-3) == 1
    assert subtract(-1,1) == -2
    assert subtract(0,0) == 0

    #cd .\calculator_test\        python -m pytest test_calculator.py -v

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-2,-3) == 6
    assert multiply(-1,1) == -1
    assert multiply(0,0) == 0

def test_divide():
    assert divide(2,3) == 0.6666666666666666
    assert divide(-2,-3) == 0.6666666666666666
    assert divide(-1,1) == -1
    assert divide(0,0) == "Error division by zero!!!"