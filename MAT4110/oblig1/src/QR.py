import numpy as np
from tools import solve_lower_triangular, solve_upper_triangular


def least_squares_QR(A, y):
    # Solves the least squares problem Ax = b, for the x that minimizes ||Ax - b||_2, using QR factorization.
    m = A.shape[1]
    Q, R = np.linalg.qr(A, mode="complete")  # mode=complete to get complete QR, without reduction.
    R1 = R[:m, :m]
    c = Q.T@y
    c1 = c[:m]
    n2 = c1.size
    x = solve_upper_triangular(R1, c1)
    return x