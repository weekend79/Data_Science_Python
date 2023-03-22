#Import required libraries
import matplotlib
from matplotlib import pyplot as plt


#Dataset from Ohio state, leading cause of death 2012
cause = 'Chronic Diseases', 'Unintential Injuries', 'Alzheimers', 'Influensa and Pneumonia', 'Sepsis', 'Other'
#Percentile
percentile = [62,5,4,2,1,26]

#Set the pie chart plot properties
#Set figure size
plt.figure(figsize=(10,10))
#explode the largest pie in the data set
explode = (0.05,0,0,0,0,0)
#Set pie chart properties
plt.pie(percentile, labels=cause, explode=explode, autopct='%1.1f%%', startangle=70)
#Set axis equal to draw pie as circle
plt.axis('equal')
#Set title of the pie chart
plt.title('Ohio State - 2012 : Leading Cause of death')
print(plt.show())