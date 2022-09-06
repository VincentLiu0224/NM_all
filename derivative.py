import numpy as np
import LUdecomp_for_trig as lt


def curvatures(xData, yData):
    n = len(xData) - 1
    c = np.zeros(n)
    d = np.ones(n+1)
    e = np.zeros(n)
    k = np.zeros(n+1)
    c[0:n-1] = xData[0:n-1] - xData[1:n]
    d[1:n] = 2.0*(xData[0:n-1] - xData[2:n+1])
    e[1:n] = xData[1:n] - xData[2:n+1]
    k[1:n] = 6.0*(yData[0:n-1] - yData[1:n]) / (xData[0:n-1] - xData[1:n]) \
        - 6.0*(yData[1:n] - yData[2:n+1]) / (xData[1:n] - xData[2:n+1])
    lt.LUdecomp3(c, d, e)
    lt.LUsolve3(c, d, e, k)
    return k
