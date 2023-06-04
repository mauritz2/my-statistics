import pytest
import statistics
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
    assert area == 5.33


def test_calc_weighted_mean():
    values = {90: 0.2, 80:0.2, 63:0.2, 87:0.4}
    weighted_mean = utils.calc_weighted_mean(values)
    assert weighted_mean == 81.4


def test_calc_variance():
    values = [0, 1, 5, 7, 9, 10, 14]
    variance = utils.calc_variance(values)
    assert pytest.approx(variance, 0.00001) == 21.387755


def test_calc_variance_is_sample():
    values = [0, 1, 5, 7, 9, 10, 14]
    variance = utils.calc_variance(values, is_sample=True)
    assert pytest.approx(variance, 0.00001) == 24.95238


def test_calc_std_deviation():
    values = [0, 1, 5, 7, 9, 10, 14]
    std_deviation = utils.calc_std_deviation(values)
    assert pytest.approx(std_deviation, 0.00001) == 4.624689


def test_calc_std_deviation_is_sample():
    values = [0, 1, 5, 7, 9, 10, 14]
    std_deviation = utils.calc_std_deviation(values, is_sample=True)
    assert pytest.approx(std_deviation, 0.00001) == 4.9952358255

def test_calc_prob_density_function():
    x = 1
    avg = 1
    std_deviation = 1
    norm_pdf = utils.calc_normal_prob_density_func(x, avg, std_deviation)
    assert pytest.approx(norm_pdf, 0.01) == 0.398
