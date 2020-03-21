import numpy as np


class HarmonicOscillator:
    def __init__(self, omega, start, end):
        self.omega = omega
        self.start = start
        self.end = end

    def coupledEquation(self, x, t=0):
        x1 = x[0]
        x2 = x[1]
        fx1 = x2
        fx2 = -(self.omega ** 2) * x1
        return np.array([fx1, fx2], float)

    def methodRK4(self, n, x1=0, x2=0, t=0):
        h = (self.end - self.start) / n
        tpoints = np.arange(self.start, self.end, h)
        xValues = []
        x = np.array([x1, x2], float)

        for t in tpoints:
            xValues.append(x[0])
            k1 = h * self.coupledEquation(x, t)
            k2 = h * self.coupledEquation(x + 0.5 * k1, t)
            k3 = h * self.coupledEquation(x + 0.5 * k2, t)
            k4 = h * self.coupledEquation(x + k3, t)
            x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return tpoints, xValues