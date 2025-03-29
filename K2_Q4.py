import numpy as np

#Recursive function to find a root using bisection

def roots(f, a, b):
    if(f(a) == 0): #a is the root
        print(round(a,10))
    elif(f(b) == 0): #b is the root
        print(round(b,10))
    elif(f(a)>0 and f(b)<0 or f(b)>0 and f(a)<0): #the root is between a and b
        if((b-a) > 10**(-10)): #the root isn't precise enough
            roots(f, a, (a+b)/2)
            roots(f, (a+b)/2, b)
        else: #the root is precise enough
            print(round(a, 10))

def function1(x):
    #Produces a divide by zero error in ln(x) b/c it is undefined at 0
    return float(np.exp(x) + np.log(x))

def function2(x):
    return np.arctan(x) - x**2

def function3(x):
    return np.sin(x)/np.log(x)

def function4(x):
    #The function does have a root,, but it is undetectable with IVT with these endpoints
    return np.log(np.cos(x))

roots(function4,5,7)