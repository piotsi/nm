import numpy as np


def characteristicCoefficients():
    y = np.zeros((len(A) + 1, len(A)))
    y[0][0] = 1.0
    # calculate y matrix
    for i in range(1, len(A) + 1):
        y[i][:] = np.dot(A, y[i - 1][:])
    # solve linear equations from matrix, then flip from p1->pn to pn->p1
    p = np.flipud(np.linalg.solve(np.transpose(y[:][0:len(A)]), -y[len(A)][:]))
    return "Characteristic polynomial coefficients are equal: " + str(p)


def matrixProperties():  # Funcion checking if matrix is positive definite
    d1 = A[0][0]
    d2 = np.linalg.det([[1.0, 1.0], [1.0, 2.0]])
    d3 = np.linalg.det(A)
    if d1 > 0 and d2 > 0 and d3 > 0:
        print("Matrix is positive definite")
    else:
        print("Matrix is not positive definite")


def iterativeMethod(A):  # Function calculating value of the first eigenvalue
                        # of matrix A

    coeffX1 = []
    coeffX2 = []
    coeffEigen1 = []

    k = 8  # number of iterations
    x3 = 1  # value taken from theorem
    x1 = 1  # arbitrary set value
    x2 = 1  # arbitrary set value

    coeffX1.append(x1)
    coeffX2.append(x2)

    eigen1 = (1.0 / x3) * (A[2][0] * x1 + A[2][1] * x2 + A[2][2] * x3)
    x1 = (1.0 / eigen1) * (A[0][0] * x1 + A[0][1] * x2 + A[0][2] * x3)
    x2 = (1.0 / eigen1) * (A[1][0] * x1 + A[1][1] * x2 + A[1][2] * x3)

    coeffEigen1.append(eigen1)

    for i in range(k):
        j = 0
        x1 = (1 / coeffEigen1[i]) * (
            (A[0][j] * coeffX1[i]) + (A[0][j + 1] * coeffX2[i]) + A[0][j + 2]
        )
        x2 = (1 / coeffEigen1[i]) * (
            (A[1][j] * coeffX1[i]) + (A[1][j + 1] * coeffX2[i]) + A[1][j + 2]
        )

        coeffX1.append(x1)
        coeffX2.append(x2)

        eigen1 = (A[2][j] * coeffX1[i + 1]) + (A[2][j + 1] * coeffX2[i + 1]) + A[2][2]
        coeffEigen1.append(eigen1)
    print("First eigenvalue is equal: " + str(coeffEigen1[8]))
    print("First eigenvector is equal: [" + str(coeffX1[8]) + ", " + str(coeffX2[8]) + ", " + str(x3) + "]")


A = [[1.0, 1.0, 1.0], [1.0, 2.0, 3.0], [1.0, 3.0, 6.0]]  # Input matrix

print(characteristicCoefficients())
matrixProperties()
iterativeMethod(A)
