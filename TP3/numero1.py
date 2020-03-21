from TP3.HarmonicOscillator import HarmonicOscillator
from TP3.AnharmonicOscillator import AnharmonicOscillator
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    oscillator = HarmonicOscillator(1, 0, 50)

    # Sous question a :
    tpoints, xValues, sValues = oscillator.methodRK4(1000, 1.0, 0.0)
    plt.subplot(2, 1, 1)
    plt.plot(tpoints, xValues)
    plt.ylabel('ODE')

    plt.subplot(2, 1, 2)
    plt.plot(tpoints, np.cos(tpoints))
    plt.ylabel('Analytical Solution')
    plt.xlabel('t')
    plt.show()

    # Sous question b :
    origins = [0.0, 0.5, 1.0, 1.5, 2.0]
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tpoints, xValues, sValues= oscillator.methodRK4(1000, origin, 0.0)
        plt.plot(tpoints, xValues, label=label)
    plt.ylabel('ODE')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question c :
    aOscillator = AnharmonicOscillator(1, 0, 50)
    origins = [0.0, 1.0, 2.0]
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tpoints, xValues, sValues = aOscillator.methodRK4(1000, origin, 0.0)
        plt.plot(tpoints, xValues, label=label)
    plt.ylabel('ODE')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question d :
    origins = [0.0, 0.5, 1.0, 1.5, 2.0]
    plt.subplot(2, 1, 1)
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tpoints, xValues, sValues = oscillator.methodRK4(1000, origin, 0.0)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Harmonic ODE')
    plt.legend()

    plt.subplot(2, 1, 2)
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tpoints, xValues, sValues = aOscillator.methodRK4(1000, origin, 0.0)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Anharmonic ODE')
    plt.xlabel('x')
    plt.legend()
    plt.show()

    plt.subplot(2, 1, 1)
    for origin in origins:
        label = r'$\dot{x}(0)$={}'.replace('{}', str(origin))
        tpoints, xValues, sValues = oscillator.methodRK4(1000, 1.0, origin)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Harmonic ODE')
    plt.legend()

    plt.subplot(2, 1, 2)
    for origin in origins:
        label = r'$\dot{x}(0)$={}'.replace('{}', str(origin))
        tpoints, xValues, sValues = aOscillator.methodRK4(1000, 1.0, origin)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Anharmonic ODE')
    plt.xlabel('x')
    plt.legend()
    plt.show()