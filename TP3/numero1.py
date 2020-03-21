from TP3.HarmonicOscillator import HarmonicOscillator
from TP3.AnharmonicOscillator import AnharmonicOscillator
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    oscillator = HarmonicOscillator(1, 0, 50)

    # Sous question a :
    tpoints, xValues = oscillator.methodRK4(1000, 1.0, 0.0)
    plt.subplot(2, 1, 1)
    plt.plot(tpoints, xValues)
    plt.ylabel('ODE')

    plt.subplot(2, 1, 2)
    plt.plot(tpoints, np.cos(tpoints))
    plt.ylabel('Analytical Solution')
    plt.xlabel('t')
    plt.show()

    # Sous question b :
    x1 = [0.0, 0.5, 1.0, 1.5, 2.0]
    for x in x1:
        label = 'x(0)={}'.replace('{}', str(x))
        tpoints, xValues = oscillator.methodRK4(1000, x, 0.0)
        plt.plot(tpoints, xValues, label=label)
    plt.ylabel('ODE')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question c :
    aOscillator = AnharmonicOscillator(1, 0, 50)
    x1 = [0.0, 1.0, 2.0]
    for x in x1:
        label = 'x(0)={}'.replace('{}', str(x))
        tpoints, xValues = aOscillator.methodRK4(1000, x, 0.0)
        plt.plot(tpoints, xValues, label=label)
    plt.ylabel('ODE')
    plt.xlabel('t')
    plt.legend()
    plt.show()