# need to define c, d and e matrix
def LU3main(a, b):
    tupl = block_collector(a)
    process = LUdecomp3(tupl(0), tupl(1), tupl(2))
    result = LUsolve3(process(0), process(1), process(2), b)
    return result


def block_collector(a):
    c = []
    d = []
    e = []
    n = len(a)
    for k in range(0, n-1):
        for i in range(1, n):
            d.append(a[k, i-1])
            e.append(a[k, i])
            c.append(a[k+1, i-1])
    return c, d, e


def LUdecomp3(c, d, e):
    n = len(d)
    for k in range(1, n):
        lam = c[k-1]/d[k-1]
        d[k] = d[k] - lam*e[k-1]
        c[k-1] = lam
    return c, d, e


def LUsolve3(c, d, e, b):
    n = len(d)
    for k in range(1, n):
        b[k] = b[k] - c[k-1]*b[k-1]
        b[n-1] = b[n-1]/d[n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - e[k]*b[k+1])/d[k]
    return b
