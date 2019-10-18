import numpy as np

def solve_upper_triangular(A, y):
    ## Solves the matrix equation Ax = y for an upper triangular A using backward substitution.
    N = A.shape[0]
    x = np.zeros(N)
    x[N-1] = y[N-1]/A[N-1,N-1]
    for i in range(N-1, -1, -1):
        tmp = y[i]
        for j in range(N-1, i, -1):
            tmp -= x[j]*A[i,j]
        x[i] = tmp/A[i,i]
    return x

def solve_lower_triangular(A, y):
    ## Solves the matrix equation Ax = y for a lower triangular A using forward substitution.
    N = A.shape[0]
    x = np.zeros(N)
    x[0] = y[0]/A[0,0]
    for i in range(1, N, 1):
        tmp = y[i]
        for j in range(0, i, 1):
            tmp -= x[j]*A[i,j]
        x[i] = tmp/A[i,i]
    return x
