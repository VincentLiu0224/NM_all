import numpy as np
import LU_decomposite as lu
import math
from random import random


def inversePower(a, s, tol=1.0e-6):
    n = len(a)
    aStar = a - np.identity(n)*s
    aStar = lu.LUdecomp(aStar)
    x = np.zeros(n)
    for i in range(n):
        x[i] = random()
    xMag = math.sqrt(np.dot(x, x))
    x = x/xMag
    for i in range(50):
        xOld = x.copy()
        x = lu.LUsolve(aStar[0], x, aStar[1])
        xMag = math.sqrt(np.dot(x, x))
        x = x/xMag
        if np.dot(xOld, x) < 0.0:
            sign = -1.0
            x = -x
        else:
            sign = 1.0
    if math.sqrt(np.dot(xOld - x, xOld - x)) < tol:
        return s + sign/xMag, x
