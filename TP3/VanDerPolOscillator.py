import numpy as np
from scipy.integrate import RK45


class VanDerPolOscillator:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def coupledEquation(self, x, t=0):
        x1 = x[0]
        x2 = x[1]
        fx1 = x2
        fx2 = -x1 - (self.epsilon * ((x1 ** 2) - 1) * x2)
        return np.array([fx1, fx2], float)

    def methodRK45(self, n, x1=0, x2=0, t=0):

