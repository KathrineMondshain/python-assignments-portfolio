import matplotlib.pyplot as plt
import numpy as np
import math

mean = 171
variance = 7.1**2

def normal_density(x):
    return (1/(math.sqrt(2*math.pi*variance)))*np.exp((-(x-mean)**2)/(2*variance))

def dosage(x):
    return 2.38*x**2

def average(function1, function2):

    n = 1000000 #Approaching infinity
    a = n*-1 #Approaching negative infinity
    b = n #Approaching infinity

    delta_x = (b-a)/n
    x_val = [a]
    approx = 0
    for i in range(1,n+1):
        xi = x_val[i-1] + delta_x
        x_val.append(xi)
        yi = function1(xi)*function2(xi)
        approx += yi
    approx *= delta_x
    return approx

#print("The probability of a randomly chosen man being in between 162cm and 190cm is", integration(normal_density, 162, 190))
print(average(normal_density, dosage))