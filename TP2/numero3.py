from gaussxw import gaussxw
import numpy as np

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

    h = 6.62067004e-34
    c = 299792458
    kB = 1.38064852e-23
    
    return h * c / (lamb * kB * T)