
def arctan(x):
    if x<0 or x>1: #checks whether input is within interval [0,1]
        print("error")
    else:
        n = -1 #size of the degree of the polynomial approximating the value
        error = 1.0 #the upper bound on the error
        estimate = 0.0
        while(error > 0.0001): #loops until error <= 0.0001
            n += 1
            error = x ** (2 * n + 1) / (2 * n + 1) #calculates error
            estimate += (((-1)**n)*x**(2*n+1))/(2*n + 1) #accumulates the estimate

        return(estimate, n, error) #returns the final tuple

print(arctan(0.5))
