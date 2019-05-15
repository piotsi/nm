import math as m


def function1(x, y):
    return -0.7 * y + m.e ** -x


def function2(x, y):
    return 7.0 * y + 14


def euler(h, interval):

    a, b = interval
    x0 = a
    y0 = 5

    print("\nEuler results: \n")

    print(
        "i: {}      xi: {:.5f} yi: {:.5f}".format(
            0, x0, y0
        )
    )
    for i in range(1, int(b / h) + 1):
        delta = h * function1(x0, y0)
        y = y0 + h * delta
        x = i * h
        y0 = y
        x0 = x
        print(
            "i: {}      xi: {:.5f} yi: {:.5f}".format(
                i, x0, y0
            )
        )


def runge_kutta(h, interval):
    a, b = interval
    x0 = a
    y0 = 5

    print("\nRunge-Kutta results: \n")

    print(
        "i: {}      xi: {:.5f} yi: {:.5f}".format(
            0, x0, y0
        )
    )

    for i in range(1, int(b / h) + 1):

        k1 = h * function1(x0, y0)
        k2 = h * function1(x0 + h / 2, y0 + k1 / 2)
        k3 = h * function1(x0 + h / 2, y0 + k2 / 2)
        k4 = h * function1(x0 + h, y0 + k3)

        delta = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y = y0 + delta
        x = i * h
        y0 = y
        x0 = x
        print(
            "i: {}      xi: {:.5f} yi: {:.5f}".format(
                i, x0, y0
            )
        )


h = 1
interval = (0, 20)
euler(h, interval)
runge_kutta(h, interval)
