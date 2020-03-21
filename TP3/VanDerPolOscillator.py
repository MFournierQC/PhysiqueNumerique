import numpy as np
from scipy.integrate import solve_ivp


class VanDerPolOscillator:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def coupledEquation(self, t, x):
        x1 = x[0]
        x2 = x[1]
        fx1 = x2
        fx2 = -x1 - (self.epsilon * ((x1 ** 2) - 1) * x2)
        return np.array([fx1, fx2], float)

    def methodRK45(self, initialState, t0=0):
        tSpan = [t0, (8 * np.pi)]
        points = solve_ivp(self.coupledEquation, tSpan, initialState, method='RK45', first_step=0.01, max_step=0.01)
        tPoints = points['t']
        fx1Points = points['y'][0]
        fx2Points = points['y'][1]
        return tPoints, fx1Points, fx2Points
