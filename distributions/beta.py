from utils import utils

def calc_beta_prob_density_for_prob(prob:float, num_successes:float, num_failures:float) -> float:
    # The higher the probability density value, the more likely that the given prob is close 
    # to the probability observed based on the num_successes and num_failures
    # In the beta distribution the prob is the x and the probability density is the y
    if prob < 0.0 or prob > 1.0:
        raise ValueError("The input probability has to be between 0% and 100%")
    numerator = prob ** (num_successes - 1.0) * (1.0 - prob) ** (num_failures - 1.0)
    # Denominator is the same for all values of x (prob) - used to scale output
    denominator = (1.0 * utils.factorial(num_successes - 1) * utils.factorial(num_failures - 1)) / (1.0 * utils.factorial(num_successes + num_failures - 1))
    prob_density = numerator / denominator
    return prob_density

def calc_beta_distribution(num_successes:float, num_failures:float) -> list[float, float]:
    beta_dist = {}
    for i in range(101):
        prob = i / 100.0
        prob_density = calc_beta_prob_density_for_prob(prob, num_successes, num_failures)
        beta_dist[prob] = prob_density
    return beta_dist

def calc_prob_of_being_between_probs(num_successes:float, num_failures:float, prob_min:float, prob_max:float=1.0) -> float: 
    beta_curve_func = lambda x: calc_beta_prob_density_for_prob(x, num_successes, num_failures)
    probability = utils.approximate_integral(prob_min,
                                             prob_max,
                                             beta_curve_func)
    return probability