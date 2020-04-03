from TP4.relaxation import Relaxation
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    rows = 20
    columns = 100
    grid = np.ndarray(shape=(rows, columns), dtype=float)
    grid[:3, :].fill(150)
    grid[4:, :].fill(0)

    # Normal relaxation.
    relax = Relaxation(grid)
    relax.relaxation(0.000001)
    iterations, relaxationChanges = relax.getChangesPerIter()

    plt.imshow(relax.grid)
    plt.show()

    # Gauss-Seidel Relaxation.
    #relax = Relaxation(grid)
    #relax.relaxationGaussSeidel(0.000001)
    #plt.imshow(relax.grid)
    #plt.show()

    # Over relaxation.
    relax = Relaxation(grid)
    relax.overRelaxation(0.000001, 0.0085)
    overIterations, overRelaxationChanges = relax.getChangesPerIter()

    plt.imshow(relax.grid)
    plt.show()

    # Plot speed of convergence.
    plt.plot(iterations, relaxationChanges)
    plt.plot(overIterations, overRelaxationChanges)
    plt.show()
