import math as m
from matplotlib import pyplot as plt


def function1(x, y):
    return -0.7 * y + m.e ** -x


def euler(h, interval):

    a, b = interval
    x0 = a
    y0 = 5
    xiTab = [0]
    yiTab = [5]

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
        yiTab.append(y)
        y0 = y
        x0 = x
        xiTab.append(x0)
        print(
            "i: {}      xi: {:.5f} yi: {:.5f}".format(
                i, x0, y0
            )
        )
    plt.plot(xiTab, yiTab)
    plt.show()


def runge_kutta(h, interval):
    a, b = interval
    x0 = a
    y0 = 5
    xiTab = [0]
    yiTab = [5]

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
        yiTab.append(y)

        x = i * h
        y0 = y
        x0 = x
        xiTab.append(x0)
        print(
            "i: {}      xi: {:.5f} yi: {:.5f}".format(
                i, x0, y0
            )
        )
    plt.plot(xiTab, yiTab)
    plt.show()


h = 1
interval = (0, 20)
euler(h, interval)
runge_kutta(h, interval)
