from TP3.HarmonicOscillator import HarmonicOscillator
from TP3.AnharmonicOscillator import AnharmonicOscillator
from TP3.VanDerPolOscillator import VanDerPolOscillator
from mpl_toolkits.mplot3d import Axes3D
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
    plt.show(block=False)
    plt.close()

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
    plt.show(block=False)
    plt.close()

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
    plt.show(block=False)
    plt.close()

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
    plt.show(block=False)
    plt.close()

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
    plt.show(block=False)
    plt.close()

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
    plt.show(block=False)
    plt.close()

    # Sous question f :
    initialStates = np.array([[1.0, 0.0], [2.0, 0.0], [3.0, 0.0]], float)
    plt.figure(figsize=(8, 4))
    for initialState in initialStates:
        tPoints, fx1Points, fx2Points = vdpOscillator.methodRK45(initialState)
        label = str(initialState)
        plt.plot(fx1Points, fx2Points, label=label)
    plt.ylabel(r'$\dot{x}(t)$')
    plt.xlabel('x(t)')
    plt.legend(loc='upper right')
    plt.show(block=False)
    plt.close()

    # Sous question g :
    initialState = np.array([1.0, 0.0], float)
    tPoints, fx1Points, fx2Points = vdpOscillator.methodRK45(initialState)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(fx1Points, fx2Points, tPoints)
    ax.set_xlabel('x(t)')
    ax.set_ylabel(r'$\dot{x}(t)$')
    ax.set_zlabel('t')
    plt.show(block=False)
    plt.close()

    # Here, we are looking for values of x(t) where x(t) is equal to 0 or close to that.
    # This translates to a position x and x + 1 where the sign of x(t) changes.
    # This allows us to find the period of the cycle as well as values of x(t), dx(t)/dt and t.
    positions = []
    for x in range(len(fx1Points) - 1):
        try:
            a = fx1Points[x]
            b = fx1Points[x + 1]
            if b * a < 0:
                positions.append([x, x + 1])
        except:
            pass

    meanValues = []
    for position in positions:
        x1 = position[0]
        x2 = position[1]
        meanX = (fx1Points[x1] + fx1Points[x2]) / 2
        meanDXDT = (fx2Points[x1] + fx2Points[x2]) / 2
        meanT = (tPoints[x1] + tPoints[x2]) / 2
        meanValues.append([meanX, meanDXDT, meanT])

    for meanValue in meanValues:
        string = 'Position : ' + str(meanValue[0]) + ', Vitesse : ' + str(meanValue[1]) + ', Temps : '\
                 + str(meanValue[2])
        print(string)