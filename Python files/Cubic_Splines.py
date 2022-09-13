import numpy as np


def h(i: int, xs: list[float]) -> float:
    if i == 0:
        i += 1
    return xs[i] - xs[i - 1]


def all_args(i: int, xs: list[float], ys: list[float]) -> tuple[float, float, float, float]:
    F = (ys[i + 1] - ys[i]) / h(i + 1, xs) - (ys[i] - ys[i - 1]) / h(i, xs)
    A = h(i, xs) / 6
    B = (h(i, xs) + h(i + 1, xs)) / 3
    C = h(i + 1, xs) / 6
    return A, B, C, F


def alpha(i: int, xs: list[float], ys: list[float]) -> float:
    A, B, C, F = all_args(i - 1, xs, ys)
    if i == 1:
        return -C / B
    return -C / (A * alpha(i - 1, xs, ys) + B)


def beta(i: int, xs: list[float], ys: list[float]) -> float:
    A, B, C, F = all_args(i - 1, xs, ys)
    if i == 1:
        return F / B
    return (F - A * beta(i - 1, xs, ys)) / (A * alpha(i - 1, xs, ys) + B)


def gamma(i: int, xs: list[float], ys: list[float]) -> float:
    if i == 0 or i == len(xs) - 1:
        return 0
    if i == len(xs) - 2:
        A, B, C, F = all_args(i, xs, ys)
        return (F - A * beta(i, xs, ys)) / (B + A * alpha(i, xs, ys))
    return alpha(i + 1, xs, ys) * gamma(i + 1, xs, ys) + beta(i + 1, xs, ys)


def spline(xs: list[float], ys: list[float], x: np.ndarray) -> list[float]:
    i = 0
    vals = []
    for xi in x:
        while (i < len(xs) - 2) and not(xs[i] <= xi <= xs[i+1]) and (xi >= xs[i]):
            i += 1
        prt1 = (xs[i + 1] - xi) / h(i + 1, xs)
        prt2 = (xi - xs[i]) / h(i + 1, xs)
        prt3 = ((xs[i + 1] - xi) ** 3 - h(i + 1, xs) ** 2 * (xs[i + 1] - xi)) / (6 * h(i + 1, xs))
        prt4 = ((xi - xs[i]) ** 3 - h(i + 1, xs) ** 2 * (xi - xs[i])) / (6 * h(i + 1, xs))
        val = ys[i] * prt1 + ys[i + 1] * prt2 + gamma(i, xs, ys) * prt3 + gamma(i + 1, xs, ys) * prt4
        vals += [val]
    return vals


def der_spline(xs: list[float], ys: list[float], x: np.ndarray) -> list[float]:
    i = 0
    vals = []
    for xi in x:
        while (i < len(xs) - 2) and not(xs[i] <= xi <= xs[i+1]) and (xi >= xs[i]):
            i += 1
        prt1 = (-1) * ys[i] / h(i+1, xs)
        prt2 = ys[i+1]/h(i+1, xs)
        prt3 = (gamma(i, xs, ys) * (-1) * (xs[i+1] - xi)**2)/(2 * h(i+1, xs)) + (gamma(i, xs, ys) * h(i+1, xs))/6
        prt4 = (gamma(i+1, xs, ys) * (xi - xs[i])**2)/(2*h(i+1, xs)) - (gamma(i+1, xs, ys) * h(i+1, xs))/6
        val = prt1 + prt2 + prt3 + prt4
        vals += [val]
    return vals


def der_der_spline(xs: list[float], ys: list[float], x: list[float]) -> list[float]:
    i = 0
    vals = []
    for xi in x:
        while (i < len(xs) - 2) and not (xs[i] <= xi <= xs[i + 1]) and (xi >= xs[i]):
            i += 1
        prt1 = (gamma(i, xs, ys) * (xs[i+1] - xi)) / h(i+1, xs)
        prt2 = (gamma(i+1, xs, ys) * (xi - xs[i])) / h(i+1, xs)
        val = prt1 + prt2
        vals += [val]
    return vals
