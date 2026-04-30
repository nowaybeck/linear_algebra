import numpy as np
from src.math_utils import projection

a = np.array([3,4])
b = np.array([1,2])

print("Projection =", projection(a,b))

# shows what would happen if vector 'a' is set to the exact same 
# line as vector 'b' , think of it like a project of 'a' into 'b'.