import math as m
from matplotlib import pyplot as plt


def f(x, y):
    return -0.7 * y + m.e ** (-x)


def euler(h, interval, y0):
    x0, b = interval
    xiTab, yiTab = [], []

    print("\nEuler results: \n")

    for i in range(int(b / h) + 1):
        print(
            "i: {:3} xi: {:8.5f} yi: {:8.5f}".format(
                i, x0, y0
            )
        )

        delta = h * f(x0, y0)

        y0 = y0 + h * delta
        x0 = i * h

        xiTab.append(x0)
        yiTab.append(y0)

    plt.plot(xiTab, yiTab, 'bo-', label='Euler')


def runge_kutta(h, interval, y0):
    x0, b = interval
    xiTab, yiTab = [], []

    print("\nRunge-Kutta results: \n")

    for i in range(int(b / h) + 1):
        print(
            "i: {:3} xi: {:8.5f} yi: {:8.5f}".format(
                i, x0, y0
            )
        )

        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)

        delta = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        y0 = y0 + delta
        x0 = i * h

        xiTab.append(x0)
        yiTab.append(y0)

    plt.plot(xiTab, yiTab, 'ro-', label='Range-Kutta')


h = 1
interval = (0, 20)
y0 = 5
euler(h, interval, y0)
runge_kutta(h, interval, y0)
plt.legend(loc='upper right')
plt.axhline(color='k', linewidth=0.5)
plt.show()

