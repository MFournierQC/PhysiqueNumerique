import numpy as np
import matplotlib.pyplot as plt


def wiensLaw(x):
    return -5*np.exp(-x) + 5


def relaxationMethod(function, precision, initialValue):
    i = 0
    x = initialValue
    while not function(x) - x < precision:
        x = function(x)
        i += 1
    return x, i


if __name__ == '__main__':
    print(relaxationMethod(wiensLaw, 1e-6, 0.1))

    x = np.linspace(-0.1, 7, 1000)
    plt.plot(x, wiensLaw(x), label=r"$f(x)=5-5e^{-x}$")
    plt.plot(x, x, label=r'$f(x)=x$', linestyle='--')
    plt.legend()
    plt.show()