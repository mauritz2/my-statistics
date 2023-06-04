from scipy.stats import norm


def calc_lookup_prob_on_cdf(lookup_value: float, mean:float, std_dev:float) -> float:
    # Returns the prob of the lookup value or lower based on the specified normal dist
    return norm.cdf(lookup_value, mean, std_dev)

def calc_prob_between_vals(lower_bound:float, upper_bound:float, mean:float, std_dev:float) -> float:
    prob_below_upper_bound = calc_lookup_prob_on_cdf(upper_bound, mean, std_dev)
    prob_below_lower_bound = calc_lookup_prob_on_cdf(lower_bound, mean, std_dev)
    prob_between_lower_and_upper = prob_below_upper_bound - prob_below_lower_bound
    return prob_between_lower_and_upper