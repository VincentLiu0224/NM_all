import numpy as np
import swap_gauss as gs


def main(f, df, x1, x2):
    result_list = []
    b = x2
    f1 = f(x1)
    f2 = f(x2)
    if int(f1) == 0:
        return x1
    elif int(f2) == 0:
        return x2
    while x1 < b:
        x = 0.5*(x1 + x2)
        result = ne_raph(f, df, x)
        if result >= b:
            break
        else:
            result_list.append(result)
            x1 = result + 1e-1
            x2 = b
    return result_list


def ne_raph(f, df, x):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) <= 1e-9:
            print("Too many iterations\n")
            break
    return x


def differentiation(f, x):
    h = 1.0e-4
    n = len(x)
    jac = np.zeros((n, n))
    f0 = f(x)
    for i in range(n):
        temp = x[i]
        x[i] = temp + h
        f1 = f(x)
        x[i] = temp
        jac[:, i] = (f1 - f0)/h
    return jac, f0


def ne_raph_jacob(f, x):
    dx = np.zeros(3) + 2
    for i in range(30):
        jac, f0 = differentiation(f, x)
        if np.sqrt(np.dot(f0, f0)/len(x)) < 1e-6:
            break
        if np.sqrt(np.dot(dx, dx)) < 1e-6*max(max(abs(x)), 1.0):
            break
        else:
            dx = gs.gaussPivot(jac, -f0)
            x = x + dx
    return x
