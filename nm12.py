import math as m
from matplotlib import pyplot as plt


def f(z):
    return -0.5 * m.e ** (-2 * z) - 0.5


def create_interval(a, b, h):
    zTab, yTab = [], []
    for i in range(h + 1):
        zTab.append((b - a) * i / h)
    yTab = [f(z) for z in zTab]
    return zTab, yTab

zTab, yTab = create_interval(a=0, b=3, h=100)


print(zTab)
print(yTab)

plt.axhline(color='k', lw=0.5)
plt.axvline(color='k', lw=0.5)

plt.plot(zTab, yTab, 'ro-', ms=3)
plt.show()
