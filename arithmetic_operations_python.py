import numpy as np 
""" Adding array A an B together"""
A = np.array ([[1,2,1], [2,2,3]])
B = np.array ([3,4,5])

AB = np.add(A,B)


""" Adding array A an D together"""
A = np.array ([[1,2,1], [2,2,3]])
D = np.array ([3,4,5])

AD = np.subtract(D,A)
print(AD)


""" Adding array A an C together"""
A = np.array ([[1,2,1], [2,2,3]])
C = np.array ([3,4,5])

AC = np.multiply(C,A)
print(AC)

""" Adding array B an C together"""
B = np.array ([[1,2,1], [2,2,3]])
C = np.array ([3,4,5])

BC = np.divide(C,B)
print(BC)

""" The power of two """
A = np.array ([[1,2,1], [2,2,3]])
D = np.array ([3,4,5])

AD = np.power(A,2)
print(AD)


""" The power of D """
B = np.array ([[1,2,1], [2,2,3]])
D = np.array ([3,4,5])

BD = np.power(B,D)
print(BD)