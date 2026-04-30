import numpy as np

def magnitude(v):
    return np.linalg.norm(v)

def dot_product(a, b):
    return np.dot(a, b)

def angle_between(a, b):
    dot = np.dot(a, b)
    val = dot / (np.linalg.norm(a) * np.linalg.norm(b))
    val = np.clip(val, -1, 1)
    return np.degrees(np.arccos(val))

def projection(a, b):
    return (np.dot(a,b) / np.dot(b,b)) * b

# shows what would happen if vector 'a' is set to the exact same 
# line as vector 'b' , think of it like a project of 'a' into 'b'.

def rotate_vector(v, angle_deg):
    rad = np.radians(angle_deg)

    R = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])

    return R @ v

# R : standard rotation matrix  , since cos90 = 0 sin90 = 1
#     matrix becomes - [0 -1]
#                      [1  0]

# @ : matrix multiplication
# matrix 'R' @ vector 'v' = [-1,2] - means vector v (2,1) rotated 90 degrees counterclockwise - (-1,2).
                                 