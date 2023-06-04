import matplotlib.pyplot as plt
import statistics
from utils import utils
from distributions import binomial 
from distributions import beta


def plot_binomial_dist():
    AMOUNT_OF_TRIALS = 19
    SUCCESS_PROB = 0.5

    binomial_dist = binomial.calc_binomial_distribution(AMOUNT_OF_TRIALS, SUCCESS_PROB)

    plt.plot(*zip(*sorted(binomial_dist.items())))
    plt.show()

def calc_beta_probability():
    NUM_SUCCESSES = 15
    NUM_FAILURES = 4

    prob_that_underlying_prob_is_above_50_pct = beta.calc_prob_of_being_between_probs(num_successes=NUM_SUCCESSES,
                                          num_failures=NUM_FAILURES,
                                          prob_min=0.5,
                                          prob_max=0.1)
    


    print( 1 - prob_that_underlying_prob_is_above_50_pct)

def plot_beta_dist():
    NUM_SUCCESSES = 15
    NUM_FAILURES = 4
    
    beta_dist = beta.calc_beta_distribution(NUM_SUCCESSES, NUM_FAILURES)
    
    plt.plot(*zip(*sorted(beta_dist.items())))
    plt.show()







#calc_beta_probability()
#plot_beta_dist()
#plot_binomial_dist()

