import numpy as np


# r-k 4th order integration, if F is only related to one variable then its is equivalent to simpson's rule
# x is equivalent to any independant variable(t), y is the state vector which is dependant to t: y(t)
# given the same step size, it might not be more accurate than other method
# but the error will reduce in the order of 4 when decreasing same amount of step size (p=4)
def op(F, u, t, tStop, dt):
    def run_kut4(F, u, t, dt):
        K0 = dt*F(u, t)
        K1 = dt*F(u + K0/2.0, t + dt/2.0)
        K2 = dt*F(u + K1/2.0, t + dt/2.0)
        K3 = dt*F(u + K2, t + dt)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(t)
    Y.append(u)
    while t < tStop:
        dt = min(dt, tStop - t)
        u = u + run_kut4(F, u, t, dt)
        t = t + dt
        X.append(t)
        Y.append(u)
    return np.array(X), np.array(Y)
