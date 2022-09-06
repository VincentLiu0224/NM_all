import numpy as np
import swap_gauss as ga
from newton_poly import evalPoly


def polyFit(xData, yData, m):
    a = np.zeros((m+1, m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i, j] = s[i+j]
    return ga.gaussPivot(a, b)


def stdDev(c, xData, yData):
    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c, xData[i])
        sigma = sigma + (yData[i] - p)**2
    sigma = np.sqrt(sigma/(n - m))
    return sigma
