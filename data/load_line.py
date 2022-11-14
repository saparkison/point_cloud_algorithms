import numpy as np

from utils.lines import Line2D

def load_line(*, noise_sigma: float = 0.0) -> np.ndarray:
    """ Function that returns points on a line."""
    p = np.random.rand(2,2)
    line = Line2D.FromTwoPoints(p[:,0], p[:,1])

    x = np.random.rand(1,10)
    y = line.m * x + line.b

    points = np.vstack((x, y))
    if noise_sigma > 0.0:
        points = points + np.random.randn(points.shape[0], points.shape[1]) * noise_sigma

    return points
