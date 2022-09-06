def trap_main(f, a, b):
    inti = 0.0
    for i in range(1, 20):
        if i == 1:
            inti = (f(a) - f(b))*(a - b)/2.0
        else:
            inti = trapezoid(f, a, b, inti, i)
    return inti


def trapezoid(f, a, b, inti, i):
    n = 2**(i - 2)
    h = (b - a)/n
    x = a + h/2.0
    sum = 0.0
    for i in range(n):
        sum = sum + f(x)
        x = x + h
    inti = (inti + h*sum)/2.0
    return inti
