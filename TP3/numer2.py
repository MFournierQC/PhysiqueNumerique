import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation

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
                                      (np.linalg.norm(self.tout_les_corps[cle_loop].position -
                                                      self.tout_les_corps[cle_masse].position) ** -3) * \
                                      (self.tout_les_corps[cle_loop].position - self.tout_les_corps[cle_masse].position)

        return acceleration

    def saute_mouton(self, temps_depart, temps_fin, temps_pas):

        self.temps.append(temps_depart)

        for i in range(int(np.ceil((temps_fin - temps_depart)/temps_pas))):
            self.temps.append(temps_depart + (i + 1) * temps_pas)
            position = {}
            vitesse = {}
            acceleration = {}

            for j in self.tout_les_corps:
                position_suivante = self.positions[i][j] + self.vitesses[i][j] * temps_pas + 1 / 2 *\
                                    self.acceleration[i][j] * (temps_pas ** 2)
                self.tout_les_corps[j].position = position_suivante

                acceleration_suivante = self.calcul_acceleration(j)
                vitesse_suivante = self.vitesses[i][j] + 1 / 2 * (self.acceleration[i][j] + acceleration_suivante) \
                                   * temps_pas

                position[j] = position_suivante
                vitesse[j] = vitesse_suivante
                acceleration[j] = acceleration_suivante

            self.positions.append(position)
            self.vitesses.append(vitesse)
            self.acceleration.append(acceleration)









if __name__ == "__main__":

    animation_lecteur = input("Quelle animation voulez vous voir? (1, 2, 3, 4 ou 5) : ")

    ###Numero a.
    if animation_lecteur == "1":
        corps_A = Corps(3, np.array([1, 3]), np.array([0, 0]))
        corps_B = Corps(4, np.array([-2, -1]), np.array([0, 0]))
        corps_C = Corps(5, np.array([1, -1]), np.array([0, 0]))
        Systeme_a = Systeme_de_corps(corps_A=corps_A, corps_B=corps_B, corps_C=corps_C)
        Systeme_a.saute_mouton(0, 1, 0.0001)

        position_des_corps_a = np.array([[[i["corps_A"][0] for i in Systeme_a.positions],
                               [i["corps_A"][1] for i in Systeme_a.positions]],
                              [[i["corps_B"][0] for i in Systeme_a.positions],
                               [i["corps_B"][1] for i in Systeme_a.positions]],
                              [[i["corps_C"][0] for i in Systeme_a.positions],
                               [i["corps_C"][1] for i in Systeme_a.positions]]])


        fig = plt.figure()

        ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
        line, = ax.plot([], [], 'o', color="red")


        def init():
            line.set_data([], [])
            return line,


        def animate(i):
            global position_des_corps_a
            p = position_des_corps_a
            x = [p[0, 0, i*10], p[1, 0, i*10], p[2, 0, i*10]]
            y = [p[0, 1, i*10], p[1, 1, i*10], p[2, 1, i*10]]
            line.set_data(x, y)
            return line,


        ani_a = FuncAnimation(fig, animate, init_func=init,
                             frames=1000, interval=10, repeat=False)
        plt.show()


    ###Numero b
    if animation_lecteur == "2":
        corps_A_b = Corps(3, np.array([1, 3]), np.array([0, 0]))
        corps_B_b  = Corps(4, np.array([-2, -1]), np.array([0, 0]))
        corps_C_b  = Corps(5, np.array([1, -1]), np.array([0, 0]))
        Systeme_b = Systeme_de_corps(corps_A=corps_A_b, corps_B=corps_B_b, corps_C=corps_C_b)
        Systeme_b.saute_mouton(0, 10, 0.0001)

        position_des_corps_b = np.array([[[i["corps_A"][0] for i in Systeme_b.positions],
                               [i["corps_A"][1] for i in Systeme_b.positions]],
                              [[i["corps_B"][0] for i in Systeme_b.positions],
                               [i["corps_B"][1] for i in Systeme_b.positions]],
                              [[i["corps_C"][0] for i in Systeme_b.positions],
                               [i["corps_C"][1] for i in Systeme_b.positions]]])


        fig = plt.figure()

        ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
        line, = ax.plot([], [], 'o', color="red")


        def init():
            line.set_data([], [])
            return line,


        def animate(i):
            global position_des_corps_b
            p = position_des_corps_b
            x = [p[0, 0, i*10], p[1, 0, i*10], p[2, 0, i*10]]
            y = [p[0, 1, i*10], p[1, 1, i*10], p[2, 1, i*10]]
            line.set_data(x, y)
            return line,


        ani_b = FuncAnimation(fig, animate, init_func=init,
                             frames=10000, interval=1, repeat=False)
        plt.show()

    ###Numero c..
    ###Corps à la position donné dans l'énoncé.
    if animation_lecteur in ["3", "4", "5"]:
        corps_A_c = Corps(1, np.array([3.3030197, -0.82771837]), np.array([1.587433767, 1.47221479]))
        corps_B_c = Corps(1, np.array([-3.3030197, 0.82771837]), np.array([1.587433767, 1.47221479]))
        corps_C_c = Corps(1, np.array([0, 0]), np.array([-3.174867535, -2.94442961]))
        Systeme_c = Systeme_de_corps(corps_A=corps_A_c, corps_B=corps_B_c, corps_C=corps_C_c)
        Systeme_c.saute_mouton(0, 50, 0.001)

        position_des_corps_c = np.array([[[i["corps_A"][0] for i in Systeme_c.positions],
                               [i["corps_A"][1] for i in Systeme_c.positions]],
                              [[i["corps_B"][0] for i in Systeme_c.positions],
                               [i["corps_B"][1] for i in Systeme_c.positions]],
                              [[i["corps_C"][0] for i in Systeme_c.positions],
                               [i["corps_C"][1] for i in Systeme_c.positions]]])

    ###Changement de la positon de C
    if animation_lecteur == "3":
        corps_A_d = Corps(1, np.array([3.3030197, -0.82771837]), np.array([1.587433767, 1.47221479]))
        corps_B_d = Corps(1, np.array([-3.3030197, 0.82771837]), np.array([1.587433767, 1.47221479]))
        corps_C_d = Corps(1, np.array([0 + np.random.uniform(low=-0.1, high=0.1),
                                       0 + np.random.uniform(low=-0.1, high=0.1)]), np.array([-3.174867535, -2.94442961]))
        Systeme_d = Systeme_de_corps(corps_A=corps_A_d, corps_B=corps_B_d, corps_C=corps_C_d)
        Systeme_d.saute_mouton(0, 50, 0.001)

        position_des_corps_d = np.array([[[i["corps_A"][0] for i in Systeme_d.positions],
                                          [i["corps_A"][1] for i in Systeme_d.positions]],
                                         [[i["corps_B"][0] for i in Systeme_d.positions],
                                          [i["corps_B"][1] for i in Systeme_d.positions]],
                                         [[i["corps_C"][0] for i in Systeme_d.positions],
                                          [i["corps_C"][1] for i in Systeme_d.positions]]])


    ###Changement de la vitesse de C
    if animation_lecteur == "4":
        corps_A_e = Corps(1, np.array([3.3030197, -0.82771837]), np.array([1.587433767, 1.47221479]))
        corps_B_e = Corps(1, np.array([-3.3030197, 0.82771837]), np.array([1.587433767, 1.47221479]))
        corps_C_e = Corps(1, np.array([0, 0]), np.array([-3.174867535 + np.random.uniform(low=-3.174867535 * 0.01, high=3.174867535 * 0.01),
                                    -2.94442961 + np.random.uniform(low=-2.94442961 * 0.01, high=2.94442961 * 0.01)]))
        Systeme_e = Systeme_de_corps(corps_A=corps_A_e, corps_B=corps_B_e, corps_C=corps_C_e)
        Systeme_e.saute_mouton(0, 50, 0.001)

        position_des_corps_e = np.array([[[i["corps_A"][0] for i in Systeme_e.positions],
                                          [i["corps_A"][1] for i in Systeme_e.positions]],
                                         [[i["corps_B"][0] for i in Systeme_e.positions],
                                          [i["corps_B"][1] for i in Systeme_e.positions]],
                                         [[i["corps_C"][0] for i in Systeme_e.positions],
                                          [i["corps_C"][1] for i in Systeme_e.positions]]])

    ###Invertion vitesse
    if animation_lecteur == "5":
        corps_A_f = Corps(1, np.array([3.3030197, -0.82771837]), np.array([-1.587433767, -1.47221479]))
        corps_B_f = Corps(1, np.array([-3.3030197, 0.82771837]), np.array([-1.587433767, -1.47221479]))
        corps_C_f = Corps(1, np.array([0, 0]), np.array([3.174867535, 2.94442961]))
        Systeme_f = Systeme_de_corps(corps_A=corps_A_f, corps_B=corps_B_f, corps_C=corps_C_f)
        Systeme_f.saute_mouton(0, 50, 0.001)

        position_des_corps_f = np.array([[[i["corps_A"][0] for i in Systeme_f.positions],
                                          [i["corps_A"][1] for i in Systeme_f.positions]],
                                         [[i["corps_B"][0] for i in Systeme_f.positions],
                                          [i["corps_B"][1] for i in Systeme_f.positions]],
                                         [[i["corps_C"][0] for i in Systeme_f.positions],
                                          [i["corps_C"][1] for i in Systeme_f.positions]]])


    if animation_lecteur == "3":
        ###Changement random de la position de départ de la particule C.
        fig = plt.figure()

        ax = plt.axes(xlim=(-7.5, 7.5), ylim=(-5, 5))

        lines = [plt.plot([], [], 'o', color=["red", "blue"][_])[0] for _ in range(2)]


        def init():
            for line in lines:
                line.set_data([], [])

            return lines


        def animate(i):
            global position_des_corps_c
            global position_des_corps_d

            x = [[position_des_corps_c[0, 0, i*10], position_des_corps_c[1, 0, i*10], position_des_corps_c[2, 0, i*10]],
                 [position_des_corps_d[0, 0, i*10], position_des_corps_d[1, 0, i*10], position_des_corps_d[2, 0, i*10]]]
            y = [[position_des_corps_c[0, 1, i*10], position_des_corps_c[1, 1, i*10], position_des_corps_c[2, 1, i*10]],
                 [position_des_corps_d[0, 1, i*10], position_des_corps_d[1, 1, i*10], position_des_corps_d[2, 1, i*10]]]

            for j, line in enumerate(lines):
                line.set_data(x[j], y[j])

            return lines


        anim_d = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=5000, interval=1, repeat=False)

        plt.show()

    ###Changement random de la vitesse de départ de la particule C.
    if animation_lecteur == "4":
        fig = plt.figure()

        ax = plt.axes(xlim=(-7.5, 7.5), ylim=(-5, 5))

        lines = [plt.plot([], [], 'o', color=["red", "blue"][_])[0] for _ in range(2)]


        def init():
            for line in lines:
                line.set_data([], [])

            return lines


        def animate(i):
            global position_des_corps_c
            global position_des_corps_e

            x = [[position_des_corps_c[0, 0, i*10], position_des_corps_c[1, 0, i*10], position_des_corps_c[2, 0, i*10]],
                 [position_des_corps_e[0, 0, i*10], position_des_corps_e[1, 0, i*10], position_des_corps_e[2, 0, i*10]]]
            y = [[position_des_corps_c[0, 1, i*10], position_des_corps_c[1, 1, i*10], position_des_corps_c[2, 1, i*10]],
                 [position_des_corps_e[0, 1, i*10], position_des_corps_e[1, 1, i*10], position_des_corps_e[2, 1, i*10]]]

            for j, line in enumerate(lines):
                line.set_data(x[j], y[j])

            return lines


        anim_e = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=5000, interval=1, repeat=False)

        plt.show()

    ###Changement random de la vitesse de départ de la particule C.
    if animation_lecteur == "5":
        fig = plt.figure()

        ax = plt.axes(xlim=(-7.5, 7.5), ylim=(-5, 5))

        lines = [plt.plot([], [], 'o', color=["red", "blue"][_])[0] for _ in range(2)]


        def init():
            for line in lines:
                line.set_data([], [])

            return lines


        def animate(i):
            global position_des_corps_c
            global position_des_corps_f

            x = [[position_des_corps_c[0, 0, i * 10], position_des_corps_c[1, 0, i * 10],
                  position_des_corps_c[2, 0, i * 10]],
                 [position_des_corps_f[0, 0, i * 10], position_des_corps_f[1, 0, i * 10],
                  position_des_corps_f[2, 0, i * 10]]]
            y = [[position_des_corps_c[0, 1, i * 10], position_des_corps_c[1, 1, i * 10],
                  position_des_corps_c[2, 1, i * 10]],
                 [position_des_corps_f[0, 1, i * 10], position_des_corps_f[1, 1, i * 10],
                  position_des_corps_f[2, 1, i * 10]]]

            for j, line in enumerate(lines):
                line.set_data(x[j], y[j])

            return lines


        anim_e = animation.FuncAnimation(fig, animate, init_func=init,
                                         frames=5000, interval=1, repeat=False)

        plt.show()