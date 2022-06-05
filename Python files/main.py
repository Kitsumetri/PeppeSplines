import matplotlib.pyplot as plt
from Spline_2 import spline, der_spline, der_der_spline
import numpy as np
from Intersections import intersection, distance


def print_spline_from_file(file):
    f = open(file, "r").readlines()
    M = [m.split(",") for m in f][0]
    X, Y = [], []
    for m in M:
        if m == " ":
            continue
        x, y = m.split()
        X += [float(x)]
        Y += [float(y)]
    return X, Y


def main():
    plt.figure(figsize=(7, 7))

    a, b = -40, -20
    h = 1e-2
    x0 = np.arange(a, b + h, h)

    X1 = [-14, -2, -1.32, 5]
    Y1 = [5, 13, 2, 3]

    X2 = [-25, -23, 9, 10]
    Y2 = [0, 9, -3, 5]

    y01 = spline(X1, Y1, x0)
    y02 = spline(X2, Y2, x0)
    y03 = []
    for i in range(len(y02)):
        y03.append(y01[i]-y02[i])

    plt.plot(x0, y01, label="Spline 1", color='green')
    plt.plot(x0, y02, label="Spline 2", color='blue')

    # plt.plot(x0, y03, label="Spline 1 - Spline 2", color='blue')

    root_i = 0
    is_root = False
    for i in range(len(y03)-1):
        if y03[i] * y03[i+1] < 0:
            root_i = i
            is_root = True

    if is_root:
        eps = 1e-5
        x = intersection(x0, y03, x0, root_i, eps)
        print('Intersection point: (', x, '; ', y02[root_i], ')', sep='')
        plt.plot(x, y02[root_i], 'ro', label='Intersection')
    else:
        extrem_i = 0
        is_extrem = False
        y01_d = der_spline(X1, Y1, x0)
        y01_d_d = der_der_spline(X1, X2, x0)
        for i in range(len(y01_d) - 1):
            if y01_d[i] * y01_d[i + 1] < 0 and y01_d_d[i] > 0:
                extrem_i = i
                is_extrem = True
        if is_extrem:
            eps = 1e-5
            point_x_1 = distance(x0, y01_d, x0, extrem_i, eps)
            point_x_2 = distance(x0, der_spline(X2, Y2, x0), x0, extrem_i, eps)
            dist = abs(y01[extrem_i] - y02[extrem_i])
            print("Min distance =", dist)
            plt.plot(point_x_1, y01[extrem_i], 'ro')
            plt.plot(point_x_2, y02[extrem_i], 'ro')
            plt.vlines(point_x_1, y01[extrem_i], y02[extrem_i], label="Min distance", color='red')
        else:
            print("Error, change borders or input!")

    plt.title("Cubic Spline Interpolation")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
    print("Program successfully finished")
