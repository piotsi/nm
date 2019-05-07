import math as m


def f(x):
    return m.sin(5 * x)


def quadratic(n):
    def fi(x, i):
        return m.sqrt(2 / m.pi) * m.sin(i * x)

    def chebyshev_b(i):
        a, b = interval
        return (b - a / 2) * (
            fi((b + a) / 2 + (b - a) / 2 * (-0.577350), i) ** 2 +
            fi((b + a) / 2 + (b - a) / 2 * 0.577350, i) ** 2
        )

    def chebyshev_a(i):
        a, b = interval
        return (b - a / 2) * (
            f((b + a) / 2 + (b - a) / 2 * (-0.577350)) *
            fi((b + a) / 2 + (b - a) / 2 * (-0.577350), i) +
            f((b + a) / 2 + (b - a) / 2 * 0.577350) *
            fi((b + a) / 2 + (b - a) / 2 * 0.577350, i)
        )
    b_coeff = []
    a_coeff = []
    for i in range(1, n + 1):
        b_coeff.append(chebyshev_b(i))
    for i in range(1, n + 1):
        a_coeff.append(1 * chebyshev_a(i) / b_coeff[i - 1])
    for i, (b, a) in enumerate(zip(b_coeff, a_coeff), start=1):
        print("b{:2}: {:+.5f}, a{:2}: {:+.5f}".format(i, b, i, a))


interval = (0, m.pi)
n = 10
quadratic(n)
