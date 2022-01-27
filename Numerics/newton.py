import numpy as np

def f(x):
    return x**2 - 4

def f_prime(x):
    return 2*x

def Newton(guess, maxIT, tol, min_div = 1e-20):
    for i in range(maxIT):
        fprime = f_prime(guess)
        if abs(fprime) < min_div:
            print("Denominator too small: root has multiplicity > 1")
            return (0,-1)
        new_guess = guess - (f(guess)/fprime)
        approxError = abs(new_guess-guess)
        guess = new_guess
        i += 1
        if approxError <= tol:
            print("Tolerance reached")
            return new_guess, i
    return new_guess, i

result = Newton(0, 20, 1e-5)
print(f"The root is found to be: {result[0]}")
print(f"Iterations: {result[1]}")
