import math as m


def big_F(x):
    return (((x ** 4) / 2) + m.sin(x))
    # return (((x ** 4) / 8) + ((x ** 3) / 2))


def small_F(x):
    return (2 * (x ** 3) + m.cos(x))
    # return (((x ** 3) + (3 * (x ** 2))) / 2)


def Analitical(a, b):
    return big_F(b) - big_F(a)


"""
Simple approximation of area under the curve -
constant line y = midPoint is (n = 0)
"""


def areaUnderCurve(a, b, h):
    midPoint = (a + b) / 2
    value = h * small_F(midPoint)
    error = Analitical(a, b) - value
    print('Value: ' + str(value))
    print('Error: ' + str(error))


# Simple Trapezoid Method (n = 1)
def simpleTrapezoid(a, b, h):
    value = ((h / 2) * (small_F(a) + small_F(b)))

    # to change ->
    zeta = -0.721

    secondDerivative = ((12 * zeta) - (m.cos(zeta)))

    error = (((h ** 3) * secondDerivative) / -12)
    print('Value: ' + str(value))
    print('Error: ' + str(error))


# Simple Simpson Formula (n = 2)
def simpleSimpson(a, b, h):
    h = h / 2
    x1 = (a + b) / 2.0
    value = ((h * (1.0 / 3.0)) * (small_F(a) + 4 * (small_F(x1)) + small_F(b)))

    # to change ->
    zeta = 0.5
    fourthDerivative = m.cos(zeta)

    error = ((-1 / 90) * (h ** 5) * fourthDerivative)
    print('Value: ' + str(value))
    print('Error: ' + str(error))


# Simple Cheb. Method (n = 2)
def simpleCheb_n2(a, b, h):
    t = 0.577350
    x1 = (b + a) / 2 + (b - a) / 2 * (-t)
    x2 = (b + a) / 2 + (b - a) / 2 * t
    value = ((h / 2) * (small_F(x1) + small_F(x2)))
    error = Analitical(a, b) - value
    print('Value: ' + str(value))
    print('Error: ' + str(error))


# Simple Cheb. Method (n = 4)
def simpleCheb_n4(a, b, h):
    t1 = 0.794654
    t2 = 0.187592
    x1 = ((b + a) / 2) + ((b - a) / 2) * (-t1)
    x4 = ((b + a) / 2) + ((b - a) / 2) * t1
    x2 = ((b + a) / 2) + ((b - a) / 2) * (-t2)
    x3 = ((b + a) / 2) + ((b - a) / 2) * t2

    value = (h / 4) * (small_F(x1) + small_F(x2) + small_F(x3) + small_F(x4))
    error = Analitical(a, b) - value
    print('Value: ' + str(value))
    print('Error: ' + str(error))


a = -1.0
b = 0.5
h = (b - a)

print('\nSimple Area under curve: ')
areaUnderCurve(a, b, h)
print('\nSimple Trapezoid: ')
simpleTrapezoid(a, b, h)
print('\nSimple Simpson: ')
simpleSimpson(a, b, h)
print('\nSimple Cheb. n = 2: ')
simpleCheb_n2(a, b, h)
print('\nSimple Cheb. n = 4: ')
simpleCheb_n4(a, b, h)
