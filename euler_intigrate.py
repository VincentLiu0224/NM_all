import derivative as de
import numpy as np


def euler_old(f, a, b, steps):
    h = (b-a)/steps
    y_list = np.zeros(steps)
    x_list = np.zeros(steps)
    for i in range(steps):
        x_list[i] = a
        y_list[i] = f(a)
        a = a + h
    y_derivative = de.curvatures(x_list, y_list)
    y_integrate = y_list + h*y_derivative
    return x_list, y_integrate


def euler_new(f_deri, y_init, a, b, steps):
    h = (b-a)/steps
    y_list = np.zeros(steps)
    x_list = np.zeros(steps)
    y_list[0] = y_init
    x_list[0] = a
    for i in range(1, steps):
        derivative = f_deri(a, y_init)
        y_init = y_init + h*derivative
        a = a + h
        x_list[i] = a
        y_list[i] = y_init
    return x_list, y_list
