from gaussxw import gaussxw


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

