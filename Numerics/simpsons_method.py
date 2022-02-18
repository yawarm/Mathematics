import numpy as np

def f(x):
    return x*np.sin(x)


def f_fourth_prime(x):
    return -3*np.sin(x) - x*np.cos(x)


def step_calc(lower, upper, decimal_place):
    x = np.linspace(lower, upper, 1000)
    
    steps = np.sqrt(np.sqrt((upper - lower)**5 * max(abs(f_fourth_prime(x)))/(90*10**(-1*decimal_place))))

    return np.ceil(steps)


def simpson_error(lower, upper, steps):
    
    x = np.linspace(lower, upper, 1000)
    h = (upper - lower)/steps

    error = ((upper - lower)*h**4)/(180*max(abs(f_fourth_prime(x))))

    return error


def simpsons_method(lower, upper, steps):
    h = (upper - lower)/steps
    S = 1/3 * (f(lower) + f(upper))
    for i in range(1, steps-1):
        S += 1/3 * (4*f(lower + (2*i-1)*h) + 2*f(lower + 2*i*h))
    
    integral = h*S

    error = simpson_error(lower, upper, steps)

    return integral, error


# run code

lower = 0
upper = 1
decimal_place = 5

steps = step_calc(lower, upper, decimal_place)
print(f'To get precision on {decimal_place} decimals, you must run the method with more than {steps} steps')

integral, error = simpsons_method(lower,upper, int(steps))
print(f'The integral has value {integral} with an error of {error}')
