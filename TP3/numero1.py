from TP3.HarmonicOscillator import HarmonicOscillator
from TP3.AnharmonicOscillator import AnharmonicOscillator
from TP3.VanDerPolOscillator import VanDerPolOscillator
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    oscillator = HarmonicOscillator(1, 0, 50)

    # Sous question a :
    tPoints, xValues, sValues = oscillator.methodRK4(1000, 1.0, 0.0)
    plt.subplot(2, 1, 1)
    plt.plot(tPoints, xValues)
    plt.ylabel('ODE')

    plt.subplot(2, 1, 2)
    plt.plot(tPoints, np.cos(tPoints))
    plt.ylabel('Analytical Solution')
    plt.xlabel('t')
    plt.show()

    # Sous question b :
    origins = [0.0, 0.5, 1.0, 1.5, 2.0]
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues= oscillator.methodRK4(1000, origin, 0.0)
        plt.plot(tPoints, xValues, label=label)
    plt.ylabel('ODE')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question c :
    aOscillator = AnharmonicOscillator(1, 0, 50)
    origins = [0.0, 1.0, 2.0]
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = aOscillator.methodRK4(1000, origin, 0.0)
        plt.plot(tPoints, xValues, label=label)
    plt.ylabel('ODE')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question d :
    origins = [0.0, 0.5, 1.0, 1.5, 2.0]
    plt.subplot(2, 1, 1)
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = oscillator.methodRK4(1000, origin, 0.0)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Harmonic ODE')
    plt.legend()

    plt.subplot(2, 1, 2)
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = aOscillator.methodRK4(1000, origin, 0.0)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Anharmonic ODE')
    plt.xlabel('x')
    plt.legend()
    plt.show()

    plt.subplot(2, 1, 1)
    for origin in origins:
        label = r'$\dot{x}(0)$={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = oscillator.methodRK4(1000, 1.0, origin)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Harmonic ODE')
    plt.legend()

    plt.subplot(2, 1, 2)
    for origin in origins:
        label = r'$\dot{x}(0)$={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = aOscillator.methodRK4(1000, 1.0, origin)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('Anharmonic ODE')
    plt.xlabel('x')
    plt.legend()
    plt.show()

    # Sous question e :
    vdpOscillator = VanDerPolOscillator(1)
    initialState = np.array([0.5, 0.0], float)
    tPoints, fx1Points, fx2Points = vdpOscillator.methodRK45(initialState)

    plt.plot(tPoints, fx1Points)
    plt.plot(tPoints, fx2Points)
    plt.show()