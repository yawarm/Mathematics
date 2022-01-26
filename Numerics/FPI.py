import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x + np.cos(x) - np.sin(x)

def g(x):
    return x

xplot = np.ndarray(3)
yplot = np.ndarray(3)



def FPI(guess, err_thresh, plot=0):
    i = 1
    x_old = guess
    if plot:
        xplot[0] = x_old;   yplot[0] = x_old
    x_new = f(guess)
    if plot:
        xplot[1] = x_old;   yplot[1] = x_new
        xplot[2] = x_new;   yplot[2] = x_new
        plt.plot(xplot, yplot, '-k')
    while (np.abs(x_new - x_old) > err_thresh):
        x_old = x_new
        if plot:
            xplot[0] = x_old;   yplot[0] = x_old
        x_new = f(x_old)
        if plot:
            xplot[1] = x_old;   yplot[1] = x_new
            xplot[2] = x_new;   yplot[2] = x_new
            plt.plot(xplot, yplot, '-k')
        i += 1

    return x_new, i, err_thresh

# run code
result = FPI(0, 1e-10, 1)
print(f"Fixed Point with error threshold {result[2]} is: {result[0]}")
print(f"FPI ran {result[1]} iterations")

x = np.linspace(-2, 2, 100)
plt.plot(x, g(x), x, f(x))
plt.grid()
plt.show()
