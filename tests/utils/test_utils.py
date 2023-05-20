import pytest
from utils.utils import factorial

def test_factorial():
    to_factor = 5
    factorial_sum = factorial(to_factor)
    assert factorial_sum == 120

def test_factorial_0():
    to_factor = 0
    factorial_sum = factorial(to_factor)
    assert factorial_sum == 1

def test_factorial_negative():
    to_factor = -2
    with pytest.raises(ValueError):
        factorial(to_factor)
    


