import numpy as np
import time

import matplotlib.pyplot as plt


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
        self.timePerIteration = []

        self.mask = None
        self.notMask = None

    # Basics functions for the class.
    def performances(self):
        return self.iterations, self.changePerIteration, np.cumsum(self.timePerIteration)

    def calculateChange(self):
        oldGrid = self.prevGrid.copy().flatten()
        newGrid = self.grid.copy().flatten()
        change = np.sqrt(np.sum((oldGrid - newGrid) ** 2))

        self.iterations.append(self.iterationCount)
        self.changePerIteration.append(change)

        return change

    def setBoundaris(self):
        self.grid[:9, :].fill(150)
        self.grid[99, :].fill(0)

    # Functions for a basic relaxation.
    def relaxation(self, deltaV):
        while self.change > deltaV:
            begin = time.perf_counter()
            self.iterate()
            end = time.perf_counter()
            self.timePerIteration.append(end - begin)
            self.iterationCount += 1

        print(f'Relaxation : Changement de {self.change * 100:.7f}% après {self.iterationCount} itérations')

    def iterate(self):
        newGrid = self.grid.copy()
        self.prevGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][1:-1, 1:-1]
        newGrid[1:-1, 1:-1] = (self.grid[:-2, 1:-1] + self.grid[2:, 1:-1] + self.grid[1:-1, :-2] +
                               self.grid[1:-1, 2:]) / 4 + (1 / (8 * r)) * (self.grid[2:, 1:-1] -
                                                                           self.grid[:-2, 1:-1])

        self.grid = newGrid
        self.setBoundaris()
        self.change = self.calculateChange()

    # Functions for a Gauss-Seidel relaxation.
    def relaxationGaussSeidel(self, deltaV):
        while self.change > deltaV:
            begin = time.perf_counter()
            self.iterateGaussSeidel()
            end = time.perf_counter()
            self.timePerIteration.append(end - begin)
            self.iterationCount += 1

        print(f'Gauss-Seidel : Changement de {self.change * 100:.7f}% après {self.iterationCount} itérations')

    def iterateGaussSeidel(self):
        newGrid = self.grid.copy()
        self.prevGrid = self.grid.copy()

        indices = np.indices(newGrid.shape)
        r = indices[0][1:-1, 1:-1]
        mask = (indices[0] % 2 == 0) & (indices[1] % 2 == 0)
        notMask = ~mask
        mask[1::2] = notMask[:-1:2]
        self.mask = mask[1:-1, 1:-1]
        self.notMask = ~self.mask

        # Calcul du masque.
        arrayCaculated = (self.grid[:-2, 1:-1] + self.grid[2:, 1:-1] + self.grid[1:-1, :-2] + self.grid[1:-1, 2:]) / 4 \
                         + (1 / (8 * r)) * (self.grid[2:, 1:-1] - self.grid[:-2, 1:-1])
        newGrid[1:-1, 1:-1][self.mask] = arrayCaculated[self.mask]

        # Calcul de l'antimasque. A corriger!
        arrayCaculated = (newGrid[:-2, 1:-1] + newGrid[2:, 1:-1] + newGrid[1:-1, :-2] + newGrid[1:-1, 2:]) / 4 \
                         + (1 / (8 * r)) * (self.grid[2:, 1:-1] - self.grid[:-2, 1:-1])
        newGrid[1:-1, 1:-1][self.notMask] = arrayCaculated[self.notMask]

        self.grid = newGrid
        self.setBoundaris()
        self.change = self.calculateChange()

    # Functions for an over relaxation.
    def overRelaxation(self, deltaV, omega):
        while self.change > deltaV:
            begin = time.perf_counter()
            self.iterateOverRelaxation(omega)
            end = time.perf_counter()
            self.timePerIteration.append(end - begin)
            self.iterationCount += 1

        print(f'Sur-Relaxation : Changement de {self.change * 100:.7f}% après {self.iterationCount} itérations')

    def iterateOverRelaxation(self, omega):
        newGrid = self.grid.copy()
        self.prevGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][1:-1, 1:-1]
        newGrid[1:-1, 1:-1] = (self.grid[:-2, 1:-1] + self.grid[2:, 1:-1] + self.grid[1:-1, :-2] +
                               self.grid[1:-1, 2:]) / 4 + (1 / (8 * r)) * (self.grid[2:, 1:-1] -
                                                                           self.grid[:-2, 1:-1])
        overRelaxedGrid = (1 + omega) * newGrid - omega * self.prevGrid

        self.grid = overRelaxedGrid
        self.setBoundaris()
        self.change = self.calculateChange()
