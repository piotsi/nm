import numpy as np


def characteristicCoefficients():
    y = np.zeros((len(A) + 1, len(A)))
    y[0][0] = 1.0
    # calculate y matrix
    for i in range(1, len(A) + 1):
        y[i][:] = np.dot(A, y[i - 1][:])
    # solve linear equations from matrix, then flip from p1->pn to pn->p1
    p = np.flipud(np.linalg.solve(np.transpose(y[:][0:len(A)]), -y[len(A)][:]))
    return p


def eigenVal():
    d1 = A[0][0]
    d2 = np.linalg.det([[1.0, 1.0], [1.0, 2.0]])
    d3 = np.linalg.det(A)
    if d1 > 0 and d2 > 0 and d3 > 0:
        print("Matrix is positive definite")
    else:
        print("Matrix is not positive definite")


A = [[1.0, 1.0, 1.0], [1.0, 2.0, 3.0], [1.0, 3.0, 6.0]]
print(characteristicCoefficients())
eigenVal()
