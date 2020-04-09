from relaxation import Relaxation
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    numero = input("Quelle numero voulez-vous faire (3b ou 3c) : ")

    if numero == "3b":
        rows = 100
        columns = 360
        grid = np.ndarray(shape=(rows, columns), dtype=float)
        grid[:9, 30:-30].fill(150)
        grid[99, 0:90].fill(0)
        grid[49:99, 90:270].fill(0)
        grid[99, 270:].fill(0)
        gridboundary = grid.copy()
        # Grid before relaxation.
        plt.imshow(grid)
        plt.colorbar(orientation='horizontal')
        plt.show()



    else:
        rows = 100
        columns = 330
        grid = np.ndarray(shape=(rows, columns), dtype=float)
        grid[:9, 20:-10].fill(150)
        grid[99, 0:100].fill(0)
        grid[79:, 100:220].fill(0)
        grid[39:, 220:].fill(0)
        # Grid before relaxation.
        plt.imshow(grid)
        plt.colorbar(orientation='horizontal')
        plt.show()

    # Normal relaxation.
    print("Normal Relaxation Method.")
    relax = Relaxation(grid, numero)
    relax.relaxation(0.001)

    plt.imshow(relax.grid)

    plt.colorbar(orientation='horizontal')
    plt.show()
