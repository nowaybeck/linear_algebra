# import numpy as np

# a = np.array([3,4])
# b = np.array([4,1])

# dot = np.dot(a,b)

# print("Dot Product =", dot)


import numpy as np
from src.math_utils import dot_product, angle_between

a = np.array([3,4])
b = np.array([4,1])

print("Dot Product =", dot_product(a,b))
print("Angle =", angle_between(a,b))