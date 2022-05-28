from sympy import lambdify, symbols, cos, sin, pi
import numpy as np


def put(f, x, arg):
    f = lambdify(x, f)
    return f(*arg)


def jacobian(f, x):
    return np.matrix([[fi.diff(xi) for fi in f] for xi in x])


def mult_put(xf, x, args):
    return np.vectorize(lambda f: put(f, x, args))(xf)


def print_values(x, X):
    xX = [str(x[i]) + " = " + str(X[i]) for i in range(len(X))]
    print(*xX, sep=",\t ")


def newtone(xf, x, J, eps):
    X = np.array([z + 1 for z in np.zeros(len(x))])
    XF = mult_put(xf, x, X)
    iterations = 0
    while any(abs(xfi) > eps for xfi in XF):
        JX = mult_put(J, x, X) ** (-1)
        X -= (XF * JX).A1
        XF = mult_put(xf, x, X)
        iterations += 1

        print(str(iterations) + ")", end=" ")
        print_values(x, X)
    return X


def main_newtone():

    # x1 = x1, x2 = x2
    # x3 = y1, x4 = y2
    # x5 = r1, x6 = r2
    # x7 = phi1, x8 = phi2
    # x9 = a1, x10 = l

    # Ax = 3, Ay = -2
    # Bx = 1, By = -1
    # p = 1000, p_ac = 0
    # phi_0 = 0.3, r0 = 5
    # a2 = 3*pi/2

    X = (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) = symbols("x1, x2, x3, x4, x5, x6, x7, x8, x9, x10")
    F = np.array([
        x1 + x5*cos(x9) - 3,
        x3 + x5*sin(x9) + 2,
        x2 + x6*cos(3*pi/2 + x8) - 1,
        x4 + x6*sin(3*pi/2 + x8) + 1,
        x7*x5 + x10 + x8*x6 - 0.3*5,
        x9 + x7 - 3*pi/2,
        x3 - x5,
        x4 - x6,
        1000 * x5 - (1000-0)*x6,
        x10 - x2 + x1
        ])
    J = jacobian(F, X)
    eps = 1e-3

    print("eps = ", eps)
    new_points = newtone(F, X, J, eps)
    print("Answer:")
    print_values(X, new_points)


'''
    X = (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) =\
        symbols("x1, x2, x3, x4, x5, x6, x7, x8, x9, x10")

    A_x = 10
    A_y = - 5
    B_x = 100
    B_y = 30
    r0 = 30
    phi0 = 1.2
    p = 1000

    F = np.array([
        x1 + x5 * cos(x9) - 10,
        x3 + x5 * sin(x9) + 5,
        x2 + x6*cos(3*pi/2 + x8) - 100,
        x4 + x6*sin(3*pi/2 + x8) - 30,
        x7*x5 + x10 + x8*x6 - 1.2*30,
        x9 + x7 - 3*pi/2,
        x3 - x5,
        x4 - x6,
        x10 - x2 + x1,
        1000 * x5 - (1000 - 0) * x6
    ])
'''