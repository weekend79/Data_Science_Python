#Importing Numpy to generate random numbers
import numpy as np
#import matplot library
import matplotlib
from matplotlib import style

from matplotlib import pyplot as plt

randomNumber = np.random.rand(10)

print(randomNumber)
#print(style.available)

#Select the style of the plot
style.use('ggplot'),
#Plot the random number
plt.plot(randomNumber,'g',label='Line one', linewidth=2),
#X axis id number of random numbers (index)
plt.xlabel('Range'),
#yAxis is actual random number
plt.ylabel('Numbers'),
# Title of the plot
plt.title('First Plot'),
plt.legend

print(plt.show())
