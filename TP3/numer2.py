import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

class Corps():
    """
    Cette classe est un corps qui a une masse, une position et une vitesse, ceci en 2D.
    """

    def __init__(self, masse, position, vitesse):
        """
        Constructeur de la classe.
        :param position_x (float-like): Position en x du corps.
        :param position_y (float-like): Position en x du corps.
        :param vitesse_x (float-like): Position en x du corps.
        :param vitesse_y (float-like): Position en x du corps.
        """
        self._masse = masse
        self._position = position
        self._vitesse = vitesse

    @property
    def masse(self):
        return self._masse

    @masse.setter
    def masse(self, masse):
        self._masse = masse

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse


class Systeme_de_corps():
    """
    Classe qui permet d'avoir un système de masse avec un force entre les corps.
    """
    def __init__(self, **kwargs):
        """
        Constructeur de la classe qui permet de mettre en place les corps ainsi que la force qui les reli
        :param kwargs:
        """
        self.tout_les_corps = kwargs
        self.temps = []
        self.positions = [{i: self.tout_les_corps[i].position for i in self.tout_les_corps}]
        self.vitesses = [{i: self.tout_les_corps[i].vitesse for i in self.tout_les_corps}]
        self.acceleration = [{i: self.calcul_acceleration(i) for i in self.tout_les_corps}]

    def calcul_acceleration(self, cle_masse):
        liste_cle = [*self.tout_les_corps.keys()]
        liste_cle.remove(cle_masse)

        acceleration = 0
        for cle_loop in liste_cle:
            acceleration += 4 * (np.pi ** 2) * self.tout_les_corps[cle_loop].masse * \
                                      (np.linalg.norm(self.tout_les_corps[cle_masse].position -
                                                      self.tout_les_corps[cle_loop].position) ** -3) * \
                                      (self.tout_les_corps[cle_masse].position -
                                                      self.tout_les_corps[cle_loop].position)

        return acceleration

    def saute_mouton(self, temps_depart, temps_fin, temps_pas):

        self.temps.append(temps_depart)

        for i in range(numpy.ceil((temps_fin - temps_depart)/temps_pas)):
            self.temps.append(temps_depart + (i + 1) * temps_pas)
            position = {}
            vitesse = {}
            acceleration = {}

            for j in self.tout_les_corps:
                position_suivante = self.positions[i][j] + self.vitesses[i][j] * temps_pas + 1 / 2 *\
                                    self.acceleration[i][j] * (temps_pas ** 2)

                vitesse_suivante = self.vitesses[i][j]

            position = {i: Systeme_a.tout_les_corps[i].position for i in self.tout_les_corps}








if __name__ == "__main__":
    corps_A = Corps(3, np.array([1, 3]), np.array([0, 0]))
    corps_B = Corps(4, np.array([-2, -1]), np.array([0, 0]))
    corps_C = Corps(5, np.array([1, -1]), np.array([0, 0]))
    Systeme_a = Systeme_de_corps(corps_A=corps_A, corps_B=corps_B, corps_C=corps_C)
    {i: Systeme_a.tout_les_corps[i].position for i in Systeme_a.tout_les_corps}
    print({i: Systeme_a.tout_les_corps[i].position for i in Systeme_a.tout_les_corps})
    liste_lol = [*Systeme_a.tout_les_corps.keys()]
    liste_lol.remove("corps_A")


    print(np.array[])