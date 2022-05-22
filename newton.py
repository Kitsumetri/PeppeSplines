import numpy as np

'''
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
    X = (x1, x2, x3) = symbols("x1, x2, x3")

    F = np.array([
        x1 ** 2 + x2,
        x1 + x2 + x3,
        x2 ** 2 + x3
    ])
    J = jacobian(F, X)
    a, b = -10, 10
    eps = 1e-3

    print("eps = ", eps)
    new_points = newtone(F, X, J, eps)
    print("Answer:")
    print_values(X, new_points)
'''

'''
x(u) = (2u^3 - 3u^2 + 1)*x_i + (-2u^3+3u^2)x_i+1  +(u^3-2u^2
'''


def get_function(X, Y):
    pass


def get_jacobian():
    pass


def newton():
    pass
