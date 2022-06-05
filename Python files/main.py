import matplotlib.pyplot as plt
from Spline_2 import spline, der_spline, der_der_spline
import numpy as np
from Intersections import intersection


def print_spline_from_file(file, mark=""):
    f = open(file, "r").readlines()
    M = [m.split(",") for m in f][0]
    X, Y = [], []
    for m in M:
        if m == " ":
            continue
        x, y = m.split()
        X += [float(x)]
        Y += [float(y)]
    plt.plot(X, Y, marker=mark)
    return X, Y


def main():
    plt.figure(figsize=(7, 7))

    a, b = -10, 10
    h = 1e-2
    x0 = np.arange(a, b + h, h)

    X1 = [-7, 11, 3]
    Y1 = [-9, 5, 0]

    X2 = [-15, -12, -6]
    Y2 = [13, 13, -4]

    y01 = spline(X1, Y1, x0)
    y02 = spline(X2, Y2, x0)
    y03 = []

    for i in range(len(y02)):
        y03.append(y01[i]-y02[i])

    plt.plot(x0, y01, label="Spline 1", color='red')
    plt.plot(x0, y02, label="Spline 2", color='orange')
    plt.plot(x0, y03, label="Spline 1 - Spline 2", color='blue')

    root_i = 0

    for i in range(len(y03)-1):
        if y03[i] * y03[i+1] < 0:
            root_i = i

    eps = 1e-8

    x = intersection(x0, y03, x0, root_i, eps)
    print('Intersection point: (', x, '; ', y02[root_i], ')', sep='')
    plt.plot(x, y02[root_i], 'ro')

    y01_d = der_spline(X1, Y1, x0)
    y02_d = der_spline(X2, Y2, x0)

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
    print("Program successfully finished")
