import numpy as np

#Sets the delta x constant throughout the program
delta_x = 10**-8

#The derivativeApproximation function takes in the original function and any x value and
# returns an approximated f'(x) value based on the Central Difference Derivative
def derivativeApproximation(function, x):
    fPrimeOfX = (function(x + delta_x) - function(x - delta_x))/(2*delta_x)
    return fPrimeOfX

#The linearApproximation function takes in the original function, the given c value, and an x value and
# returns the L(x) for that c and x
def linearApproximation(function, c, x):
    LofX = function(c)+derivativeApproximation(function, c)*(x-c)
    return LofX

#The main function is where we are looking for the appropriate x1 and v2 values given the function, c, and ERROR
def main(function, c, ERROR):
    x1 = c
    x2 = c
    #x1 starts at c and decreases until the absolute value difference between f(x1) and L(x1) is equal to the ERROR
    while abs(function(x1)-linearApproximation(function,c,x1)) < ERROR:
        x1 -= 10**-4
    #x2 starts at c and increases until the absolute value difference between f(x2) and L(x2) is equal to the ERROR
    while abs(function(x2)-linearApproximation(function,c,x2)) < ERROR:
        x2 += 10**-4

    #returns x1 and x2 as a tuple
    return (x1, x2)

def function1(x):
    return x**2

def function2(x):
    return np.sin(x)

def function3(x):
    return np.exp(x)

print("x1 and x2 for f1 are: ", main(function1, 1, 0.1))
print("x1 and x2 for f2 are: ", main(function2, np.pi/4, 0.05))
print("x1 and x2 for f3 are: ", main(function3, 0, 0.01))