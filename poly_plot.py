import numpy as np
import matplotlib.pyplot as plt


def plotPoly(xData, yData, coeff, xlab='x', ylab='y'):
    m = len(coeff)
    x1 = min(xData)
    x2 = max(xData)
    dx = (x2 - x1)/20.0
    x = np.arange(x1, x2+dx/10.0, dx)
    y = np.zeros((len(x)))*1.0
    for i in range(m):
        y = y + coeff[i]*x**i
    plt.plot(xData, yData, 'o', x, y, '-')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.grid()
    plt.show()
