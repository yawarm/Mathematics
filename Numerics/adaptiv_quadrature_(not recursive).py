import numpy as np

def f(x):
    return x*np.sin(x)


def f_fourth_prime(x):
    return -3*np.sin(x) - x*np.cos(x)


def simpsons_method(lower, upper, steps):
    h = (upper - lower)/steps
    S = 1/3 * (f(lower) + f(upper))
    for i in range(1, steps-1):
        S += 1/3 * (4*f(lower + (2*i-1)*h) + 2*f(lower + 2*i*h))
    
    integral = h*S

    return integral


def adaptiv_quadrature_simpson(lower, upper, TOL):

    stack = []
    stack.append(lower)
    stack.append(upper)

    integral = 0
    iteration = 0

    while len(stack) != 0:

        bb = stack.pop()
        aa = stack.pop()

        integral_1 = simpsons_method(aa, bb, 4)

        c = (aa+bb)/2

        integral_2 = simpsons_method(aa, c, 4) + simpsons_method(c, bb, 4)

        iteration += 1

        if abs(integral_2 - integral_1) < 15*TOL*(bb-aa):
            integral += integral_2
        else:
            stack.append(c)
            stack.append(bb)
            stack.append(aa)
            stack.append(c)
        if iteration > 10000:
            print('Danger of infinite while loop')
            break
    
    return integral, iteration


# run code

integral, iteration = adaptiv_quadrature_simpson(0, 1, 10**(-6))

print(f'The integral has value: {integral} after {iteration} iterations')
