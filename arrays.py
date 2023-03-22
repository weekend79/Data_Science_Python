"""" Learning about array's, zero's, ones, empty, 
     arange, reshape, linespace, 1d, 2d and 
     3Dimensional array's """

import numpy as np


first_numpy_array = np.array([1,2,3,4])

print (first_numpy_array)

array_with_zeros = np.zeros((3,3))
print(array_with_zeros)

array_with_ones = np.ones((3,3))
print(array_with_ones)

array_with_empty = np.empty((2,3))
print(array_with_empty)

np_arange = np.arange(12)
print(np_arange)

np_rearange = np_arange.reshape(4,3)
print(np_rearange)

np_linspce = np.linspace(1,6,5)
print(np_linspce)

oneD_array = np.arange(15)
print(oneD_array)

TwoD_array = oneD_array.reshape(3,5)
print(TwoD_array)

ThreeD_array = np.arange(27).reshape(3,3,3)
print(ThreeD_array)

