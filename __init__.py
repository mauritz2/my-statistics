import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats import norm
from distributions import binomial, beta, normal 


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


def calc_confidence_interval_span():
    CONFIDENCE_INTERVAL = 0.95
    SAMPLE_MEAN = 10345
    SAMPLE_STD = 552
    N = 45

    left_tail_area_p = (1 - CONFIDENCE_INTERVAL) / 2
    right_tail_area_p = CONFIDENCE_INTERVAL + ((1 - CONFIDENCE_INTERVAL) / 2)

    norm = normal.create_standard_normal_dist()
    left_tail_area_z = normal.calc_inverse_cdf(left_tail_area_p, norm)
    right_tail_area_z = normal.calc_inverse_cdf(right_tail_area_p, norm)
    
    margin_of_error_left = left_tail_area_z * SAMPLE_STD / math.sqrt(N)
    margin_of_error_right = right_tail_area_z * SAMPLE_STD / math.sqrt(N)
    
    confidence_interval_left = SAMPLE_MEAN + margin_of_error_left 
    confidence_interval_right = SAMPLE_MEAN + margin_of_error_right 

    print(confidence_interval_left, confidence_interval_right)


def hypothesis_test():
    MEAN = 10345
    STD_DEV = 552

    high_end_area = 1 - norm.cdf(11641, MEAN, STD_DEV)
    low_end_area = high_end_area # doesn't matter what lookup is here because areas are symmetrical
        
    print(low_end_area + high_end_area)


def fit_simple_linear_regression():
    df = pd.read_csv("data/Fish.csv")
    df = df[df["Weight"] < 1250]
    df["Volume"] = df.Length1 * df.Length2 * df.Length3 * df.Width

    x = df["Volume"]
    y = df["Weight"]

    # Regression by scikit learn
    linear_reg_sklearn = LinearRegression()
    linear_reg_sklearn.fit(df["Volume"].to_numpy().reshape(-1, 1), df["Weight"])
    y_pred = linear_reg_sklearn.predict(df["Volume"].to_numpy().reshape(-1, 1))
    plt.scatter(df["Volume"], df["Weight"],color='g') 
    # TODO - update Volume 
    plt.plot(df["Volume"], y_pred,color='k') 
    plt.show()


    # using the formula to calculate the b1 and b0
    #numerator = 0
    #denominator = 0
    #for i in range(n):
    #    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    #    denominator += (X[i] - x_mean) ** 2
    
    #b1 = numerator / denominator
    #b0 = y_mean - (b1 * x_mean)
    #printing the coefficient
    #print(b1, b0)

    # 


if __name__ == "__main__":
    #calc_beta_probability()
    #plot_beta_dist()
    #plot_binomial_dist()
    #calc_confidence_interval_span()
    #hypothesis_test()
    fit_simple_linear_regression()