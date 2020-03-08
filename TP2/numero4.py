import numpy as np
from scipy import constants

##Numéro 4 b.
def faiseur_vecteurs_u_et_q(matrice):
    """
    Fonction qui prend une matrice carrée et qui retourne c'est vecteurs u et q
    :param matrice: (numpy array) matrice carré
    :return: (dictionnaire) dictionnaire contenant les vecteurs u et q sous forme matricielle où les colones sont les
    vecteurs
    """
    vecteurs_u = np.zeros((len(matrice), len(matrice)))
    vecteurs_q = np.zeros((len(matrice), len(matrice)))

    for i in range(len(matrice)):
        u_jetable = matrice[:, i]
        projection = np.zeros(len(matrice))
        for j in range(i):
            projection += np.dot(vecteurs_q[:, j], u_jetable) * vecteurs_q[:, j]
        vecteurs_u[:, i] = u_jetable - projection
        vecteurs_q[:, i] = (vecteurs_u[:, i])/np.linalg.norm(vecteurs_u[:, i])

    return {"vecteurs_u": vecteurs_u, "vecteurs_q": vecteurs_q}


def decomposition_QR(matrice):
    """
    Fonction qui fait la decomposition QR d'un matrice.
    :param matrice: Matrice carrée sur laquelle on fait la décomposition QR
    :return: Dictionnaire qui contient matrice Q et matrice R
    """
    vecteurs_u = faiseur_vecteurs_u_et_q(matrice)["vecteurs_u"]
    vecteurs_q = faiseur_vecteurs_u_et_q(matrice)["vecteurs_q"]

    matrice_Q = vecteurs_q
    matrice_R = np.zeros((len(matrice), len(matrice)))

    for i in range(len(matrice)):
        for j in range(i+1):
            if j == i:
                matrice_R[j, i] = np.linalg.norm(vecteurs_u[:, i])
            else:
                matrice_R[j, i] = np.dot(vecteurs_q[:, j], matrice[:, i])

    return {"matrice_Q": matrice_Q, "matrice_R": matrice_R}


B = np.array([[1, 4, 8, 4], [4, 2, 3, 7], [8, 3, 6, 9], [4, 7, 9, 2]])

print("La matrice Q de B est :")
print(decomposition_QR(B)["matrice_Q"])
print("\nLa matrice R de B est :")
print(decomposition_QR(B)["matrice_R"])
print("\nLe produit matricielle de la matrice Q avec la matrice R de B donne effitivement:")
print(np.dot(decomposition_QR(B)["matrice_Q"], decomposition_QR(B)["matrice_R"]))


##Numéro 4 c.
def verification_element_hors_diagonale(matrice, valeur_max):
    """
    Fonction qui vérifie que les éléments hors diagonale d'une matrice sont plus petit qu'une certaine valeur.
    :param matrice: (numpy array) Matrice carré.
    :param valeur_max: (float-like) Valeur que les éléments hors diagonale doivent être plus petit
    :return:(bool) True si les éléments hors diagonale sont plus petit, False sinon.
    """

    taille_matrice = len(matrice)
    objet_bool = True

    for i in range(taille_matrice):
        if not objet_bool:
            break
        for j in range(taille_matrice):
            if not objet_bool:
                break
            elif i != j and abs(matrice[i,j]) >= valeur_max:
                objet_bool = False

    return objet_bool

def valeur_et_vecteur_propre_decomposition_QR(matrice, valeur_max):
    """
    Fonction qui retourne les vecteurs et valeurs propre approximer avec la décomposition QR.
    :param matrice: (numpy array) Matrice carré
    :param valeur_max: (float-like) Valeur que les éléments hors diagonale doivent être plus petit
    :return: Dictionnaire qui contient matrice des vecteurs propre et matrice des valeur propre
    """
    matrice_vecteurs_propres = np.identity(len(matrice))

    matrice_A_jetable = np.dot(decomposition_QR(matrice)["matrice_R"], decomposition_QR(matrice)["matrice_Q"])
    matrice_vecteurs_propres = np.dot(matrice_vecteurs_propres, decomposition_QR(matrice)["matrice_Q"])
    i = 1
    while not verification_element_hors_diagonale(matrice_A_jetable, valeur_max):
        if i == 150000:
            print("Après 150000 itération le système ne converge pas, la matrice des valeurs propres est :")
            print(matrice_A_jetable)
            quit()
        i += 1
        matrice_A_jetable = np.dot(decomposition_QR(matrice_A_jetable)["matrice_R"],
                                   decomposition_QR(matrice_A_jetable)["matrice_Q"])
        matrice_vecteurs_propres = np.dot(matrice_vecteurs_propres, decomposition_QR(matrice_A_jetable)["matrice_Q"])


    return {"matrice_V": matrice_vecteurs_propres, "matrice_A": matrice_A_jetable}

print("\nLa matrice des valeurs propres de B si la limite maximal est 1e-6 est:")
print(valeur_et_vecteur_propre_decomposition_QR(B, 1e-6)["matrice_A"])
print("\nLa matrice des vecteurs propres de B si la limite maximal est 1e-6 est:")
print(valeur_et_vecteur_propre_decomposition_QR(B, 1e-6)["matrice_V"])
print("\nLa matrice des valeurs propres de B si la limite maximal est 1e-12 est:")
print(valeur_et_vecteur_propre_decomposition_QR(B, 1e-12)["matrice_A"])
print("\nLa matrice des vecteurs propres de B si la limite maximal est 1e-12 est:")
print(valeur_et_vecteur_propre_decomposition_QR(B, 1e-12)["matrice_V"])
print("\nLa matrice des valeurs propres de B si la limite maximal est 1e-18 est:")
print(valeur_et_vecteur_propre_decomposition_QR(B, 1e-18)["matrice_A"])
print("\nLa matrice des vecteurs propres de B si la limite maximal est 1e-18 est:")
print(valeur_et_vecteur_propre_decomposition_QR(B, 1e-18)["matrice_V"])