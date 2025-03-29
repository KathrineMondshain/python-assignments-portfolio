import numpy as np
def funny(x):
    #return y
    if x<=-1:
        return 0
    elif x>=1:
        return 8
    else:
        return -(1/(1-x**(10**250)))

print(funny(0.99))