import pytest
from distributions import normal


def test_lookup_prob_on_cdf_avg():
    lookup = 10
    mean = 10
    std_dev = 5

    prob_of_lookup_or_lower = normal.calc_lookup_prob_on_cdf(lookup, mean, std_dev)
    assert prob_of_lookup_or_lower == 0.5

    lookup = 11
    prob_of_lookup_or_lower = normal.calc_lookup_prob_on_cdf(lookup, mean, std_dev)
    assert prob_of_lookup_or_lower > 0.5

    lookup = 9
    prob_of_lookup_or_lower = normal.calc_lookup_prob_on_cdf(lookup, mean, std_dev)
    assert prob_of_lookup_or_lower < 0.5


def test_prob_between_vals():
    lower = 20
    upper = 30
    mean = 42
    std_dev = 8

    prob_between_vals = normal.calc_prob_between_vals(lower, upper, mean, std_dev)
    assert pytest.approx(prob_between_vals, 0.01) == 0.0638