def newton(xData, yData):
    y_copy = yData.copy()
    for i in range(1, len(yData)):
        for k in range(i, len(yData)):
            y_copy[k] = (yData[k]-yData[k-1])/(xData[k]-xData[k-1])
        yData = y_copy
    return yData


def func_newton(xData, yData, x):
    coeff_list = newton(xData, yData)
    power = len(coeff_list)
    p = coeff_list[-1]
    for i in range(1, power+1):
        p = coeff_list[power-i]+(x-xData[power-i])*p
    return p
