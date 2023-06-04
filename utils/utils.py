import math
from statistics import mean
from scipy import integrate
from scipy.stats import norm
from typing import Collection

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError(f"{n} needs to be 0 or above")

    factorial_sum = 1
    for i in range(n):
        factorial_sum *= (i + 1)
    return factorial_sum

def calc_integral(x_min:int, x_max:int, curve_func:Collection) -> float:
    # Quad returns both the integral and the upper bound of the error - only returning integral here
    return integrate.quad(curve_func, x_min, x_max)[0]

def approximate_integral(x_min:int, x_max:int, curve_func:Collection, num_rectangles:int=10000) -> float:
    # Approximates the integral by estimating the size of n rectangles placed under the curve
    width_of_rectangles = (x_max - x_min) / num_rectangles
    total_sum = 0

    for i in range(1, num_rectangles + 1):
        midpoint = 0.5 * (2 * x_min + width_of_rectangles * (2 * i - 1))
        total_sum += curve_func(midpoint)

    area = total_sum * width_of_rectangles
    return area


def calc_weighted_mean(values: list[float, float]) -> float:
    numerator = sum({val * weight for val, weight in values.items()})
    denominator = sum(values.values())
    return numerator / denominator

def calc_variance(values:list[float], is_sample=False) -> float:
    avg = mean(values)
    n = len(values) - 1 if is_sample else len(values)
    variance = sum([(x - avg) ** 2 for x in values]) / n
    return variance

def calc_std_deviation(values:list[float], is_sample=False) -> float:
    return math.sqrt(calc_variance(values, is_sample=is_sample))

def calc_normal_prob_density_func(x:float, avg:float, std_dev:float):
    norm_pdf = (1 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * math.exp(-1.0 * ((x - avg) ** 2 / (2.0 * std_dev ** 2)))
    return norm_pdf
