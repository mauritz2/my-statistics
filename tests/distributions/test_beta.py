import pytest
from distributions import beta


def test_calc_beta_probability_at_specific_x_too_high_x():
    with pytest.raises(ValueError):
        probability = beta.calc_beta_prob_density_for_prob(1.2, 1.0, 1.0)


