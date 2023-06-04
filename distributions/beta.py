from utils import utils

def calc_beta_probability_at_specific_x(lookup_prob:float, num_successes:float, num_failures:float) -> float:
    if lookup_prob < 0.0 or lookup_prob > 1.0:
        raise ValueError("You can only lookup probabilities between 0% and 100%")
    numerator = lookup_prob ** (num_successes - 1.0) * (1.0 - lookup_prob) ** (num_failures - 1.0)
    denominator = (1.0 * utils.factorial(num_successes - 1) * utils.factorial(num_failures - 1)) / (1.0 * utils.factorial(num_successes + num_failures - 1))
    return numerator / denominator 