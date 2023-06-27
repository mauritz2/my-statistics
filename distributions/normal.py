from scipy.stats import norm
from scipy.special import erfinv

def calc_prob_of_value_or_lower_on_cdf(lookup_value: float, mean:float, std_dev:float) -> float:
    return norm.cdf(lookup_value, mean, std_dev)

def calc_prob_between_vals(lower_bound:float, upper_bound:float, mean:float, std_dev:float) -> float:
    prob_below_upper_bound = calc_prob_of_value_or_lower_on_cdf(upper_bound, mean, std_dev)
    prob_below_lower_bound = calc_prob_of_value_or_lower_on_cdf(lower_bound, mean, std_dev)
    prob_between_lower_and_upper = prob_below_upper_bound - prob_below_lower_bound
    return prob_between_lower_and_upper

def convert_x_to_z_score(x:float, mean:float, std_dev:float) -> float:
    z_score = (x - mean) / std_dev 
    return z_score

def calc_inverse_cdf(prob:float, dist) -> float:
    return dist.ppf(prob)

def create_standard_normal_dist():
    standard_norm_dist = norm(loc=0.0, scale=1.0)
    return standard_norm_dist