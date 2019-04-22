import numpy as np


def f(x):  # function
    return 3 * (x ** 2) - 2 * x - 5
    
    
def nodes():  # equally spaced nodes
    h = (b - a) / nc
    for nn in range(nc + 1):
        n.append(a + nn * h)


def xi(i):  # chebyshev function
    return np.cos((2 * i + 1) * np.pi / (2 * nc + 2))


def cheb():  # chebyshev nodes
    for i in range(nc + 1):
        n[nc - i] = ((b - a) * xi(i) / 2) + (a + b) / 2

    print(n)


def errors(o):  # calculate errors with step o
    err = []
    for v in np.arange(a, b, o):
        err.append(abs(f(v) - w(v)))
    return max(err), f(v), v


def w(x):  # interpolation value for x
    aux = np.zeros(nc + 1)
    result = 0.0
    for m in range(nc + 1):
        chunk = 1.0
        for j in range(nc + 1):
            if j != m:
                chunk *= (x - n[j]) / (n[m] - n[j])
        aux[m] = chunk
    for i in range(nc + 1):
        result += f(n[i]) * aux[i]
    return result


n = []
nc = input("Order: ")
a = float(input("Lower bound: "))
b = float(input("Upper bound: "))
e = input("Point: ")
o = 0.01

nodes()
print(n)
if input("Type '1' to use Chebyshev nodes. Anything else if not: ") == 1:
    cheb()

print("Value of interpolated function at " + str(e) + " equals " + str(w(e)))
print("Max error / value of max error / x of max error: ")
print(errors(o))
