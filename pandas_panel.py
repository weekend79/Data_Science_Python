import pandas as pd

df = pd.read_csv(r'C:\Users\EntroBet\Desktop\PlayerSearch.csv', parse_dates = True)

print(df.head(5))

df.set_index(['Language', 'Registration Date'], inplace = True)

"""print(df.index)"""

print(df.loc['NO'])
