import numpy as np
import matplotlib.pyplot as plt
from Intersections import intersection, distance
from Cubic_Splines import spline, der_spline
from shapely.geometry import LineString


def der_local(y0, h):
    vals = []
    for i in range(0, len(y0)-2):
        val = (y0[i+1] - y0[i])/h
        vals += [val]
    return vals


def do_operations(X1, Y1, X2, Y2, h, a, b):
    plt.figure(figsize=(7, 7))

    x0 = np.arange(a, b + h, h)

    y01 = spline(X1, Y1, x0)
    y02 = spline(X2, Y2, x0)
    y03 = []
    for i in range(len(y02)):
        y03.append(y01[i] - y02[i])

    plt.plot(x0, y01, label="Spline 1", color='green')
    plt.plot(x0, y02, label="Spline 2", color='blue')

    # plt.plot(x0, y03, label="Spline 1 - Spline 2", color='orange')

    first = LineString(np.column_stack((x0, y01)))
    second = LineString(np.column_stack((x0, y02)))

    intersect = first.intersection(second)
    print(*intersect.xy)

    root_i = 0
    is_root = False
    for i in range(len(y03) - 1):
        if y03[i] * y03[i + 1] < 0:
            root_i = i
            is_root = True

    if is_root:
        eps = 1e-5
        x = intersection(x0, y03, x0, root_i, eps)
        print('Intersection point: ({0}, {1})'.format(x, y01[root_i]))
        plt.plot(x, y02[root_i], 'ro', label='Intersection')

    else:
        extrem_i = 0
        is_extrem = False

        y03_d = der_local(y03, h)
        y03_d_d = der_local(y03_d, h)

        for i in range(len(y03_d) - 1):
            if y03_d[i] * y03_d[i + 1] < 0 and y03_d_d[i] > 0:
                extrem_i = i
                is_extrem = True

        distances = []
        distances += [abs(y01[0] - y02[0])]
        distances += [abs(y01[len(y01) - 1] - y02[len(y02) - 1])]

        if is_extrem:
            eps = 1e-5

            point_x_1 = distance(x0, der_spline(X1, Y1, x0), x0, extrem_i, eps)
            point_x_2 = distance(x0, der_spline(X2, Y2, x0), x0, extrem_i, eps)
            distances += [abs(y01[extrem_i] - y02[extrem_i])]

            plt.vlines(point_x_1, y01[extrem_i], y02[extrem_i], label="Min distance", color='red')
            plt.plot(point_x_1, y01[extrem_i], 'go', label='P1')
            plt.plot(point_x_2, y02[extrem_i], 'bo', label='P2')

            print("Min distance =", min(distances))
            print("Points of distance:\n"
                  "P1: ({0}, {1})\n"
                  "P2: ({0}, {2})".format
                  (point_x_1, y01[extrem_i], y02[extrem_i]))
        else:
            if min(distances) == distances[0]:
                plot_i = 0
                plot_x = x0[plot_i]
            else:
                plot_i = len(x0) - 1
                plot_x = x0[plot_i]

            plt.vlines(plot_x, y01[plot_i], y02[plot_i], label="Min distance", color='red')
            plt.plot(plot_x, y01[plot_i], 'go', label="P1")
            plt.plot(plot_x, y02[plot_i], 'bo', label="P2")

            print("Min distance =", min(distances))
            print("Points of distance:\n"
                  "P1: ({0}, {1})\n "
                  "P2: ({0}, {2})".format
                  (plot_x, y01[plot_i], y02[plot_i]))

    plt.title("Cubic Spline Interpolation")
    plt.grid()
    plt.legend()
    plt.show()

