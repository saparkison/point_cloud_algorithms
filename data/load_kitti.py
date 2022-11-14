import numpy as np

def load_velo(file: str):
    """Load and parse a velodyne binary file."""
    pc = np.fromfile(file, dtype=np.float32)
    return pc.reshape((-1, 4))
