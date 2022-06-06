from operations import do_operations


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
    a, b = -10, 10 # intersection
    # a, b = 2, 10  # min distance using extremum
    # a, b = -10, 0  # min distance using boarder case

    # Data:
    h = 1e-3

    X1 = [-14, -2, -1.32, 5]
    Y1 = [5, 13, 2, 3]

    X2 = [-25, -23, 9, 10]
    Y2 = [0, 9, -3, 5]

    do_operations(X1, Y1, X2, Y2, h, a, b)


if __name__ == "__main__":
    main()
