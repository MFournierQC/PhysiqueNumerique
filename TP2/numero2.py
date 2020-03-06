import numpy as np
import matplotlib.pyplot as plt


def y1(energy):
    w = 1e-9
    m = 9.1094e-31
    hbar = 1.0545718e-34
    return np.tan(np.sqrt(((w ** 2) * m * (energy * 1.602176565e-19)) / (2 * (hbar ** 2))))


def evenStates(energy):
    v = 20
    return np.sqrt((v - energy) / energy)


def unevenStates(energy):
    v = 20
    return -np.sqrt(energy / (v - energy))


def bisection(function1, function2, min, max):
    previousxmid = 0
    xmin = min
    xmid = (min + max) / 2
    xmax = max
    while abs(previousxmid - xmid) > 0.001:
        if (function1(xmax) - function2(xmax)) * (function1(xmid) - function2(xmid)) < 0:
            xmin = xmid
        elif (function1(xmid) - function2(xmid)) * (function1(xmin) - function2(xmin)) < 0:
            xmax = xmid
        elif function1(xmid) - function2(xmid) == 0:
            return xmid
        previousxmid = xmid
        xmid = (xmin + xmax) / 2
    return xmid


if __name__ == '__main__':
    print(bisection(y1, unevenStates, 1, 2))
    print(bisection(y1, evenStates, 2, 3))
    print(bisection(y1, unevenStates, 4, 6))
    print(bisection(y1, evenStates, 7, 8))
    print(bisection(y1, unevenStates, 10, 12))
    print(bisection(y1, evenStates, 14, 17))

    energies = np.linspace(0.001, 19.999, 200)
    plt.plot(energies, y1(energies), label=r'$y_{1}$')
    plt.plot(energies, evenStates(energies), label='Even states')
    plt.plot(energies, unevenStates(energies), label='Uneven States')
    plt.axis(ymin=-7.5, ymax=7.5)
    plt.xlabel('Energy [eV]')
    plt.legend()
    plt.show()