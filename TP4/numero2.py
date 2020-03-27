from TP4.relaxation import Relaxation
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Essai 1
    #rows = 200
    #columns = 1000
    #grid = np.ndarray(shape=(rows, columns), dtype=float)
    #grid[:89, :].fill(0)
    #grid[90:110, :].fill(150)
    #grid[111:, :].fill(0)

    #relax = Relaxation(grid, 5000)
    #relax(5000)
    #plt.imshow(relax.getGrid())
    #plt.show()

    rows = 20
    columns = 100
    grid = np.ndarray(shape=(rows, columns), dtype=float)
    grid[:3, :].fill(150)
    grid[4:, :].fill(0)

    plt.imshow(grid)
    plt.show()

    relax = Relaxation(grid, 2000)
    relax(2000)
    plt.imshow(relax.grid)
    plt.show()