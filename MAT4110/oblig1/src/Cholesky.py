import numpy as np
import matplotlib.pyplot as plt
from tools import solve_lower_triangular, solve_upper_triangular
np.random.seed(42)


def cholesky(A):
    # Performs a Cholesky factorization A = L*L^T of a matrix A.
    n = A.shape[0]
    L = np.array([[0.0] * n for i in range(n)])
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k):
                L[i][k] = np.sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L


def least_squares_cholesky(A, y):
    # Solves the least squares problem Ax = b, for the x that minimizes ||Ax - b||_2, using Cholesky factorization.
    R = cholesky(A.T@A)
    RT = R.T
    w = A.T@y
    z = solve_lower_triangular(R, w)
    x = solve_upper_triangular(RT, z)
    return x