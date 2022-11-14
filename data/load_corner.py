import numpy as np

def load_corner(*, noise_sigma: float = 0.0) -> np.ndarray:
    """ Function to load a example 2D "corner" point cloud. """
    points = np.array([[0.0, 0.0], [0.0, 0.25], [0.0, 0.50], [0.0, 0.75], [0.0, 1.0], [0.25, 1.0]]).T
    if noise_sigma > 0.0:
        points = points + np.random.randn(points.shape[0], points.shape[1]) * noise_sigma
    return points
