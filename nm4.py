k, n, x0, h = 1, 4, 3, 0
x = []
fx = []
dfx = []
d2fx = []
d3fx = []
d4fx = []
fd1Analytic = 12
fd2Analytic = 4

h = input("h: ")


def f(x):
    return 2 * x ** 2 + 4


for i in range(n + 1):
    x.append(x0 + i * h)
    fx.append(f(x[i]))

for i in range(n):
    dfx.append(fx[i + 1] - fx[i])

for i in range(n - 1):
    d2fx.append(dfx[i + 1] - dfx[i])

for i in range(n - 2):
    d3fx.append(d2fx[i + 1] - d2fx[i])

for i in range(n - 3):
    d4fx.append(d3fx[i + 1] - d3fx[i])


fd = (1.0 / h) * (dfx[0] - d2fx[0] / 2.0 + d3fx[0] / 3.0 - d4fx[0] / 4.0)
f2d = (1.0 / (h * h)) * (d2fx[0] - d3fx[0] + 11.0 * d4fx[0] / 12.0)
overallError = [fd1Analytic - fd, fd2Analytic - f2d]

print(x)
print(fx)
print(dfx)
print(d2fx)
print(d3fx)
print(d4fx)
print("")
print(fd)
print(f2d)
print("")
print(overallError)
