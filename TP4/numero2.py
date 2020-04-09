from relaxation import Relaxation
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    rows = 100
    columns = 200
    grid = np.ndarray(shape=(rows, columns), dtype=float)
    grid[:9, :].fill(150)
    grid[10:, :].fill(0)

    # Grid before relaxation.
    plt.imshow(grid)
    plt.colorbar(orientation='horizontal')
    plt.show()

    # Normal relaxation.
    print("Normal Relaxation Method.")
    relax = Relaxation(grid, "2")
    relax.relaxation(0.001)
    iterations, relaxationChanges, relaxationTimes = relax.performances()

    plt.imshow(relax.grid)
    plt.colorbar(orientation='horizontal')
    plt.show()

    # Gauss-Seidel Relaxation.
    print("Gauss-Seidel Relaxation Method.")
    relax = Relaxation(grid, "2")
    relax.relaxationGaussSeidel(0.001)
    gsIterations, gsRelaxationChanges, gsRelaxationTimes = relax.performances()

    plt.imshow(relax.grid)
    plt.colorbar(orientation='horizontal')
    plt.show()

    # Over relaxation.
    print("Over Relaxation Method.")
    relax = Relaxation(grid, "2")
    relax.overRelaxation(0.001, 0.0001)
    overIterations, overRelaxationChanges, overRelaxationTimes = relax.performances()

    plt.imshow(relax.grid)
    plt.colorbar(orientation='horizontal')
    plt.show()

    # Plot speed of convergence.
    # Changes per iterations.
    plt.plot(iterations, relaxationChanges, label='Relaxation')
    plt.plot(overIterations, overRelaxationChanges, label='Sur-relaxation')
    plt.plot(gsIterations, gsRelaxationChanges, label='Gauss-Seidel')
    plt.ylabel('Changement [%]')
    plt.xlabel('Itération [-]')
    plt.legend()
    plt.show()

    # Cumulative time of iterations per iterations.
    plt.plot(iterations, relaxationTimes, label='Relaxation')
    plt.plot(overIterations, overRelaxationTimes, label='Sur-relaxation')
    plt.plot(gsIterations, gsRelaxationTimes, label='Gauss-Seidel')
    plt.ylabel('Temps cumulé [s]')
    plt.xlabel('Itération [-]')
    plt.legend()
    plt.show()
