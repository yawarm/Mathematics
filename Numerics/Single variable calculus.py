import numpy as np

def f(x):
    return #insert function here

def fprime(x):
    return #insert the derivative here

def newtons_method():
    guess = float(input('Enter zero point guess: '))
    for i in range(1, 10):
        nextGuess = guess - f(guess)/fprime(guess)
        print(nextGuess)
        guess = nextGuess


def fixed_point(x_null, iteration):
    for i in range(iteration):
        x_n = f(x_null)
        x_null = x_n
    return x_n


def trapezoidal_rule():
    lower = float(input('Lower limit: '))
    upper = float(input('Upper limit: '))
    n = int(input('Number of iterations: '))
    h = (upper - lower)/n
    Integral = 0
    for i in range(0, n+1):
        x = lower + h*i 
        if i == 0:
            Integral += f(x)/2
        elif i == n:
            Integral += f(x)/2
        else:
            Integral += f(x)
    return h*Integral


def midpoint_method():
    lower = float(input('Lower limit: '))
    upper = float(input('Upper limit: '))
    n = int(input('Number of iterations: '))
    h = (upper - lower)/n
    Integral = 0
    for i in range(1, n+1):
        x = lower + (i - 0.5)*h
        Integral += f(x)
    return h*Integral


def simpsons_method():
    lower = float(input('Lower limit: '))
    upper = float(input('Upper limit: '))
    n = int(input('Number of iterations: '))
    h = (upper - lower)/n
    Integral = 0
    for i in range(0, n+1):
        x = lower + h*i 
        if i == 0 or i == n:
            Integral += f(x)
        elif i%2 == 0:
            Integral += 2*f(x)
        elif i %2 != 0:
            Integral += 4*f(x)
    return (h/3) * Integral + 0
