import sympy as sp

x, y = sp.symbols('x y')

##Part A
f = sp.exp(x)*sp.sin(y)+ y**3
print("Part A:")
print("First derivative of f(x,y) wrt x:", sp.diff(f,x))
print("First derivative of f(x,y) wrt y:", sp.diff(f,y))
print()


##Part B
g = x**2*y + x*y**2
g_x = sp.diff(g,x)
g_y = sp.diff(g,y)
def gradient_vector_magn(a,b):
    return sp.sqrt((g_x.subs({x:a, y: b}))**2 + (g_y.subs({x:a, y: b}))**2)
print("Part B:")
print("The magnitude of g(x,y)'s gradient vector at (1,-1) is:",gradient_vector_magn(1,-1))
print()

#Part C
h = sp.log(x**2 + y**2)
h_x = sp.diff(h,x)
h_y = sp.diff(h,y)
h_xx = sp.diff(h_x,x)
h_yy = sp.diff(h_y,y)
h_xy = sp.diff(h_x,y)

print("Part C:")
print("First derivs: ")
print("h_x= ", h_x)
print("h_y= ", h_y)
print("Second derivs: ")
print("h_xx= ", h_xx)
print("h_yy= ", h_yy)
print("h_xy= ", h_xy)
print("Since h_xx and h_yy are identical with x and y swapped, the function is symmetrical")
print("As well, mixed partial derivatives are always the same, for nice functions, even if the function is not symmetrical like this one")
print()

#Part D
import numpy as np
import matplotlib.pyplot as plt
j = x**3 - 3*x*y + y**3
j_func = sp.lambdify((x, y), j, 'numpy')
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

#Part E
k = x**2 - y**2
k_func = sp.lambdify((x, y), k, 'numpy')
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = k_func(X, Y)
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $k(x, y) = x^2 - y^2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()