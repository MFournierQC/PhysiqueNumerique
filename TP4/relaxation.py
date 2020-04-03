import numpy as np


class Relaxation:
    def __init__(self, grid: np.ndarray):
        # The original and current grid.
        self.originalGrid = grid.copy()
        self.grid = grid
        self.prevGrid = None
        self.change = np.inf
        self.iterationCount = 0

        self.iterations = []
        self.changePerIteration = []

    # Basics functions for the class.
    def getChangesPerIter(self):
        return self.iterations, self.changePerIteration

    def calculateChange(self):
        oldGrid = self.prevGrid.copy().flatten()
        newGrid = self.grid.copy().flatten()
        change = np.sqrt(np.sum((oldGrid - newGrid) ** 2))

        self.iterations.append(self.iterationCount)
        self.changePerIteration.append(change)

        return change

    def setBoundaris(self):
        self.grid[:3, :].fill(150)
        self.grid[19, :].fill(0)

    # Functions for a basic relaxation.
    def relaxation(self, deltaV):
        while self.change > deltaV:
            self.iterate()
            self.iterationCount += 1

        print(f'Relaxation : Changement de {self.change * 100:.7f}% après {self.iterationCount} itérations')

    def iterate(self):
        newGrid = self.grid.copy()
        self.prevGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][2:-2, 2:-2]
        newGrid[2:-2, 2:-2] = (self.grid[:-4, 2:-2] + self.grid[4:, 2:-2] + self.grid[2:-2, :-4] +
                               self.grid[2:-2, 4:]) / 4 + (1 / (4 * r)) * (self.grid[3:-1, 2:-2] - self.grid[1:-3, 2:-2])

        self.grid = newGrid
        self.setBoundaris()
        self.change = self.calculateChange()

    # Functions for a Gauss-Seidel relaxation.
    def relaxationGaussSeidel(self, deltaV):
        while self.change > deltaV:
            self.iterateGaussSeidel()
            self.iterationCount += 1

        print(f'Gauss-Seidel : Changement de {self.change * 100:.7f}% après {self.iterationCount} itérations')

    def iterateGaussSeidel(self):
        self.prevGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][2:-2, 2:-2]
        self.grid[2:-2, 2:-2] = (self.grid[:-4, 2:-2] + self.grid[4:, 2:-2] + self.grid[2:-2, :-4] +
                               self.grid[2:-2, 4:]) / 4 + (1 / (4 * r)) * (self.grid[3:-1, 2:-2] - self.grid[1:-3, 2:-2])

        self.setBoundaris()
        self.change = self.calculateChange()

    # Functions for an over relaxation.
    def overRelaxation(self, deltaV, omega):
        while self.change > deltaV:
            self.iterateOverRelaxation(omega)
            self.iterationCount += 1

        print(f'Sur-Relaxation : Changement de {self.change * 100:.7f}% après {self.iterationCount} itérations')

    def iterateOverRelaxation(self, omega):
        newGrid = self.grid.copy()
        self.prevGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][2:-2, 2:-2]
        newGrid[2:-2, 2:-2] = (self.grid[:-4, 2:-2] + self.grid[4:, 2:-2] + self.grid[2:-2, :-4] +
                               self.grid[2:-2, 4:]) / 4 + (1 / (4 * r)) * (self.grid[3:-1, 2:-2] - self.grid[1:-3, 2:-2])
        overRelaxedGrid = self.prevGrid + (1 + omega) * (newGrid - self.prevGrid)

        self.grid = overRelaxedGrid
        self.setBoundaris()
        self.change = self.calculateChange()