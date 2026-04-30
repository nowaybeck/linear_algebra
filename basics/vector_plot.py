# import numpy as np
# import matplotlib.pyplot as plt

# v = np.array([3,4])

# plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1)
# plt.xlim(-1, 6)
# plt.ylim(-1, 6)
# plt.grid()
# plt.title("Vector [3,4]")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from src.plot_utils import draw_vector

v = np.array([3,4])

fig = draw_vector(v, "Vector [3,4]")
plt.show()
