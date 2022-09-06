import numpy as np
import math


def jacobi(a, tol=1.0e-8):
    def threshold(a):
        sum = 0.0
        for i in range(n-1):
            for j in range(i+1, n):
                sum = sum + abs(a[i, j])
        return 0.5*sum/(n*(n-1))

    def rotate(a, p, k, j):
        aDiff = a[j, j] - a[k, k]
        if abs(a[k, j]) < abs(aDiff)*1.0e-36:
            t = a[k, j]/aDiff
        else:
            phi = aDiff/(2.0*a[k, j])
            t = 1.0/(abs(phi) + math.sqrt(phi**2 + 1.0))
            if phi < 0.0:
                t = -t
        c = 1.0/math.sqrt(t**2 + 1.0)
        s = t*c
        tau = s/(1.0 + c)
        temp = a[k, j]
        a[k, j] = 0.0
        a[k, k] = a[k, k] - t*temp
        a[j, j] = a[j, j] + t*temp
        for i in range(k):
            temp = a[i, k]
            a[i, k] = temp - s*(a[i, j] + tau*temp)
            a[i, j] = a[i, j] + s*(temp - tau*a[i, j])
        for i in range(k+1, j):
            temp = a[k, i]
            a[k, i] = temp - s*(a[i, j] + tau*a[k, i])
            a[i, j] = a[i, j] + s*(temp - tau*a[i, j])
        for i in range(j+1, n):
            temp = a[k, i]
            a[k, i] = temp - s*(a[j, i] + tau*temp)
            a[j, i] = a[j, i] + s*(temp - tau*a[j, i])
        for i in range(n):
            temp = p[i, k]
            p[i, k] = temp - s*(p[i, j] + tau*p[i, k])
            p[i, j] = p[i, j] + s*(temp - tau*p[i, j])

    n = len(a)
    p = np.identity(n, float)
    for k in range(20):
        mu = threshold(a)
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(a[i, j]) >= mu:
                    rotate(a, p, i, j)
        if mu <= tol:
            return np.diagonal(a), p
