import numpy as np

a = [[8, 3, -3], [-2, -8, 5], [3, 5, 10]]


# Find diagonal coefficients

def gauss_seidel():
    diag = np.diag(np.abs(a))
    # Find row sum without diagonal
    off_diag = np.sum(np.abs(a), axis=1) - diag

    if np.all(diag > off_diag):
        print('Matrix is diagonally dominant')
    else:
        print('Matrix is not diagonally dominant')

    x1 = 0
    x2 = 0
    x3 = 0
    epsilon = 10 ** -20
    converged = False
    x_old = np.array([x1, x2, x3])
    print("Iteration results")
    print(" k, x1, x2, x3 ")
    for k in range(1, 500000):
        x1 = (14 - 3 * x2 + 3 * x3) / 8
        x2 = (5 + 2 * x1 - 5 * x3) / (-8)
        x3 = (-8 - 3 * x1 - 5 * x2) / (-5)
        x = np.array([x1, x2, x3])
        # check if it is smaller than threshold
        dx = np.sqrt(np.dot(x - x_old, x - x_old))
        print("%d, %.4f, %.4f, %.4f" % (k, x1, x2, x3))
        if dx < epsilon:
            converged = True
            print("Converged!")
            break
        # assign the latest x value to the old value
        x_old = x
    if not converged:
        print("Not converged, increase the # of iterations")


def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += matrix[0][i] * (-1) ** i * determinant([row[:i] + row[i + 1:] for row in matrix[1:]])
        return det


def inverse(matrix):
    det = determinant(matrix)
    if len(matrix) == 2:
        return [[matrix[1][1] / det, -1 * matrix[0][1] / det],
                [-1 * matrix[1][0] / det, matrix[0][0] / det]]
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = [row[:c] + row[c + 1:] for row in (matrix[:r] + matrix[r + 1:])]
            cofactorRow.append(((-1) ** (r + c)) * determinant(minor))
        cofactors.append(cofactorRow)
    cofactors = cofactors
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / det
    return cofactors


print(determinant(a))

