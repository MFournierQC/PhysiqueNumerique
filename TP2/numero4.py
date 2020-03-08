import numpy as np
from scipy import constants

def faiseur_vecteurs_u_et_q(matrice):

    vecteurs_u = np.zeros((len(matrice), len(matrice)))
    vecteurs_q = np.zeros((len(matrice), len(matrice)))

    for i in range(len(matrice)):
        u_jetable = matrice[:, i]
        projection = np.zeros(len(matrice))
        for j in range(i):
            projection += np.dot(vecteurs_q[:, j], u_jetable) * vecteurs_q[:, j]
        print(str(i) + " --> " + str(projection))
        vecteurs_u[:, i] = u_jetable - projection
        vecteurs_q[:, i] = (u_jetable - projection)/np.linalg.norm(u_jetable - projection)
        print(vecteurs_u[:, i])
    return {"vecteurs_u": np.array(vecteurs_u), "vecteurs_q":np.array(vecteurs_q)}

def decomposition_QR(matrice):
    vecteurs_u = faiseur_vecteurs_u_et_q(matrice)["vecteurs_u"]
    vecteurs_q = faiseur_vecteurs_u_et_q(matrice)["vecteurs_q"]

    matrice_Q = vecteurs_q
    matrice_R = np.zeros((len(matrice), len(matrice)))

    for i in range(len(matrice)):
        for j in range(i + 1):
            if j == i:
                matrice_R[j, i] = np.linalg.norm(vecteurs_u[:, i])
            else:
                matrice_R[j, i] = np.dot(vecteurs_q[:, i], matrice[:, i])

    return {"matrice_Q":matrice_Q, "matrice_R":matrice_R}


B = np.array([[1, 4, 8, 4], [4, 2, 3, 7], [8, 3, 6, 9], [4, 7, 9, 2]])

#print(decomposition_QR(B)["matrice_Q"])

#print(decomposition_QR(B)["matrice_R"])

print(faiseur_vecteurs_u_et_q(B)["vecteurs_u"])


print(np.dot(decomposition_QR(B)["matrice_Q"], decomposition_QR(B)["matrice_Q"]))


m = np.array([[1,2],[3,4]])

print(m[:,0])

