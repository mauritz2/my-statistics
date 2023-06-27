import pytest
from distributions import normal


def test_lookup_prob_on_cdf_avg():
    lookup = 10
    mean = 10
    std_dev = 5

    prob_of_lookup_or_lower = normal.calc_prob_of_value_or_lower_on_cdf(lookup, mean, std_dev)
    assert prob_of_lookup_or_lower == 0.5

    lookup = 11
    prob_of_lookup_or_lower = normal.calc_prob_of_value_or_lower_on_cdf(lookup, mean, std_dev)
    assert prob_of_lookup_or_lower > 0.5

    lookup = 9
    prob_of_lookup_or_lower = normal.calc_prob_of_value_or_lower_on_cdf(lookup, mean, std_dev)
    assert prob_of_lookup_or_lower < 0.5


def test_prob_between_vals():
    lower = 20
    upper = 30
    mean = 42
    std_dev = 8

    prob_between_vals = normal.calc_prob_between_vals(lower, upper, mean, std_dev)
    assert pytest.approx(prob_between_vals, 0.01) == 0.0638


def test_convert_x_to_z_score():
    x = 150000
    mean = 140000
    std_dev = 3000
    z_score = normal.convert_x_to_z_score(x, mean, std_dev)
    assert pytest.approx(z_score, 0.01) == 3.333

def test_calc_value_of_prob_on_inverse_cdf():
    x = 0.95
    loc=64.43
    scale=2.99
    x_value_at_prob = normal.calc_inverse_cdf(x, loc, scale)    
    assert pytest.approx(x_value_at_prob, 0.01) == 69.34

def test_calculate_inverse_cdf():
    norm = normal.create_standard_normal_dist()
    right_tail_area_z = normal.calc_inverse_cdf(0.975, norm)
    assert pytest.approx(1.9599, 0.01) == right_tail_area_z