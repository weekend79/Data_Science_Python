import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Name', 'Number of employees']

df = pd.read_csv(r'C:\Users\EntroBet\Desktop\orgSampleDB.csv', parse_dates = True)

df.set_index('Name').plot()
print(df.head())
print(plt.show())
