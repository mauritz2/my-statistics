from utils.utils import factorial

def _calc_binomial_coefficient(num_trials: int, num_successes:int) -> float:
    # Binomial coefficient is the amount of ways you could've ended up with this amount of 
    # successes for this amount of trials
    # Put in another way: the number of ways to choose k items from n items without repetition
    return factorial(num_trials) / (factorial(num_successes) * factorial(num_trials - num_successes))

def _calc_binomial_distribution_value(num_successes:int, num_trials:int, success_prob:float) -> float:
    binomial_coefficient = _calc_binomial_coefficient(num_trials, num_successes)
    failure_prob = 1.0 - success_prob
    num_failures = num_trials - num_successes
    probability_of_occuring = success_prob ** num_successes
    probability_of_not_occuring = failure_prob ** num_failures

    binomial_distribution = binomial_coefficient * probability_of_occuring * probability_of_not_occuring
    return binomial_distribution

def calc_binomial_distribution(num_trials:int, success_prob:float) -> dict[int, float]:
    binomial_dist = {}
    for num_successes in range(num_trials + 1):
        probability = _calc_binomial_distribution_value(num_successes, num_trials, success_prob)
        binomial_dist[num_successes] = probability
    return binomial_dist