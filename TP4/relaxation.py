import numpy as np


class Relaxation:
    def __init__(self, grid: np.ndarray):
        # The original and current grid.
        self.originalGrid = grid.copy()
        self.grid = grid
        self.prevGrid = None

    def iterate(self):
        newGrid = self.grid.copy()

        r = np.indices(self.grid.shape)[0][2:-2, 1:-1]
        newGrid[2:-2, 1:-1] = (self.grid[:-4, 1:-1] + self.grid[4:, 1:-1] + self.grid[2:-2, :-2] +
                               self.grid[2:-2, 2:]) / 4 + (1 / r) * (self.grid[3:-1, 1:-1] - self.grid[1:-3, 1:-1]) / 4

        self.prevGrid = np.copy(self.grid)
        self.grid = newGrid

    def __call__(self, iterations):
        for iteration in range(iterations):
            self.iterate()
