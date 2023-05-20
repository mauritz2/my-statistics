
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError(f"{n} needs to be 0 or above")

    factorial_sum = 1
    for i in range(n):
        factorial_sum *= (i + 1)
    return factorial_sum
