import numpy as np
import choleski_decomp as che


def stdForm(a, b):
    def invert(L):
        n = len(L)
        for j in range(n-1):
            L[j, j] = 1.0/L[j, j]
        for i in range(j+1, n):
            L[i, j] = -np.dot(L[i, j:i], L[j:i, j])/L[i, i]
            L[n-1, n-1] = 1.0/L[n-1, n-1]

    # n = len(a)
    L = che.choleski(b)
    invert(L)
    h = np.dot(b, np.inner(a, L))
    return h, np.transpose(L)
