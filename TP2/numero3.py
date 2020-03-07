from gaussxw import gaussxw
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

def integrale_gausienne(fonction, a, b, N):

    """
    Fonction qui calcule l'intégrale de la fonction entre les bornes a et b de façon numérique en utilisant la méthode
    gauss avec N pas.
    :param fonction: La fonction à intégrer.
    :param a: La borne inférieur.
    :param b: La borne supérieur.
    :param N: Nombre de pas.
    :return: La valeur de l'intégrale.
    """
    x, w = gaussxw(N)
    xp = 0.5 * (b-a) * x + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w

    # Perform the integration
    s = 0.0
    for k in range(N):
        s += wp[k] * fonction(xp[k])

    return s

def fonction_spectre_electromag(x):

    return x ** 3 / (np.exp(x) - 1)

def changement_variable(lamb, T):

    h = constants.h
    c = constants.c
    kB = constants.k

    return h * c / (lamb * kB * T)


def eta_visible(T):

    lamb_1 = 390e-9
    lamb_2 = 750e-9

    eta = 15/(np.pi ** 4) * integrale_gausienne(fonction_spectre_electromag,
                                          changement_variable(lamb_2, T), changement_variable(lamb_1, T), 100)

    return eta

temperatures_300_10000 = np.linspace(300,10000,100)

eta_300_10000 = np.array([eta_visible(i) for i in temperatures_300_10000])

plt.figure(figsize=(10, 8))
plt.plot(temperatures_300_10000, eta_300_10000, label="Efficacité en fonction de la température")
plt.xlabel('Température [K]', fontsize=24)
plt.ylabel('Efficacité', fontsize=24)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)
plt.show()


def methode_nombre_dor_max(fonction, x1_initiale, x4_initiale, incertitude):

    # Nombre d'or
    z = (1 + np.sqrt(5))/2

    # Valeurs initiales
    x1 = x1_initiale
    x4 = x4_initiale
    x2 = x4 - (x4 - x1) / z
    x3 = x1 + (x4 - x1) / z

    while (x4 - x1) > incertitude:
        if fonction(x2) > fonction(x3):
            x4, x3 = x3, x2
            x2 = x4 - (x4 - x1) / z
        else:
            x2, x1 = x3, x2
            x3 = x1 + (x4 - x1) / z

    return (x4 + x1) / 2

print("Le maximum se trouve à x = {}".format(str(methode_nombre_dor_max(eta_visible, 5000, 8000, 1))[:7]))

