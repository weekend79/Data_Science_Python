import numpy as np


z = np.array([i for i in range (12)])
np.where(z%2==0, 'Even', 'Odd')


condlist = [z<5,z>5]
choicelist = [z**2, z**3]

print(np.select(condlist,choicelist,default=z))
