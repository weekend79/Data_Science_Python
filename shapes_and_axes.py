import numpy as np

"""
2D Arrays
numpy_arr = np.array([x for x in range(1,10)])
print(numpy_arr)
print(numpy_arr.reshape(3,3))
"""
"""
3D ARRAYS
numpy_arr = np.array([x for x in range(1,13)])
print(numpy_arr.reshape(3,2,2))
"""
"""
3D ARRAYS
numpy_arr = np.array([x for x in range(1,13)])
print(numpy_arr.reshape(2,2,3))
"""

"""3D Array Flaten to 1D"""
numpy_arr = np.array([x for x in range(1,13)])
numpy_arr  = numpy_arr.reshape(-1)
print(numpy_arr)


