import numpy as np
from matplotlib import pyplot as plt


def kernel(x):
    return np.exp(-x)


def f(x):
    return 5


def analitical():
    def f(z):
        ##################################
        return 5 + 5 * z

    zAn = [f(z) for z in yArange]

    plt.axhline(color="k", lw=0.5)
    plt.axvline(color="k", lw=0.5)

    plt.plot(yArange, zAn, "ro-", ms=3)


a, b, h = 0, 1, 0.01
iterations = 100
yArange = np.arange(a, b + h, h)

analitical()

x = np.zeros(len(yArange))

for n in range(2, iterations + 1):
    for i in range(len(yArange)):
        temp = 0
        for j in range(i):
            temp += kernel(yArange[i] - yArange[j]) * x[j] * h
        x[i] = temp + f(yArange[i])

plt.plot(yArange, x, "go-", ms=3)

plt.show()
