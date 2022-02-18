import numpy as np

def f(x):
    return x*np.sin(x)


def f_double_prime(x):
    return 2*np.cos(x) - x*np.sin(x)


def step_calc(lower, upper, decimal_place):
    x = np.linspace(lower, upper, 1000)
    
    steps = np.sqrt((upper - lower)**3 * max(abs(f_double_prime(x)))/(6*10**(-1*decimal_place)))

    return np.ceil(steps)


def trapezoidal_error(lower, upper, steps):
    x = np.linspace(lower, upper, 1000)
    h = (upper - lower)/steps

    error = ((upper - lower)*h**2)/12 * max(abs(f_double_prime(x)))

    return error


def trapezoidal_rule(lower, upper, steps):
    h = (upper - lower)/steps
    S = 0.5*(f(lower) + f(upper))
    for i in range(1, steps):
        S += f(lower + i*h)
    
    integral = h*S

    error = trapezoidal_error(lower, upper, steps)

    return integral, error


# run code

lower = 0
upper = 1
decimal_place = 5

steps = step_calc(lower, upper, decimal_place)
print(f'To get precision on {decimal_place} decimals, you must run the method with more than {steps} steps')

integral, error = trapezoidal_rule(lower,upper, int(steps))
print(f'The integral has value {integral} with an error of {error}')
