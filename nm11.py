import numpy as np
np.set_printoptions(formatter={'float_kind': '{:6.2f}'.format})

def netMethod(h, r):
    d = 10
    matrix = np.zeros((d + 2, d))
    

    aValue = 0.1
    x = (aValue * h) / (r ** 2)

    for i in range(1, d + 1):
        matrix[i][0] = np.sin(r*i*3.14)

    for i in range(1, d):
        for k in range(1, d + 1):
            matrix[k][i] = matrix[k][i - 1] + (x*((matrix[k + 1][i - 1]) -
            2 * (matrix[k][i - 1]) + matrix[k - 1][i - 1]))
    print(matrix)

netMethod(0.01, 0.1)
