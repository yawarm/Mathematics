import numpy as np

def f(x):
    return x**2


def f_double_prime(x):
    return 2 + 0*x


def step_calc(lower, upper, decimal_place):
    x = np.linspace(lower, upper, 1000)
    
    steps = np.sqrt((upper - lower)**3 * max(abs(f_double_prime(x))) / (12*10**(-1*decimal_place)))

    return np.ceil(steps)


def midpoint_error(lower, upper, steps):

    x = np.linspace(lower, upper, 1000)
    h = (upper - lower)/steps

    error = (upper - lower)*h**2/(24*max(abs(f_double_prime(x))))

    return error


def midpoint_method(lower, upper, steps):
    h = (upper - lower)/steps
    S = 0
    for i in range(1, steps):
        S += f((lower + h/2) + i*h)
    
    integral = S*h

    error = midpoint_error(lower, upper, steps)

    return integral, error


# run code

lower = 0
upper = 1
decimal_place = 5

steps = step_calc(lower, upper, decimal_place)
print(f'To get precision on {decimal_place} decimals, you must run the method with more than {steps} steps')

integral, error = midpoint_method(lower,upper, int(steps))
print(f'The integral has value {integral} with an error of {error}')
