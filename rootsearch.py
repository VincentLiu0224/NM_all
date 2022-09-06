import numpy as np


def main(f, a, b):
    for i in range(5):
        dx = (b - a)/10
        a, b = rootsearch(f, a, b, dx)
    return (a + b)/2


def rootsearch(f, a, b, dx):
    c = a + dx
    f1 = f(a)
    f2 = f(c)
    while np.sign(f1) == np.sign(f2):
        if a >= b:
            return "None", "no root found"
        else:
            a = a + dx
            c = a + dx
            f1 = f(a)
            f2 = f(c)
    return a, c
