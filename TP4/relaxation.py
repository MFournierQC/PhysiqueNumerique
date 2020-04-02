import numpy as np


class Relaxation:
    def __init__(self, grid: np.ndarray):
        # The original and current grid.
        self.originalGrid = grid.copy()
        self.grid = grid
        self.prevGrid = None
        self.change = np.inf

    def iterate(self):
        newGrid = self.grid.copy()
        self.prevGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][2:-2, 1:-1]
        newGrid[2:-2, 1:-1] = (self.grid[:-4, 1:-1] + self.grid[4:, 1:-1] + self.grid[2:-2, :-2] +
                               self.grid[2:-2, 2:]) / 4 + (1 / (4 * r)) * (self.grid[3:-1, 1:-1] - self.grid[1:-3, 1:-1])

        self.grid = newGrid
        self.setBoundaris()
        self.change = self.calculateChange()

    def calculateChange(self):
        oldGrid = self.prevGrid.copy().flatten()
        newGrid = self.grid.copy().flatten()
        change = np.sqrt(np.sum((oldGrid - newGrid) ** 2))
        return change * 100

    def setBoundaris(self):
        self.grid[:3, :].fill(150)
        self.grid[19, :].fill(0)

    def __call__(self, precision):
        while self.change > precision:
            self.iterate()
