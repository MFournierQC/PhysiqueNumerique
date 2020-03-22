from TP3.HarmonicOscillator import HarmonicOscillator
from TP3.AnharmonicOscillator import AnharmonicOscillator
from TP3.VanDerPolOscillator import VanDerPolOscillator
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    oscillator = HarmonicOscillator(1, 0, 50)

    # Sous question a :
    tPoints, xValues, sValues = oscillator.methodRK4(1000, 1.0, 0.0)
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(tPoints, xValues)
    plt.ylabel('EDO')

    plt.subplot(2, 1, 2)
    plt.plot(tPoints, np.cos(tPoints))
    plt.ylabel('Solution analytique')
    plt.xlabel('t')
    plt.show()

    # Sous question b :
    origins = [0.0, 0.5, 1.0, 1.5, 2.0]
    plt.figure(figsize=(8, 4))
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues= oscillator.methodRK4(1000, origin, 0.0)
        plt.plot(tPoints, xValues, label=label)
    plt.ylabel('EDO')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question c :
    aOscillator = AnharmonicOscillator(1, 0, 50)
    origins = [0.0, 1.0, 2.0]
    plt.figure(figsize=(8, 4))
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = aOscillator.methodRK4(1000, origin, 0.0)
        plt.plot(tPoints, xValues, label=label)
    plt.ylabel('EDO')
    plt.xlabel('t')
    plt.legend()
    plt.show()

    # Sous question d :
    origins = [0.0, 0.5, 1.0, 1.5, 2.0]
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = oscillator.methodRK4(1000, origin, 0.0)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('EDO Harmonique')
    plt.legend()

    plt.subplot(2, 1, 2)
    for origin in origins:
        label = 'x(0)={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = aOscillator.methodRK4(1000, origin, 0.0)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('EDO Anharmonique')
    plt.xlabel('x')
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    for origin in origins:
        label = r'$\dot{x}(0)$={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = oscillator.methodRK4(1000, 1.0, origin)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('EDO Harmonique')
    plt.legend()

    plt.subplot(2, 1, 2)
    for origin in origins:
        label = r'$\dot{x}(0)$={}'.replace('{}', str(origin))
        tPoints, xValues, sValues = aOscillator.methodRK4(1000, 1.0, origin)
        plt.plot(xValues, sValues, label=label)
    plt.ylabel('EDO Anharmonique')
    plt.xlabel('x')
    plt.legend()
    plt.show()

    # Sous question e :
    vdpOscillator = VanDerPolOscillator(1)
    initialStates = np.array([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0]], float)
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    for initialState in initialStates:
        tPoints, fx1Points, fx2Points = vdpOscillator.methodRK45(initialState)
        label = str(initialState)
        plt.plot(tPoints, fx1Points, label=label)
    plt.ylabel('x(t)')
    plt.legend(loc='upper right')

    initialStates = np.array([[0.5, 0.0], [0.5, 1.0], [0.5, 2.0]], float)
    plt.subplot(2, 1, 2)
    for initialState in initialStates:
        tPoints, fx1Points, fx2Points = vdpOscillator.methodRK45(initialState)
        label = str(initialState)
        plt.plot(tPoints, fx2Points, label=label)
    plt.ylabel(r'$\dot{x}(t)$')
    plt.xlabel('t')
    plt.legend(loc='upper right')
    plt.show()