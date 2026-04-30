import numpy as np
import matplotlib.pyplot as plt

theta = np.radians(90) 

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v = np.array([2,1])

new = R @ v

plt.quiver(0,0,v[0],v[1],color='blue',scale=1,angles='xy',scale_units='xy')
plt.quiver(0,0,new[0],new[1],color='red',scale=1,angles='xy',scale_units='xy')

plt.xlim(-3,3)
plt.ylim(-3,3)
plt.grid()
plt.title("Rotation")
plt.show()

# R : standard rotation matrix  , since cos90 = 0 sin90 = 1
#     matrix becomes - [0 -1]
#                      [1  0]

# @ : matrix multiplication
# matrix 'R' @ vector 'v' = [-1,2] - means vector v (2,1) rotated 90 degrees counterclockwise - (-1,2).
                                 