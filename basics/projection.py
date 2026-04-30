import numpy as np

a = np.array([3,4])
b = np.array([1,2])

proj = (np.dot(a,b)/np.dot(b,b))*b

print("Projection =", proj)

# shows what would happen if vector 'a' is set to the exact same 
# line as vector 'b' , think of it like a project of 'a' into 'b'.