import pytest
from utils import utils

def test_factorial():
    to_factor = 5
    factorial_sum = utils.factorial(to_factor)
    assert factorial_sum == 120

def test_factorial_0():
    to_factor = 0
    factorial_sum = utils.factorial(to_factor)
    assert factorial_sum == 1

def test_factorial_negative():
    to_factor = -2
    with pytest.raises(ValueError):
        utils.factorial(to_factor)
    

def test_approximate_integral():
    def my_curve(x):
        return x**2 + 1

    area = utils.approximate_integral(0, 1, my_curve, 5)
    assert area == 1.33

def test_approximate_integral():
    def my_curve(x):
        return x**2 + 5

    area = utils.approximate_integral(0, 1, my_curve, 5)
    assert area == 1.33

