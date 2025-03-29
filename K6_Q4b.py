import numpy as np
import math

mean = 171
variance = 7.1**2

def prob_density(x):
    return (1/50)*np.exp(-(1/50)*x)

def expected_val(function1):

    n = 10000000 #Approaching infinity
    a = 0 #Approaching negative infinity
    b = 10000 #Approaching infinity

    delta_x = (b-a)/n
    x_val = [a]
    approx = 0
    for i in range(1,n+1):
        xi = x_val[i-1] + delta_x
        x_val.append(xi)
        yi = function1(xi)*xi
        approx += yi
    approx *= delta_x
    return approx

#print("The probability of a randomly chosen man being in between 162cm and 190cm is", integration(normal_density, 162, 190))
print(expected_val(prob_density), "Yes, this is the value I was expecting, since the average time between pandemics is 50 years")