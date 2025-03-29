import matplotlib.pyplot as plt
import numpy as np
import math

def normal_density(mean, variance, x):
    return (1/(math.sqrt(2*math.pi*variance)))*np.exp((-(x-mean)**2)/(2*variance))

def plot_distribution(mean, variance): #function plotting the distribution
    plot_range = np.linspace(0,300, 1000)
    function_range=[normal_density(mean, variance, i) for i in plot_range]
    plt.plot(plot_range, function_range) #plots f(x)
    plt.show()

def integration(mean, variance, a, b):
    n = 1000000
    delta_x = (b-a)/n
    x_val = [a]
    approx = 0
    for i in range(1,n+1):
        xi = x_val[i-1] + delta_x
        x_val.append(xi)
        yi = normal_density(mean, variance, xi)
        approx += yi
    approx *= delta_x
    return approx

#plot_distribution(171,(7.1**2))

print("The probability of a randomly chosen man being in between 162cm and 190cm is", integration(171,(7.1**2), 162, 190))
