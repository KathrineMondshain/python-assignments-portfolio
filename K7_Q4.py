import numpy as np
from scipy.special import gamma

#Defining given information
scores = [92.64,79.00,84.79,97.41,93.68,65.23,84.50,73.49,73.97,79.11]
national_average = 75

def t_distribution_pdf(x, nu):
    """
    Compute the probability density of the t-distribution
    at a given point x with nu degrees of freedom.
    Parameters:
    x (float): The point at which to evaluate the density.
    nu (int): The degrees of freedom of the t-distribution.
    Returns:
    density (float): The probability density at point x for
    the t-distribution with nu degrees of freedom.
    """
    coeff = gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * gamma(nu / 2))
    density = coeff * (1 + x**2 / nu) ** (-0.5 * (nu + 1))
    return density

def find_t_star(prob, nu, x_start=0, x_end=20, num_points=10000):
    """
    Find the t-value t* for a given cumulative probability
    and degrees of freedom.
            Parameters:
            prob (float): The cumulative probability (between 0 and 1).
            nu (int): The degrees of freedom of the t-distribution.
            x_start (float): The start point for numerical integration.
            x_end (float): The end point for numerical integration.
            20 will almost always be big enough.
            num_points (int): The number of points to use in
            the numerical integration.
    Returns:
    float: The t-value t* such that the area between [-t*, t*]
    equals the given probability.
    """

    # Define the x values
    x = np.linspace(x_start, x_end, num_points)
    # Apply the density function to the x values
    y = t_distribution_pdf(x, nu)
    # This next line is the integration (exercise: why does this work?)
    cdf = np.cumsum(y) * (x[1] - x[0])
    # Find the t-value where the cumulative probability reaches half of the required probability
    target_half_prob = prob / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    t_star = x[index]
    print("t_star:", t_star)
    return t_star

#Function to find mean of a list
def mean(list):
    sum = 0
    for i in list:
        sum += i
    #print("mean:", sum / len(list))
    return sum / len(list)

#Function to find standard deviation of a list
def stdev(list):
    sum = 0
    for i in list:
        sum += (i - mean(list)) ** 2
    #print("stdev:", np.sqrt(sum/(len(list)-1)))
    return np.sqrt(sum/(len(list)-1))

#Function to calculate t_0 value of a list based on a mu_0 value
def calc_t_0(list, mu_0):
    t_0 = (mean(list) - mu_0) / (stdev(list) / np.sqrt(len(list)))
    print("t_0:", t_0)
    return t_0

#Function checking whether t_0 is within the t_star set
def check_t(t_0,t_star):
    return t_0 < t_star and t_0 > -t_star #Returns boolean

print("t-test result:", check_t(calc_t_0(scores,national_average),find_t_star(0.95,len(scores)-1)))

print("Since the result is false, we can reject the null hypothesis and conclude that mu is not 75.")
print("Since t_0 is above the upper bound of [-t_star,t_star], the true average score is higher than the national average.")
print("This means that the new teaching techniques are working.")