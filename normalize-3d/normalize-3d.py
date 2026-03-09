import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v, dtype=float)
    norm = np.sqrt(np.sum(v**2, axis=-1, keepdims=True))
    safe_norm = np.where(norm > 1e-10, norm, 1.0)
    return np.where(norm >1e-10, v/safe_norm, v)
    
    