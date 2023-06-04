from typing import Collection

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError(f"{n} needs to be 0 or above")

    factorial_sum = 1
    for i in range(n):
        factorial_sum *= (i + 1)
    return factorial_sum

def approximate_integral(x_min:int, x_max:int, curve_func:Collection, num_rectangles:int=1000000) -> float:
    # Approximates the integral by estimating the size of n rectangles placed under the curve
    width_of_rectangles = (x_max - x_min) / num_rectangles
    total_sum = 0

    for i in range(1, num_rectangles + 1):
        midpoint = 0.5 * (2 * x_min + width_of_rectangles * (2 * i - 1))
        total_sum += curve_func(midpoint)

    area = total_sum * width_of_rectangles
    return area

