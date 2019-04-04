import numpy as np

np.set_printoptions(suppress=True)


def gauss(a):
    n = len(a)
    # single division scheme
    for j in range(n):
        # leading element
        leading = a[j][j]
        # check assumption
        assert leading != 0, "Leading element must be different than zero!"
        # divide by coefficient
        a[j] /= leading
        # multiplicate by coeffcient and substract
        for i in range(j + 1, n):
            a[i] -= a[i][j] * a[j]
    return a


def relax(a, acc):
    n = len(a)
    # initial guesses for x = 0
    x = np.zeros(n)
    r = np.zeros(n)
    diff = np.zeros(n)
    temp = np.zeros(n)
    # sum function which sums cij * xj

    def sum(i):
        s = 0
        for z in range(n):
            if z != i:
                s += a[i][z] * x[z]
        return s

    def stopcriterion():
        for i in range(n):
            diff[i] = abs(x[i] - temp[i])
        return all(d <= acc for d in diff)
    # transform matrix in form Axb into b - Ax0 form
    for i in range(n):
        for j in range(n):
            a[i][j] *= -1.0
    # divide each row by leading coefficient
    for i in range(n):
        leading = -a[i][i]
        for j in range(n + 1):
            a[i][j] /= leading
    # do k times
    while True:
        for i in range(n):
            r[i] = a[i][n] - x[i] + sum(i)
            temp[i] = x[i]
            x[i] += r[i]
        if stopcriterion() is True:
            break
    return x


arr = np.array([[5.0, 2.0, 19.0], [2.0, 4.0, 14.0]])
arr2 = np.copy(arr)
accuracy = 0.01

# gauss returns whole Axb matrix
print(gauss(arr))
# relax returns solutions for x
print(relax(arr2, accuracy))
