import numpy as np
import swap_gauss as sw


def matInv(a):
    n = len(a[0])
    aInv = np.identity(n)
    result = aInv.copy()
    for i in range(n):
        a_copy = a.copy()
        result[:, i] = sw.gaussPivot(a_copy, aInv[:, i])
    return result
