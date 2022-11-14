import numpy as np

class SE2:
    """ Class representing the 2D special euclidean group of rigid body transformations """

    def __init__(self, R: np.ndarray = np.eye(2), t: np.ndarray = np.zeros((2,1))):
        self.R = R
        self.t = t

    def set_theta(self, theta_deg: float):
        theta = np.radians(theta_deg)
        c, s = np.cos(theta), np.sin(theta)
        self.R = np.array(((c, -s), (s, c)))

    def get_theta(self) -> float:
        return np.degrees(np.arctan2(self.R[0,1], self.R[0,0]))

    def inv(self):
        return SE2(self.R.T, - self.R.T @ self.t)

    def __matmul__(self, other):
        if isinstance(other, self.__class__):
            return SE2(self.R @ other.R, self.R @ other.t + self.t)
        elif isinstance(other, np.ndarray):
            return self.R @ other + self.t


