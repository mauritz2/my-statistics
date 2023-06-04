import matplotlib.pyplot as plt
from distributions import binomial 
from scipy.stats import beta


def plot_binomial_dist():
    AMOUNT_OF_TRIALS = 2
    SUCCESS_PROB = 0.5

    binomial_dist = binomial.calc_binomial_distribution(AMOUNT_OF_TRIALS, SUCCESS_PROB)

    plt.plot(*zip(*sorted(binomial_dist.items())))
    plt.show())
