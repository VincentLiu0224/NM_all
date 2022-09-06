import numpy as np
import swap_engine as sw


def LUmain(a, b):
    a_and_seq = LUdecomp(a)
    ans = LUsolve(a_and_seq[0], b, a_and_seq[1])
    return ans


def LUdecomp(a):
    n = len(a)
    seq = np.array(range(n))
    s = np.zeros((n))
    for i in range(n):
        s[i] = max(abs(a[i, :]))
    for k in range(0, n-1):
        p = np.argmax(np.abs(a[k:n, k])/s[k:n]) + k
        if p != k:
            sw.swapRows(s, k, p)
            sw.swapRows(a, k, p)
            sw.swapRows(seq, k, p)
    for k in range(0, n):
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k]/a[k, k]
                a[i, k:n] = a[i, k:n] - lam*a[k, k:n]
                a[i, k] = lam
    return a, seq


def LUsolve(a, b, seq):
    n = len(a)
    x = b.copy()
    for i in range(n):
        x[i] = b[seq[i]]
    for k in range(1, n):
        x[k] = x[k] - np.dot(a[k, 0:k], x[0:k])
    x[n-1] = x[n-1]/a[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (x[k] - np.dot(a[k, k+1:n], x[k+1:n]))/a[k, k]
    return x
