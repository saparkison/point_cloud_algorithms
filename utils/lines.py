import numpy as np

class Line2D:
    """
    Class for representing 2D lines.

    stored internally as slope-intercept form, or y = m * x + b
    """
    def __init__(self, m: float = 0.0, b: float = 0.0):
        self.m = m
        self.b = b

    @classmethod
    def FromTwoPoints(self, p1: np.ndarray, p2: np.ndarray):
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return Line2D(m, b)

    def distance_to_point(self, p: np.ndarray) -> float:
        """
        using the equation:
        | ax + by + c | / \sqrt( a^2 + b^2)
        """
        return np.fabs(p[1] - self.m * p[0] - self.b) / np.sqrt(1 + self.m**2)


