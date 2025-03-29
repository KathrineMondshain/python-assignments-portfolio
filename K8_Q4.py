import numpy as np
import matplotlib.pyplot as plt #usual matplotlib
from mpl_toolkits import mplot3d #for 3D plots

def gradient_descent(x0, y0,f, grad_f, alpha, num_iterations):
    """
        Parameters:
        x0, y0: Initial point for the descent.
        f: a function of two variables
        grad_f: the gradient of f
        alpha: Learning rate.
        num_iterations: Number of iterations to perform.
        Returns:
        (x, y): The coordinates of the final point after gradient descent.
        """
    x, y = x0, y0 # Initialize x and y with the initial point
    for i in range(num_iterations):
        # obtain the gradient of f at (x, y)
        grad_x, grad_y = grad_f(x,y)[0], grad_f(x,y)[1]
                # Update x and y by taking a step in the opposite direction of the gradient x = # YOUR CODE HERE
        y = y - alpha*grad_y# YOUR CODE HERE
        x = x - alpha*grad_x
    return x, y

#PART B
def fun_1(x,y):
    return x**2+y**2

def grad_f_1(x,y):
    grad_x = 2*x
    grad_y = 2*y
    return grad_x, grad_y

print(gradient_descent(0.1,0.1,fun_1,grad_f_1,0.1,10))
print(gradient_descent(-1,1,fun_1,grad_f_1,0.01,100))
    #test cases:
    #(x0, y0) = (0.1, 0.1), α = 0.1, max iterations = 10
    #(x0, y0) = (−1, 1), α = 0.01, max iterations = 100



#PART C
def fun_2(x,y):
    return 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)

def grad_f_2(x,y):
    grad_x = -np.exp(-x**2-(y-2)**2)*(-2*x) - 2*np.exp(-x**2-(y+2)**2)*(-2*x)#YOUR CODE HERE
    grad_y = -np.exp(-x**2-(y-2)**2)*(-2*(y-2)) - 2*np.exp(-x**2-(y+2)**2)*(-2*(y+2))#YOUR CODE HERE
    return grad_x, grad_y

    #test cases:
    #(x0, y0) = (0, 1), α = 0.01, max iterations = 10000
    #(x0 , y0 ) = (0, −1), α = 0.01, max iterations = 10000.
print(gradient_descent(0,1,fun_2,grad_f_2,0.01,10000))
print(gradient_descent(0, -1, fun_2,grad_f_2,0.01,10000))


X=np.linspace(-5,5,100)
Y=np.linspace(-5,5,100)
x,y = np.meshgrid(X,Y)
z = np.array(fun_2(x,y))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none') #x,y z are variable names.
fig.show()