from Spline_2 import der_spline, der_der_spline, spline


def intersection(xs, ys, x0, good_i, eps):
    x = xs[good_i]
    y = ys[good_i]
    for i in range(0, 100):
        if abs(spline([x, xs[good_i+1]], [y, ys[good_i+1]], [x0[good_i]])[0]) < eps:
            return x
        x = x - eps * spline([x, xs[good_i + 1]], [y, ys[good_i + 1]], [x0[good_i]])[0] / \
            der_spline([x, xs[good_i + 1]], [y, ys[good_i + 1]], [x0[good_i]])[0]
        good_i += 1
    return x


def distance():
    pass
