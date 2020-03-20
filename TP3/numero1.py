from TP3.HarmonicOscillator import HarmonicOscillator
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    oscillator = HarmonicOscillator(1, 0, 50)
    tpoints, xValues = oscillator.methodRK4(1000)

    plt.subplot(2, 1, 1)
    plt.plot(tpoints, xValues)
    plt.ylabel('ODE')

    plt.subplot(2, 1, 2)
    plt.plot(tpoints, np.cos(tpoints))
    plt.ylabel('Analytical Solution')
    plt.xlabel('t')
    plt.show()