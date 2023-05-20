from distributions import binomial


def test_calc_binomial_coefficient():
    num_trials = 3
    num_successes = 2
    expected_permutations = 3.0
    binomial_coefficient = binomial._calc_binomial_coefficient(num_trials, num_successes)
    assert binomial_coefficient == expected_permutations

def test_calc_binomial_coefficient_single_possible_permutation():
    num_trials = 6
    num_successes = 6
    expected_permutations = 1
    binomial_coefficient = binomial._calc_binomial_coefficient(num_trials, num_successes)
    assert binomial_coefficient == expected_permutations

def test_calc_binomial_coefficient_alot_of_permutations():
    num_trials = 2000
    num_successes = 1
    expected_permutations = 2000.0
    binomial_coefficient = binomial._calc_binomial_coefficient(num_trials, num_successes)
    assert binomial_coefficient == expected_permutations

def test_calc_binomial_distribution():
    num_successes = 8
    num_trials = 10
    success_prob = 0.9
    expected_probability = 0.19371024449999993
    assert expected_probability == binomial._calc_binomial_distribution_value(num_successes, num_trials, success_prob)

def test_calc_binomial_distribution_result_len():
    num_trials = 10
    expected_dict_length = num_trials + 1
    success_prob = 0.9
    assert expected_dict_length == len(binomial.calc_binomial_distribution(num_trials, success_prob))

def test_calc_binomial_distribution_result_len():
    num_trials = 10
    success_prob = 0.9
    binomial_dist = binomial.calc_binomial_distribution(num_trials, success_prob)
    assert binomial_dist[8] == 0.19371024449999993

