import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import inspect
import math

#---------------------------------

def f(x):
    return np.cos(x) - np.sin(x**2)

#---------------------------------

def bisection(a, b, tol):
    xl = a
    xr = b
    i = 1
    while (np.abs(xl - xr) >= tol):
        c = (xl + xr)/2.0
        prod = f(xl)*f(c)

        if prod > tol:
            xl = c
            i += 1
        elif prod < tol:
            xr = c
            i += 1
    return i, c

#---------------------------------

def num_iterations(a, b, deci_pre):
    n = (deci_pre*(b-a))/np.log10(2)
    return n, deci_pre

#---------------------------------

# number of iterations to get solution within deci_pre desimal places
print("Analysis:")
iterations = num_iterations(0, 1, 10)
print(f"Number of iterations to get within {iterations[1]} decimal places: {math.ceil(iterations[0])}")
print(f"The Bisection method will use {math.ceil(iterations[0]) + 2} iterations to get the result\n")

# run bisection method
answer = bisection(0, 1, 0.5e-10)
print(f"Bisection Method Gives Root At x = {answer[1]}")
print(f"Iterations: {answer[0]}")

# Graphics code
x = np.linspace(-1, 1, 100)
plt.plot(x, f(x))
plt.grid()
plt.show()


#---------------------------------

# Shortcut using fsolve
# how to use fsolve: print(inspect.getargspec(fsolve))

# shortcut = fsolve(f, [-1.5, 1.5])

# print(f"Fsolve gives root(s) at x = {shortcut}")

#---------------------------------
