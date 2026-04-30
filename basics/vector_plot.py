import numpy as np
import matplotlib.pyplot as plt

v = np.array([3,4])

plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1)
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.grid()
plt.title("Vector [3,4]")
plt.show()

# quiver() : converts displacement into an arrow.
# angles='xy' : use the actual x-y coordinate.
# scale_units='xy' : measure arrow size inn graph units.
# scale=1 : arrow length stays same, no shrinking/stretching.
#     - intuition: 'scale' is a divisor for the arrow length.
#     think of it like "drawn length = actual length/scale"
# xlim()/ylim : x-axis range and y-axis range 
# grid() : shows grid lines 

    
