import pandas as pd
from pandas import DataFrame
import matplotlib 
from matplotlib import style
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv(r'C:\Users\morte\Desktop\ADANIPORTS.csv')

print(df.head())

#Select the style of the plot


df['H-L'] = df.High-df.Low

df['100MA'] = df('Close').rolling(100).mean() 

#Plotting 3D graph
ax = plt.axes(projection='3d')
ax.scatter(df.index,df['H-L'],df['100MA'])
ax.set_xlabel('Index')
ax.set_ylabel('H-L')
ax.set_zlabel('100MA')

print(plt.show())
