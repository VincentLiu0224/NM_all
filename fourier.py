import numpy as np
import matplotlib.pyplot as plt


def main():
    x1 = np.array([10000])
    for i in x1:
        i = int(i)
        for t in [0.2, 5, 10]:
            func = function(i, t)
            plot(func[0], func[1], func[2])
    return


def function(n, t):
    x = np.linspace(0, 50, 1000)
    a0 = 2*t*1/10
    for a in range(1, n+1):
        a0 += (2*t/(x*np.pi))*np.sin(np.pi*x*t/10)*np.cos(2*np.pi*x*0/10)
    return x, a0, n


def plot(x, y, n):
    plt.plot(x, y, label=n)
    plt.grid()
    plt.show()
    return


main()
