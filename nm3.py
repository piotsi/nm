def f(x):
    return 3 * (x ** 2) + 4 * x - 4


def nodes():
    h = (b - a) / nc
    for nn in range(nc):
        n.append(a + nn * h)
    print(n)


def cheb():
    h = (1.0 - (-1.0)) / nc
    for nn in range(nc):
        n.append(((b - a) * (-1 + h * nn) / 2) + a + b)
    print(n)


def errors():
    err = []
    for nn in range(nc):
        err.append(f(n[nn]) - w(n[nn]))
    print(err)


def aux(i, x):
    w = 1
    for j in range(nc):
        if j != i:
            w *= (x - n[j]) / (n[i] - n[j])
    return w


def w(x):
    result = 0
    for m in range(nc):
        result += aux(m, e) * f(n[m])
    return result


n = []
nc = input("How many nodes: ")
a = float(input("Lower bound: "))
b = float(input("Upper bound: "))
e = input("Point: ")
if input("Type '1' to use Chebyshev nodes. Anything else if not: ") == 1:
    cheb()
else:
    nodes()

print("Value of interpolated function at " + str(e) + " equals " + str(w(e)))
errors()
print(f(e) - w(e))
