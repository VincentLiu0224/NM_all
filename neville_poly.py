def neville(xData, yData, x):
    m = len(xData)
    y = yData.copy()
    for k in range(1, m):
        y[0:m-k] = ((x - xData[k:m])*y[0:m-k] +
                    (xData[0:m-k] - x)*y[1:m-k+1]) / \
                    (xData[0:m-k] - xData[k:m])
    return y[0]
