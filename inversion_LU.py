import numpy as np
import swap_LU as sw


def matInv(a):
    n = len(a[0])
    aInv = np.identity(n)
    a, seq = sw.LUdecomp(a)
    for i in range(n):
        aInv[:, i] = sw.LUsolve(a, aInv[:, i], seq)
    return aInv
