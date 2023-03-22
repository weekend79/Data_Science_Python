# Learing to use shape and ndim on Array's
import numpy as np


myArray = np.array(24)
print(myArray)

myOneDArray = np.array([1,2,3,4])
print(myOneDArray)

myTwoDArray = np.array([[1,1,1],[1,2,1]])
print(myTwoDArray)

myThreeDArray = np.array([[[1,1,1], [2,2,2]], [[3,3,3], [4,4,4]]])
#myThreeDArray = myThreeDArray.shape
myThreeDArray = myThreeDArray.ndim
print(myThreeDArray)
