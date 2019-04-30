import math as m


def f(x):
    return (x ** 4) - 625
    # return (x ** 4) + 7 * (x ** 3) - 94 * (x ** 2) - 328 * x + 960


def fprime(x):
    return 4 * (x ** 3)
    # return 4 * (x ** 3) + 21 * (x ** 2) - 188 * x - 328


def fprimeprime(x):
    return 12 * (x ** 2)


def falsi(a, b, acc):
    k = 0
    if fprimeprime(a) * f(a) > 0:
        x = float(b)
        while abs(f(x)) > acc:
            x = x - (f(x) / (f(a) - f(x))) * (a - x)
            k += 1
            print("k = {:2d}, x = {:+.5f}, f(x) = {:+.5f}".format(k, x, f(x)))
    elif fprimeprime(b) * f(b) > 0:
        x = float(a)
        while abs(f(x)) > acc:
            x = x - (f(x) / (f(b) - f(x))) * (b - x)
            k += 1
            print("k = {:2d}, x = {:+.5f}, f(x) = {:+.5f}".format(k, x, f(x)))


def newton(a, b, acc, ig):
    k = 0
    x = float(ig)
    while abs(f(x)) > acc:
        x = x - (f(x) / fprime(x))
        k += 1
        print("k = {:2d}, x = {:+.5f}, f(x) = {:+.5f}".format(k, x, f(x)))
    return


acc = 0.001
a, b = 1, 10
print("Formula falsi:")
falsi(a, b, acc)
print("Newton:")
newton(a, b, acc, 10)
print("Bernoulli:")
bernoulli(5, [1, 5, 0, 0, 0, -5], acc)
