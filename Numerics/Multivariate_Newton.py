import autograd as ad
from autograd import grad, jacobian
import autograd.numpy as npp
import numpy as np

#--------------------------

#Example of use

# def ex_f(x):
#     return x[0]**2 + x[1]**3

# z = np.array([5,3], np.dtype=="float")
# print(z)

# print(ex_f(z))

# jacobian_func = jacobian(ex_f)
# print(jacobian_func(z))

#--------------------------

# Defining functions and jacobians here:

func1 = lambda x: x[0] - 2*x[1] + 3*x[2] - 7;   jac_1 = jacobian(func1)
func2 = lambda x: 2*x[0] + x[1] + x[2] - 4; jac_2 = jacobian(func2)
func3 = lambda x: -3*x[0] + 2*x[1] - 2*x[2] + 10;   jac_3 = jacobian(func3)


#----------------------------

def multivariate_newton(eq_num, var_num, maxIT):
    if eq_num != var_num:
        print("Kan ikke løse disse enda")
        pass
    i = 0;  guess_arr = []
    for _ in range(var_num):
        guess_in = float(input("Gi inn ditt gjett som desimaltall: "))
        guess_arr.append(guess_in)
    guess = np.array(guess_arr, dtype="float").reshape(var_num, 1)

    while (i < maxIT):
        func_eval = np.array([func1(guess), func2(guess), func3(guess)]).reshape(eq_num, 1)

        flat_guess = guess.flatten()

        jacobi = np.array([jac_1(flat_guess), jac_2(flat_guess), jac_3(flat_guess)])
        jacobi = jacobi.reshape(var_num, eq_num)

        new_guess = guess - np.linalg.inv(jacobi)@func_eval

        guess = new_guess;  i += 1

    return new_guess, i

resultat = multivariate_newton(3, 3, 100)
print(f"\n Løsningen på likningssystemet er: {resultat[0]}")
print(f"Iterasjoner: {resultat[1]}")
